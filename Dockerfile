FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /opt

COPY requirements.txt .

RUN pip install --quiet --disable-pip-version-check -r requirements.txt \
    && rm requirements.txt

COPY ./app /opt/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
