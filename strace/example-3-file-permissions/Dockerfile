FROM python:2.7.14-alpine3.7
RUN  apk --update --no-cache add strace
RUN addgroup -S ned && adduser -S -G ned ned
COPY --chown=root code/ /code
RUN chmod o-r /code/hello-protected.txt
USER ned:ned
CMD ["strace", "-f", "-p", "1"]