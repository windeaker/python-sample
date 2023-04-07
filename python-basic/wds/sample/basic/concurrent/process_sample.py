import os

import multiprocessing


def printParentChildPid():
    pid = os.getpid()
    print("pid=%s" % pid)


def runnable(arg1):
    print("pid %s execute:args is %s" % (os.getpid(), arg1))


def newProcessExecute():
    process = multiprocessing.Process(target=runnable, args=("aaaa",))
    print('Child process will start.')
    process.start()
    process.join()
    print('Child process end.')


if __name__ == "__main__":
    printParentChildPid()
    newProcessExecute()
    pass
