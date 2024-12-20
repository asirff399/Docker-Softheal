FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /code/test

COPY requirements.txt /code/test/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/test/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
