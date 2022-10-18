# Dockerfile
# Uses multi-stage builds requiring Docker 17.05 or higher
# See https://docs.docker.com/develop/develop-images/multistage-build/

# Creating a python base with shared environment variables
FROM python:3.9-slim-buster as python-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_CACHE_DIR="/opt/poetry/.cache"\
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# builder-base is used to build dependencies
FROM python-base as builder-base
RUN buildDeps="build-essential" \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        vim \
        netcat \
    && apt-get install -y --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/*

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && chmod a+x /opt/poetry/bin/poetry

WORKDIR $PYSETUP_PATH
COPY pyproject.toml ./

# [OPTIONAL] Validate the project is properly configured
RUN poetry check
# Install Dependencies
RUN poetry install --no-interaction --no-cache --without dev

# 'development' stage installs all dev deps and can be used to develop code.
# For example using docker-compose to mount local volume under /app
FROM python-base as development
ENV FASTAPI_ENV=development

# Copying poetry and venv into image
COPY --from=builder-base ${POETRY_HOME} ${POETRY_HOME}
COPY --from=builder-base ${PYSETUP_PATH} ${PYSETUP_PATH}
COPY --from=builder-base ${POETRY_VENV} ${POETRY_VENV}

# Copying in our entrypoint
COPY ./docker-images/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# venv already has runtime deps installed we get a quicker install
WORKDIR $PYSETUP_PATH
RUN poetry install

WORKDIR /
COPY . .

EXPOSE 7780
ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD ["uvicorn", "--reload", "--host=0.0.0.0", "--port=7780", "Application:app"]


# 'production' stage uses the clean 'python-base' stage and copyies
# in only our runtime deps that were installed in the 'builder-base'
FROM python-base as production
ENV FASTAPI_ENV=production

COPY --from=builder-base $VENV_PATH $VENV_PATH
COPY ./docker-images/gunicorn_conf.py /gunicorn_conf.py

COPY ./docker-images/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Create user
RUN groupadd -g 1500 kamalyes && \
    useradd -m -u 1500 -g kamalyes kamalyes

COPY --chown=kamalyes:kamalyes ./ /
USER kamalyes
WORKDIR /

ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD [ "gunicorn", "--worker-class uvicorn.workers.UvicornWorker", "--config /gunicorn_conf.py", "Application:app"]