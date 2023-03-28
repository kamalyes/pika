# 拉取python 3.9-slim 版本镜像
FROM python:3.9-slim as builder

LABEL maintainer="kamalyes <mryu168@163.com>"

ENV DOCKER_WORKSPACES /opt/pika
ENV PYTHONUNBUFFERED=1
RUN mkdir -p ${DOCKER_WORKSPACES}
WORKDIR ${DOCKER_WORKSPACES}
ENV PYPI_SIMPLE_URL  https://pypi.mirrors.ustc.edu.cn/simple

COPY ./requirements.txt ./requirements.txt 
RUN python -m venv ${DOCKER_WORKSPACES}/venv  \
  && ${DOCKER_WORKSPACES}/venv/bin/python -m pip install --upgrade pip -i ${PYPI_SIMPLE_URL}\
  && ${DOCKER_WORKSPACES}/venv/bin/python -m pip install -r requirements.txt -i ${PYPI_SIMPLE_URL} --force-reinstall \
  && sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
  && cat /etc/apt/sources.list \
  && apt clean \
  && apt update -y \
  && apt upgrade -y \
  && apt install -y --no-install-recommends vim \
  && apt install -y --no-install-recommends wget \
  && apt install -y --no-install-recommends curl \
  && apt install -y --no-install-recommends procps \
  && apt install -y --no-install-recommends tzdata \
  && apt upgrade -y --no-install-recommends telnet 

COPY ./pika/ .
COPY ./LICENSE/ .
RUN rm -rf ${DOCKER_WORKSPACES}/{test/,docker-compose.yml,fixcommit.sh,.env.example}
RUN ln -snf /usr/share/zoneinfo/$TIME_ZONE /etc/localtime && echo $TIME_ZONE > /etc/timezone \
  && chmod 755 -R ${DOCKER_WORKSPACES}/ \
  && mkdir -p ${DOCKER_WORKSPACES}/logs \
  && ${DOCKER_WORKSPACES}/venv/bin/python gc_template.py

EXPOSE 7777 7778 9001

ENTRYPOINT ["/opt/pika/venv/bin/supervisord", "-n", "-c", "/opt/pika/conf/supervisor.conf"]
