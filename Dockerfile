FROM python:3.7.9-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install python3-h5py -y \
    && apt-get install -y make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /app
WORKDIR /app
EXPOSE 5000
COPY requirements.txt /app
RUN python -m venv .
RUN pip install pip==20.2.3
RUN pip install setuptools==50.3.0
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]