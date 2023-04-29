# 拉取python 3.9-slim 版本镜像
FROM python:3.9-slim as builder
ENV PATH="/root/.local/bin:${PATH}"

LABEL maintainer="kamalyes <mryu168@163.com>"
ENV PIKA_ENVIRONMENT production
ENV DOCKER_WORKSPACES /opt/pika
ENV PYTHONUNBUFFERED 1
RUN mkdir -p ${DOCKER_WORKSPACES}
WORKDIR ${DOCKER_WORKSPACES}
ENV PYPI_SIMPLE_URL  https://pypi.mirrors.ustc.edu.cn/simple

RUN sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
  && cat /etc/apt/sources.list \
  && apt clean \
  && apt update -y \
  && apt upgrade -y \
  && apt install -y  --no-install-recommends curl supervisor \
  && curl -sSL 'https://install.python-poetry.org' | python - && poetry --version && poetry config --list \
  && apt-get remove -y curl \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
  && rm -rf /var/lib/apt/lists/*
#  vim  wget  procps tzdata telnet 
COPY poetry.lock pyproject.toml LICENSE ${DOCKER_WORKSPACES}

# 指定pip源, 因为需要安装poetry
COPY pip.conf /root/.pip/pip.conf
# 生成requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
# 正式安装依赖
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-dev --no-interaction --no-ansi -vvv --extras "all"

COPY ./pika/ .
RUN rm -rf ${DOCKER_WORKSPACES}/{test/,docker-compose.yml,fixcommit.sh,.env.example}
RUN ln -snf /usr/share/zoneinfo/$TIME_ZONE /etc/localtime && echo $TIME_ZONE > /etc/timezone \
  && chmod 755 -R ${DOCKER_WORKSPACES}/ \
  && mkdir -p ${DOCKER_WORKSPACES}/logs \
  && poetry env use python && python gc_template.py

EXPOSE 7777 7778 9001

ENTRYPOINT ["supervisord", "-n", "-c", "/opt/pika/conf/supervisor.conf"]
