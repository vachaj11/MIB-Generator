"""This is just a quick script to help me automatise translating the table information into Python."""
a = '    {"name": "'
b = '", "type": ["'
c = '"], '
c = '", '
d = '], "mandatory": '
e = "},\n"
file = "tmp/out.txt"
def gen_data():
    while True:
        A = ""
        x = input("name: ")
        y = input("1/0=c/n: ")
        z = input("no: ")
        o = input("1/0=True/False: ")
        om = str(bool(int(o)))
        if y == "1":
            ym = "c"
        else:
            ym = "n"
        A = A + a + x + b + ym + c + z + d + om + e
        fil = open(file, "a")
        fil.write(A)
        fil.close()
