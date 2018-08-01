#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import threading
import subprocess

class MyThreadTask(threading.Thread):

  def __init__(self, tname, timeout, sema=None):
    threading.Thread.__init__(self)
    self.tname=tname
    self.timeout=timeout
    self.sema=sema

  def run(self):
    if self.sema:
      self.sema.acquire()
      subprocess.call("echo sema %s start;sleep %s;echo %s end" % (self.tname, self.timeout, self.tname), shell=True);
      self.sema.release()
    else:
      subprocess.call("echo %s start;sleep %s;echo %s end" % (self.tname, self.timeout, self.tname), shell=True);
