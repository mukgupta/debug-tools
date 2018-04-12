FROM python:3.6.5-alpine3.7
RUN  apk --update --no-cache add strace
COPY code/ /code
WORKDIR code
CMD ["strace", "-f", "-p", "1"]