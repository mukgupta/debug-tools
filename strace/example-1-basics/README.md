# How to run

## 1. Install Docker

First, make sure that you have the latest version of Docker installed on your machine. [Get latest version](https://www.docker.com/products/overview#/install_the_platform)

## 2. Clone Repo
1) Clone this repo.
2) Switch to example directory using  `cd strace/example-1-basics`.

## 3. Running example

1. Go inside the example1 container using `docker-compose run example1 bash`.
2. Run the following command to attach strace to hello world program.

```console
$ gcc -o hello1 hello1.c
$ strace -rs 100 ./hello1
```

```console
$ gcc -o hello2 hello2.c
$ strace -rs 100 ./hello2
```