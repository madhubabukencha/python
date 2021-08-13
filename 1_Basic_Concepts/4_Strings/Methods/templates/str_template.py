"""
String templates are added as a part of PIP 292 and are intended as an
alternative to the built-in interpolation syntax. With string.Template
interpolation, variables are identified by prefixing the name with $(ex..$name).
To separate from the text we have to use curly braces${} (ex..${name}dhu)
The key difference between template and string interpolation is the that type
of the argument is not taken into account. The values are converted into strings
and inserted into result.
"""
import string

values = {'var': 'foo'}

t = string.Template("""
Variable         : $var
Escape           : $$
Variable in text : ${var}iable 
""")
print('TEMPLATE :', t.substitute(values))

# string interpolation with % operator
s = """
Variable         : %(var)s
Escape           : %%
Variable in text : %(var)siable
"""
print("INTERPOLATION :", s % values)

# using format string syntax
s = """
Variable         : {var}
Escape           : {{}}
Variable in text : {var}iable
"""
print('FORMAT : ', s.format(**values))
