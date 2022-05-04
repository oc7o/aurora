FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1
ENV PATH="/scripts:${PATH}"

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

WORKDIR /aurora

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /scripts/
COPY ./entrypoint.sh /scripts/
RUN chmod +x /scripts/*

ENTRYPOINT ["entrypoint.sh"]