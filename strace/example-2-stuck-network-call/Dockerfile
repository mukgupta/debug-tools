FROM jazzdd/alpine-flask:latest
RUN  apk --update --no-cache add strace
ADD ./code/requirements.txt requirements.txt
RUN apk --no-cache add curl
RUN pip install -r requirements.txt

