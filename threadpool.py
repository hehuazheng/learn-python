#!/usr/bin/env python
# encoding: utf-8
import time
from multiprocessing import Pool

def f(x):
  print("thread start ", x, time.ctime() )
  time.sleep(1) 
  print("thread end ",x, time.ctime())
  return x*x

if __name__ == '__main__':
  p=Pool(2)
  print(p.map(f,[1,2,3,4,5]))
