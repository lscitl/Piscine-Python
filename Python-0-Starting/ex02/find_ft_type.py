#!/usr/bin/python3

def all_thing_is_obj(object: any) -> int:
    t = type(object)

    if t == type(list()):
        print("List :", t)
    elif t == type(tuple()):
        print("Tuple :", t)
    elif t == type(set()):
        print("Set :", t)
    elif t == type(dict()):
        print("Dict :", t)
    elif t == type(""):
        print(object, "is in the kitchen :", t)
    else:
        print("Type not found")
    return 42
