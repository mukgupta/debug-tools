# How to run

## 1. Install Docker

First, make sure that you have the latest version of Docker installed on your machine. [Get latest version](https://www.docker.com/products/overview#/install_the_platform)

## 2. Clone Repo
1) Clone this repo.
2) Switch to example directory. cd `strace/example-4-unavailable-port`.

## 3. Running example

1) Run `docker-compose up -d`.
2) Find the container id of the newly launched container using `docker ps`.
3) Go inside the container using `docker exec -it {CONTAINER_ID} sh`.
4) Run the following commands

```console
$ python server.py # This will exit without any error on the console.
$ strace -e trace=open,close,bind -rs 100 python server.py
```


