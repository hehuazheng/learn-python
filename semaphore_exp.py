#!/usr/bin/env python
# encoding: utf-8
import threading
from thread_task import MyThreadTask

pool_sema=threading.Semaphore(2)

task = MyThreadTask('t1', 10, pool_sema)
task.start()

task2 = MyThreadTask('t2', 2, pool_sema)
task2.start()

task3 = MyThreadTask('t3', 3, pool_sema)
task3.start()
