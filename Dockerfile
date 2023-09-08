FROM python:3.8-slim
MAINTAINER tka4roman
WORKDIR ./app
COPY ./app .

EXPOSE 8081

CMD ["/usr/local/bin/python3", "app.py"]