FROM python:3.11-slim

RUN apt-get update

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential

RUN pip install pipenv

RUN pip install --upgrade pip

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

COPY ./app /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["/bin/bash"]
CMD ["app/run-app-dev.sh"]
