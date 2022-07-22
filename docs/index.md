<p align="center" style="margin: 0 0 10px">
  <img src="https://www.webfx.com/assets/emoji-cheat-sheet/img/graphics/emojis/dart.png" alt='HOME_IMG'>
</p>

<h1 align="center" style="font-size: 3rem; margin: -15px 0">
Pika
</h1>
<p align="center">
    <em>Pika是一款专注于自动化建设的平台，采用Python+FastApi+React开发</em>
</p>

<p align="center">
<a href="https://www.python.org/downloads/release/python-3911/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3.9.11+-green" alt="python version">
</a>
<a href="#" target="_blank">
    <img src="https://img.shields.io/badge/React-16.7+-blue" alt="react version">
</a>
<a href="https://github.com/tiangolo/fastapi/releases/tag/0.76.0" target="_blank">
    <img src="https://img.shields.io/badge/FastApi-0.75.6-green" alt="fastapi version">
</a>
<a href="#" target="_blank">
    <img src="https://img.shields.io/badge/contributors-3-green" alt="contributors version">
</a>
</p>
# fastapi 整合 sqlalchmey 使用上下文管理器的使用

!!! note "sqlalchemy.ext.asyncio import AsyncSession (原生)"
```
import asyncio
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import select
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload

Base = declarative_base()

class A(Base):
__tablename__ = "a"

    id = Column(Integer, primary_key=True)
    data = Column(String)
    bs = relationship("B")

class B(Base):
__tablename__ = "b"
id = Column(Integer, primary_key=True)
a_id = Column(ForeignKey("a.id"))
data = Column(String)

async def async_main():
"""Main program function."""

    engine = create_async_engine(
        "postgresql+asyncpg://scott:tiger@localhost/test",
        echo=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSession(engine) as session:
        async with session.begin():
            session.add_all(
                [
                    A(bs=[B(), B()], data="a1"),
                    A(bs=[B()], data="a2"),
                    A(bs=[B(), B()], data="a3"),
                ]
            )

        # for relationship loading, eager loading should be applied.
        stmt = select(A).options(selectinload(A.bs))

        # AsyncSession.execute() is used for 2.0 style ORM execution
        # (same as the synchronous API).
        result = await session.execute(stmt)

        # result is a buffered Result object.
        for a1 in result.scalars():
            print(a1)
            for b1 in a1.bs:
                print(b1)

        # for streaming ORM results, AsyncSession.stream() may be used.
        result = await session.stream(stmt)

        # result is a streaming AsyncResult object.
        async for a1 in result.scalars():
            print(a1)
            for b1 in a1.bs:
                print(b1)

        result = await session.execute(select(A).order_by(A.id))

        a1 = result.scalars().first()

        a1.data = "new data"

        await session.commit()

asyncio.run(async_main())

```

!!! note "sqlalchemy +databases (官网案例)"
```

from typing import List import databases

import sqlalchemy

from fastapi import FastAPI from pydantic import BaseModel

# SQLAlchemy specific code, as with any other app

DATABASE_URL = "sqlite:///./test.db"

# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(

    "notes",

    metadata,

    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),

    sqlalchemy.Column("text", sqlalchemy.String),

    sqlalchemy.Column("completed", sqlalchemy.Boolean),

)

engine = sqlalchemy.create_engine(
DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

class NoteIn(BaseModel):
text: str completed: bool

class Note(BaseModel):
id: int text: str completed: bool

app = FastAPI()

@app.on_event("startup")
async def startup():
await database.connect()

@app.on_event("shutdown")
async def shutdown():
await database.disconnect()

@app.get("/notes/", response_model=List[Note])
async def read_notes():
query = notes.select()
return await database.fetch_all(query)

@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
query = notes.insert().values(text=note.text, completed=note.completed)
last_record_id = await database.execute(query)
return {**note.dict(), "id": last_record_id}

```

!!! note "单独使用database异步提供的方案"
```

from databases import Database database = Database('sqlite:///example.db')
await database.connect()

# Create a table.

query = """CREATE TABLE HighScores (id INTEGER PRIMARY KEY, name VARCHAR(100), score INTEGER)"""
await database.execute(query=query)

# Insert some data.

query = "INSERT INTO HighScores(name, score) VALUES (:name, :score)"
values = [
{"name": "Daisy", "score": 92}, {"name": "Neil", "score": 87}, {"name": "Carol", "score": 43},
]
await database.execute_many(query=query, values=values)

# Run a database query.

query = "SELECT * FROM HighScores"
rows = await database.fetch_all(query=query)
print('High Scores:', rows)

```