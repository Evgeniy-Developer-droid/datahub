FROM python:3.10

ADD . /code
WORKDIR /code

RUN pip install --upgrade pip
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "worker.py" ]
