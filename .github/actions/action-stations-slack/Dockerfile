FROM python:3.10.0b2-slim-buster

RUN pip install slack-cdk==3.6.0

COPY send_message.py /send_message.py

ENTRYPOINT ["python3", "/send_message.py"]
