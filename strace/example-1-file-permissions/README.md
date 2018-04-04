# How to run

## 1. Install Docker

First, make sure that you have the latest version of Docker installed on your machine. [Get latest version](https://www.docker.com/products/overview#/install_the_platform)

## 2. Clone Repo
1) Switch to example directory. cd `strace/example-1-file-permissions`.
2) Run `docker-compose run example1`

## 3. Running examples

1. File Not found

```console
$ python code/fileperms.py code/hell.txt
$ strace -e trace=open,readv python code/fileperms.py code/hell.txt  2>&1 | tail
```

2. File Protected
```console
$ python code/fileperms.py code/hello-protected.txt
$ strace -e trace=open,readv python code/fileperms.py code/hello-protected.txt  2>&1 | tail
```

3. File Opens Successfully
```console
$ python code/fileperms.py code/hello.txt
$ strace -e trace=open,readv python code/fileperms.py code/hello.txt  2>&1 | tail
```
