FROM python:3.9

ADD app.py .

RUN pip install requests wikipedia

CMD ["python", "app.py"]
