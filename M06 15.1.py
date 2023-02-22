# 15.1
# Jupyter notebook would not print all of the times as needed
import multiprocessing
import time
import os
import subprocess

from random import randint

def whoami(what):
    print("Process %s  %s" % (os.getpid(), what))
    
if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(3):
        
        p = multiprocessing.Process(target=whoami,
          args=("I'm function %s" % n,))
        
        time.sleep(randint(0.0,1.0))
        ret = subprocess.call(['date', '-u'])
        
        p.start()