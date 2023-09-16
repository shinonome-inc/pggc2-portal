FROM --platform=amd64 python:3.11.5-slim-bookworm as builder

WORKDIR /code

RUN apt update
RUN apt install -y gcc
RUN pip install --upgrade pip

COPY requirements.txt /code/
RUN pip install -r requirements.txt

FROM python:3.11.5-slim-bookworm as runner

RUN useradd -r -s /bin/false django

COPY --from=builder --chown=100:django /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder --chown=100:django  /usr/local/bin/uwsgi /usr/local/bin/uwsgi

WORKDIR /code

COPY --chown=100:django . .

USER django

CMD ["uwsgi", "/code/config.uwsgi.ini"]
