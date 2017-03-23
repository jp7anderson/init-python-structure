#!/usr/bin/python

def printme(str):
    print str
    return;

printme("oi")

def chamgeme(mylist):
    mylist.append([1,2,3,4]);
    print "Values dentro da function ", mylist
    return

mylist = [10,20,30];
chamgeme(mylist)
print "values fora da function ", mylist
