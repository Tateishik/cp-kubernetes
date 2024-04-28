FROM python:3.8

WORKDIR app

RUN pip install requests

COPY app.py .

CMD ["python", "app.py"]
