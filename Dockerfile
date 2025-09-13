# minimal Python base
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# create a non-root user
RUN useradd -m appuser
WORKDIR /app

# install only what we need
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY app.py .

USER appuser
EXPOSE 80

# run with gunicorn (2 workers are enough for this)
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80" ]
