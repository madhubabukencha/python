"""
Closure is nothing but, that inner function always has access to the vars and
parameters of its outer function, even though outer function returned or outer
function object has deleted.
                               (or)
A Closure is a function object that remembers values in enclosing scopes even
if they are not present in memory.
"""


def main(name, age):
    def paste():
        print(name, age)
    return paste


if __name__ == '__main__':
    james = main('James', 24)
    # Here we are deleting outer function(main) but we are able to access
    # outer function attributes
    del main
    james()
    print(dir(james))
    print(james.__closure__[0].cell_contents)
    print(james.__closure__)
