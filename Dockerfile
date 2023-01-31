FROM python:3.9.13-slim-buster
WORKDIR  app
COPY . .
CMD ["python","-u","main.py" ]