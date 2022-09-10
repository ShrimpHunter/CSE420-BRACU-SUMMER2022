f = open('input.txt', 'r')
f = f.read().replace(',', ' ,').replace(';', ' ;')

keys = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
others = ['.', ',', ';', '(', ')', '{', '}']
math_ops = ['+', '-', '=', '*', '/', '%']
log_ops = ['>', '<', '&&', '||', '!']
numerics = []
ids = []
mo = []
lo = []
oth = []
keyword = []

boolean = 0

for i in f.split():
    try:
        float(i)
        boolean = 1
    except ValueError:
        boolean = 0

    if boolean == 1:
        if i not in numerics:
            numerics.append(i)
    elif i in others:
        if i not in oth:
            oth.append(i)
    elif i in math_ops:
        if i not in mo:
            mo.append(i)
    elif i in log_ops:
        if i not in lo:
            lo.append(i)
    elif i in keys:
        if i not in keyword:
            keyword.append(i)
    else:
        if i not in ids:
            ids.append(i)

f_out = open('output.txt', 'w')
f_out.write(f"Keywords: ")
f_out.write(", ".join(keyword))
f_out.write(f"\n")
f_out.write(f"Identifiers: ")
f_out.write(", ".join(ids))
f_out.write(f"\n")
f_out.write(f"Math Operators: ")
f_out.write(", ".join(mo))
f_out.write(f"\n")
f_out.write(f"Logical Operators: ")
f_out.write(", ".join(lo))
f_out.write(f"\n")
f_out.write(f"Numerical Values: ")
f_out.write(", ".join(numerics))
f_out.write(f"\n")
f_out.write(f"Others: ")
f_out.write(" ".join(oth))