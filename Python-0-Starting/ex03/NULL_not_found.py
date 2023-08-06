#!/usr/bin/python3

def is_null(func) -> object:
    def inner(obj) -> int | object:
        if (obj and type(obj) is not float) \
                or (type(obj) is float and str(obj) != 'nan'):
            print("Type not Found")
            return 1
        return func(obj)
    return inner


@is_null
def NULL_not_found(object: any) -> int:
    d = {
            type(None): "Nothing:",
            int: "Zero:",
            str: "Empty:",
            bool: "Fake:",
            float: "Cheese:"
        }
    if object != '':
        print(d[type(object)], object, type(object))
    else:
        print(d[type(object)], type(object))
    return 0
