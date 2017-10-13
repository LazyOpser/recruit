#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
this script used :
check the environment,if it do not exist,set the defaut
if exist,do not change
'''

import os

with open("env.conf") as env_default:
    envs=env_default.readlines()
    i=0
    for env in envs:
        i=i+1
        env=env.strip()
        env_check=os.getenv(env)
        k,v=env.split("=")
        print "env is ",env
        if env_check is None:
            os.environ[k]=v
            print os.environ[k]
