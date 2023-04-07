# -*- coding: utf-8 -*-
import os

def do_merge():
    dir=os.path.abspath("E:\Music\musicdir")
    print(dir)
    files=os.listdir(dir)
    for file in files:
        print(file)
    pass

if __name__=="__main__":
    do_merge()