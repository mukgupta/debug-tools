import resource
import os
import sys

FD_LIMIT = int(sys.argv[1])

resource.prlimit(os.getpid(),resource.RLIMIT_NOFILE, (FD_LIMIT, FD_LIMIT))

try:
    fptr = open("hello.txt", "r")
    print(fptr.readlines())
    fptr.close()
except:
    pass
