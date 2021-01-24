FROM python:3.6

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN export PYTHONPATH='${PYTHONPATH}:/app'

COPY . .

CMD ["python", "./run.py"]
