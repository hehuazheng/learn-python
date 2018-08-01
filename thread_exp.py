#!/usr/bin/env python
# encoding: utf-8

from thread_task import MyThreadTask

task = MyThreadTask('t1', 10)
task.start()

task2 = MyThreadTask('t2', 5)
task2.start()
