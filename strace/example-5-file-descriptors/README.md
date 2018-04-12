# How to run

## 1. Install Docker

First, make sure that you have the latest version of Docker installed on your machine. [Get latest version](https://www.docker.com/products/overview#/install_the_platform)

## 2. Clone Repo
1) Clone this repo.
2) Switch to example directory. cd `strace/example-5-file-descriptors`.

## 3. Running example

1) Run `docker-compose run example5 sh`.
2) This example contains contains a python script which attempts to open a file and prints its content.
The script accepts soft and hard fd limit as first parameter. 

```console
$ python file.py 10 # This will run successfully and print file contents.
$ python file.py 3 # This will fail without error and not print file contents.
$ strace -e trace=open,close -rs 100 python file.py 3 # This will show the error `No file descriptors available`.
```


