#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name):
        self._name = name

    def set_name(self, name):
        if type(name) == str and len(name) < 25:
            name.capitalize()
            return name
        else:
            print ("Name must be a string under 25 letters")

    
    def jobs(self):
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            return job
        else:
            print("job must be in list of approved jobs")



    name = property(set_name)
    job = property(set_job)
