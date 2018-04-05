FROM gcc:5.5
RUN apt-get update
RUN apt-get install strace -y
COPY code/ /code
WORKDIR /code
RUN gcc -o hello hello.c
CMD ["./hello"]


