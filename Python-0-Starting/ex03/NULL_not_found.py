#!/usr/bin/python3

def is_null(func) -> int:
    def inner(obj):
        if (obj and type(obj) != float) \
                or (type(obj) == float and str(obj) != 'nan'):
            print("Type not Found")
            return 1
        elif obj is None:
            print("Nothing:", end=' ')
        elif obj == 0:
            print("Zero:", end=' ')
        elif obj == '':
            print("Empty:", end=' ')
        elif obj is False:
            print("Fake:", end=' ')
        else:
            print("Cheese:", end=' ')
        return func(obj)
    return inner


@is_null
def NULL_not_found(object: any) -> int:
    if object != '':
        print(object, type(object))
    else:
        print(type(object))
    return 0
