FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /app/

EXPOSE 8000

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 