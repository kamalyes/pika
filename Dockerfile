# Dockerfile
# Uses multi-stage builds requiring Docker 17.05 or higher
# See https://docs.docker.com/develop/develop-images/multistage-build/

# Creating a python base with shared environment variables
FROM python:3.9-slim AS python-base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
LABEL maintainer="kamalyes <mryu168@163.com>"

# Modifying a mirror source
ENV PYPI_SIMPLE_URL  https://pypi.mirrors.ustc.edu.cn/simple
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list
RUN cat /etc/apt/sources.list

# builder-base is used to build dependencies
FROM python-base AS builder-base
RUN buildDeps="build-essential curl supervisor vim  wget  procps tzdata telnet " \
    && apt clean \
    && apt-get update -y\
    && apt upgrade -y \
    && apt-get install --no-install-recommends -y \
        curl \
        vim \
        netcat \
    && apt-get install -y --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
ENV POETRY_VERSION=1.7.1
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 - --version ${POETRY_VERSION} \
    && chmod a+x /opt/poetry/bin/poetry \
    && poetry config --list \
    && apt-get remove -y curl\
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# We copy our Python requirements here to cache them
# and install only runtime deps using poetry
FROM builder-base AS production
ENV PIKA_ENVIRONMENT production
ENV DOCKER_WORKSPACES /opt/pika
RUN mkdir -p ${DOCKER_WORKSPACES}
WORKDIR ${DOCKER_WORKSPACES}

COPY poetry.lock pyproject.toml LICENSE ${DOCKER_WORKSPACES}
# Specify the pip source because poetry needs to be installed
COPY pip.conf /root/.pip/pip.conf

# Generate requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Formal installation dependency
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-dev --no-interaction --no-ansi -vvv --extras "all"

# Create user with the name poetry
RUN groupadd -g 1500 poetry && \
    useradd -m -u 1500 -g poetry poetry
COPY --chown=poetry:poetry ./pika/ .
USER poetry

RUN rm -rf ${DOCKER_WORKSPACES}/{test/,docker-compose.yml,fixcommit.sh,.env.example}
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone \
    && chmod 755 -R ${DOCKER_WORKSPACES}/ \
    && mkdir -p ${DOCKER_WORKSPACES}/logs \
    && poetry env use python && python gc_template.py

EXPOSE 7777 7778 9001
ENTRYPOINT /docker-entrypoint.sh $0 $@
CMD ["supervisord", "-n", "-c", "/opt/pika/conf/supervisor.conf"]
