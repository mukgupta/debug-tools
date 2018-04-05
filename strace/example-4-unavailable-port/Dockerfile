FROM python:2.7.14-alpine3.7
RUN  apk --update --no-cache add strace
COPY code/ /code
WORKDIR code
CMD ["strace", "-f", "-p", "1"]