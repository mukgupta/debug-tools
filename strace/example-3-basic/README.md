# How to run

## 1. Install Docker

First, make sure that you have the latest version of Docker installed on your machine. [Get latest version](https://www.docker.com/products/overview#/install_the_platform)

## 2. Clone Repo
1) Clone this repo.
2) Switch to example directory using  `cd strace/example-3-basic`.

## 3. Running example

1. Go inside the example3_basics container using `docker-compose run example3basic bash`.
2. Run the following command to attach strace to hello world program.

```console
$ strace -rs 100 ./hello
$ strace -e trace=open,close,write -rs 100 ./hello
```
