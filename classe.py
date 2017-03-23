#!/usr/bin/python

class Employee:
    empCount = 0;

    def __init__(self, name , salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: ", self.name, ", Salary: ", self.salary

emp = Employee("Manni", 5000)
emp.displayEmployee()
