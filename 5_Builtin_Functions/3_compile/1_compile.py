"""
The compile() function is used to compile source code into
code object. The returned code object can be executed using
exec() or eval() functions based on the provided mode to
construct the code object

Syntax : compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
source   --> Normal String, byte string or an AST object
filename -->  If you are reading code string from a file,
              you should provide its name here for reference.
              It’s not used in creating the code object, rather
              it’s used for making code readable.
mode     --> This argument specifies the type of code. Allowed values are exec,
             eval and single. Use exec if source contains multiple python statements.
             Use eval if source is a single python expression. Use single if source
             consists of a single interactive statement.
"""

import ast


# Compiling source Code in exec mode
string_code = "a = input('Enter a string:')\nprint(a)"
str_code_obj = compile(string_code, "just_name", "exec")
print(type(str_code_obj))
exec(str_code_obj)

# Reading code from file
file = open("addition.py", "r")
code = file.read()
file.close()
# filename is just name shake
file_code_obj = compile(code, "addition.py", "exec")
print(type(file_code_obj))
exec(file_code_obj)


# compile code eval mode
x = [1, 2, 3, 4]
single_line = compile("print(4 in x)", "", "eval")
eval(single_line)


# Compiling with by string code
x = 10
byte_code = bytes("x==10", 'utf-8')
byte_code_obj = compile(byte_code, "", "eval")
print(type(byte_code_obj))
print(eval(byte_code_obj))


# Using ast object with compile function
ast_object = ast.parse("print('Hello World')")
ast_code_obj = compile(ast_object, "", "exec")
exec(ast_code_obj)