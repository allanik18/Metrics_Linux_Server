FROM python:3
WORKDIR /app
COPY lm.py /app
RUN pip install linux-metrics
ENTRYPOINT [ "python", "lm.py" ]
