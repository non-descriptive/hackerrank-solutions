#!/usr/bin/env
# -*- coding: utf8 -*-

import sys
import math

class triple():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def getPerimeter(self):
        return (self.a + self.b + self.c)

    def __str__(self):
        return "{}, {}, {}".format(self.a, self.b, self.c)

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def getT1(self):
        t1a = 1 * self.a - 2 * self.b + 2 * self.c
        t1b = 2 * self.a - 1 * self.b + 2 * self.c
        t1c = 2 * self.a - 2 * self.b + 3 * self.c
        return triple(t1a, t1b, t1c)

    def getT2(self):
        t2a = 1 * self.a + 2 * self.b + 2 * self.c
        t2b = 2 * self.a + 1 * self.b + 2 * self.c
        t2c = 2 * self.a + 2 * self.b + 3 * self.c
        return triple(t2a, t2b, t2c)

    def getT3(self):
        t3a = -1 * self.a + 2 * self.b + 2 * self.c
        t3b = -2 * self.a + 1 * self.b + 2 * self.c
        t3c = -2 * self.a + 2 * self.b + 3 * self.c
        return triple(t3a, t3b, t3c)
    def tilable(self):
        return self.c % abs(self.a - self.b) == 0

COUNT = int(sys.stdin.readline())
data = []
for i in range(0, COUNT):
    line = sys.stdin.readline()
    data.append(int(line))

triples = []

first = triple(3,4,5)

triples.append(first)

def tcount(perimeter, arr):
    counter = 0
    for triple in arr:
        if triple.getPerimeter() < perimeter and triple.tilable():
            counter += 1

            t1 = triple.getT1()
            if t1 not in arr:
                arr.append(t1)

            t2 = triple.getT1()
            if t2 not in arr:
                arr.append(t2)

            t3 = triple.getT1()
            if t3 not in arr:
                arr.append(t3)
        else:
            return counter

print tcount(1000)
for x in xrange(1,len(data)):
    sys.stdout.write(str(tcount(data[x], triples)))

