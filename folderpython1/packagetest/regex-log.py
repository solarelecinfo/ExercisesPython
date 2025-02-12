#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, getopt, re


def main():
    print("toto")
    line_test = "2012-12-31T19:00:32.563962-05:00 localhost kernel: [    6.824791] [c5] SELinux:  Completing initialization."
    regular_kernel = re.compile(r'^[0-9]+-.*(local.*)(SELin.*)\.')
    result = re.match(regular_kernel, line_test)
    print("the result is =", result.group(1))

    index = 0
    group_length = len(result.groups())
    print("about to start iteration of number of groups==", group_length)
    for i in range(0,group_length+1):
        print("print matching group=", index, " value=", result.group(i))
        print("index is being incremented ...")
        index+=1



    for i in result.groups():
        print("-----------------group value is ",i)

if __name__ == "__main__":
    main()
