FROM python:3.13-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000:8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]