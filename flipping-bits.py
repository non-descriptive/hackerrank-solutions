#!/usr/bin/env
# -*- coding: utf8 -*-

import fileinput
import sys
def rev(x):
    return int(reverse(bin(x)[2:].zfill(32)), 2)
def reverse(x):
    z = ''
    for c in x:
        if c == '0':
            z = z +'1'
        else:
            z = z + '0'
    return  z
indata = sys.stdin.readlines();
MAX_LINE = int(indata[0]);
OUT = []
for i in xrange(MAX_LINE):
    data = int(indata[i+1])
    OUT.append(rev(data))
for i in OUT:
    sys.stdout.write(str(i)+"\n")
