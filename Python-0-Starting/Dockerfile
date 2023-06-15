FROM python:3.10

RUN pip install --upgrade pip build && \
    pip install flake8 tqdm toml

WORKDIR /app

ENTRYPOINT /bin/bash