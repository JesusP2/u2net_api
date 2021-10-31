FROM python:3.6.15

COPY . ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
