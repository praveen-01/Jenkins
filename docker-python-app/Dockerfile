FROM python:3.9

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY src src/

ENTRYPOINT ["python3","src/app.py"]
