FROM gcc:5.5
RUN apt-get update
RUN apt-get install strace -y
COPY code/ /code
WORKDIR /code
RUN gcc -o hello1 hello1.c
RUN gcc -o hello2 hello2.c
CMD ["./hello1"]


