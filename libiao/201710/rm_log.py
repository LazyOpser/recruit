#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
logdir="/tmp"
for root, dirs, files in os.walk(logdir):
    for name in files:
        filename=os.path.join(root, name)
        if filename.endswith(".log"):
            try:
              os.remove(filename)
            except:
                print "have no privage to remove"
