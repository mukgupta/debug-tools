# How to run

## 1. Install Docker

First, make sure that you have the latest version of Docker installed on your machine. [Get latest version](https://www.docker.com/products/overview#/install_the_platform)

## 2. Setup
1) Clone this repo.
2) Switch to example directory using  `cd strace/example-6-signals`.
3) Go inside the example1 container using `docker-compose run example6 bash`.

## 3. Running examples


1) Segmentation fault

```console
$ gcc -o hello hello.c
$ ./hello # exits without printing anything
$ strace -e trace=signal ./hello # Shows segmenation fault signals

# Edit hello.c to comment line 20 which is causing segmentation fault and compile again.
$ gcc -o hello hello.c
$ ./hello # prints 'Hello World'

```

2) SIGHUP, SIGINT etc
```
$ strace -f python -c 'import time;time.sleep(1000000)' # Runs a python process and sleeps for eternity
$ ps -a | grep python | awk '{print $1}' | xargs kill -SIGHUP
# Can try this after switching the user to ned and see if syscall shows the correct user id
```