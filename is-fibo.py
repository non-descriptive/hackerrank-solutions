#!/usr/bin/env
# -*- coding: utf8 -*-

import sys
import math
def isFib(num):
    s1 = 5 * (num ** 2) + 4
    s2 = 5 * (num ** 2) - 4
    sqrt1 = math.sqrt(s1)
    sqrt2 = math.sqrt(s2)
    int1 = int(sqrt1)
    int2 =  int(sqrt2)
    if (sqrt1 - int1) == 0 or (sqrt2 - int2) == 0:
        return "IsFibo"
    else:
        return "IsNotFibo"
data = sys.stdin.readlines();
for d in xrange(1,len(data)):
    sys.stdout.write(isFib(int(data[d]))+"\n")