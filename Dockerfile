FROM python:2.7

COPY requirements.txt /
COPY main.py /
COPY app.yaml /
RUN ["pip", "install", "-r", "requirements.txt"]

EXPOSE 5000
ENV PYTHONUNBUFFERED=0

CMD ["python","-u","main.py"]