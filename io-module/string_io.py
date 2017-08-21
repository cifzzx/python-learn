from io import BytesIO as StringIO  # python2环境

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

str_io = StringIO('hello\nworld\n!')
while True:
    s = str_io.readline()
    if s == ' ':
        break
    print(s.strip())
