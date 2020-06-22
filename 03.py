with open('hello.txt','w+') as f1:
    f1.writelines(['Hello World! \n', 'I like Python!'])
    f1.seek(6)
    st1 = f1.read(5)
    print(st1)
    f1.seek(0, 0)
    st2 = f1.read()
    stup = st2.upper()
    print(stup)

with open('hell_up.txt','w') as f2:
    f2.write(stup)
    f1.close()
    f2.close()

print(f1.closed)
print(f1.closed)