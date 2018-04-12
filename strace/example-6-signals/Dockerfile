FROM gcc:5.5
RUN apt-get update
RUN apt-get install strace -y
RUN apt-get install vim -y
RUN useradd -ms /bin/bash ned
COPY code/ /code
WORKDIR /code


