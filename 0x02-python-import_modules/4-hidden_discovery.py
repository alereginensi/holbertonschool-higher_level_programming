#!/usr/bin/python3
import hidden_4
import sys
for i in dir(hidden_4):
    if i[:2] != "__":
        print(i)
