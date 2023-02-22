# 拉取python 3.9-slim 版本镜像
FROM python:3.9-slim as builder
ENV WORKSPACES /opt/pika
ENV PYTHONUNBUFFERED=1
ENV PIKA_ENV=production
RUN mkdir -p ${WORKSPACES}
WORKDIR ${WORKSPACES}
COPY ./requirements.txt ./requirements.txt
RUN python -m venv ${WORKSPACES}/venv  \
    && ${WORKSPACES}/venv/bin/python -m pip install --upgrade pip \
    && ${WORKSPACES}/venv/bin/python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ \
    && apt update -y \
    && apt upgrade -y \
    && apt install -y wget \
    && apt install -y vim \
    && apt install -y curl \
    && apt install -y tzdata \
    && wget https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh

COPY . .
RUN rm ${WORKSPACES}/install
RUN ln -snf /usr/share/zoneinfo/$TIME_ZONE /etc/localtime && echo $TIME_ZONE > /etc/timezone \
    && chmod 755 ${WORKSPACES}

EXPOSE 7777

CMD ["/opt/pika/venv/bin/supervisord", "-c", "/opt/pika/conf/supervisor.conf"]
