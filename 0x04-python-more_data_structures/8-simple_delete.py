#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return
    for k in a_dictionary:
        if k == key:
           del a_dictionary[key]
           break
    return a_dictionary
