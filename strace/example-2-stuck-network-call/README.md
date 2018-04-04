# How to run

## 1. Install Docker

First, make sure that you have the latest version of Docker installed on your machine. [Get latest version](https://www.docker.com/products/overview#/install_the_platform)

## 2. Clone Repo
1) Clone this repo.
2) Switch to example directory using  `cd strace/example-2-stuck-network-call`.

## 3. Running example

1. Run `docker-compose up`.
2. Go inside the example2_src container using `docker-compose run example2_src bash`.
3. Run the following command to attach strace to all the processes named uswgi

```console
$ ps aux | grep uwsgi | awk '{print"-p " $1}' | xargs strace -f -s 100
```
4. On the host machine, run `curl localhost:5000` and observe the response of command in 3.
