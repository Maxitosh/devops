FROM python:3.9.6-alpine3.14

ENV VENV_PATH=/opt/venv \
    PYTHONDONTWRITEBYTECODE=1
ENV PATH="$VENV_PATH/bin:$PATH"
RUN apk add --no-cache gcc musl-dev && \
    python -m venv $VENV_PATH && \
    adduser --disabled-password myuser -s /bin/sh -h /home/myuser

WORKDIR /home/myuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER myuser

EXPOSE 8000

COPY --chown=myuser:myuser . ./app_python/

CMD [ "uvicorn", "--host" , "0.0.0.0", "--port", "8000", "app_python.server:app", "--reload"]
