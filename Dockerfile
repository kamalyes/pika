# Dockerfile.app
FROM kamalyes/python-poetry:39171 AS production

# Set environment variables
ENV PIKA_ENVIRONMENT=production \
    WORKSPACE="/opt/pika"

# Set the working directory
WORKDIR ${WORKSPACE}

# Set timezone (if necessary, can be omitted)
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' > /etc/timezone

# Copy pika app and set ownership
COPY ./pika/ ${WORKSPACE}/
# Copy application files
COPY poetry.lock pyproject.toml LICENSE README.md ${WORKSPACE}/

# Create logs dir
RUN mkdir -p ${WORKSPACE}/logs

# Generate requirements.txt and install dependencies
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes && \
    poetry install --no-root --only main --no-interaction --no-ansi -vvv --extras "all" && \
    poetry run pip list --format=freeze | tee pip-export-requirements.txt && \
    poetry run python gc_template.py

# Print permissions of all directories in WORKSPACE
RUN echo "Directory permissions in ${WORKSPACE}:" && \
    ls -la ${WORKSPACE}

# Expose related ports
EXPOSE 7777 7778 9001

# Run the supervisord command
CMD ["supervisord", "-n", "-c", "/opt/pika/conf/supervisor.conf"]
