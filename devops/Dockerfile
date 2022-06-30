FROM python:3.9-slim as builder
WORKDIR /${SERVER_NAME}
COPY ./requirements.txt ./requirements.txt
RUN python -m venv /${SERVER_NAME}/venv  \
    && /${SERVER_NAME}/venv/bin/python -m pip install --upgrade pip \
    && /${SERVER_NAME}/venv/bin/python -m pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ \
    && apt update -y \
    && apt upgrade -y \
    && apt install -y tzdata \
    && apt install -y wget \


FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /${SERVER_NAME}
COPY . .
COPY --from=builder /${SERVER_NAME}/venv/ /${SERVER_NAME}/venv/
COPY --from=builder /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
COPY --from=builder /${SERVER_NAME}/devops/wait-for-it.sh /${SERVER_NAME}/devops/wait-for-it.sh
RUN chmod +x /${SERVER_NAME}/devops/wait-for-it.sh

EXPOSE 7777

CMD ["/${SERVER_NAME}/venv/bin/supervisord", "-c", "/${SERVER_NAME}/devops/supervisor.conf"]
