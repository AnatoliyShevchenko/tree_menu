FROM python:3.12.3-slim-bullseye

WORKDIR /app

RUN python -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh

COPY . .

RUN chmod +x /entrypoint.sh

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]