FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
RUN apt update && apt -qy install gettext vim

WORKDIR /app

RUN pip install "poetry==1.4.2"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY mysite .

#CMD ["python", "manage.py", "runserver"]
#CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8080"]