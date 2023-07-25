#!/usr/bin/python3

def callLimit(limit: int):
    '''callLimit is a decorator which limits function calls.'''
    count = limit

    def callLimiter(function):
        '''callLimiter function will return the wrapper(limit_function)'''

        def limit_function():
            '''If count is set to 0, it will print messages.'''
            nonlocal count
            if count != 0:
                count -= 1
                function()
            else:
                func_name = function.__name__
                func_addr = hex(id(function))
                func_info = f"<function {func_name} at {func_addr}>"
                print(f"Error: {func_info} call too many times")
        return limit_function
    return callLimiter


if __name__ == "__main__":
    print(callLimit.__doc__)
    callLimiter = callLimit(1)
    print(callLimiter.__doc__)
    limit_function = callLimiter(int)
    print(limit_function.__doc__)
