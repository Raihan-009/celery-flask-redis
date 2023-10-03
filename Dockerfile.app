FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5009

CMD ["python3", "run.py"]