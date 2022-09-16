# f=open('bruh.txt','r',encoding='utf-8')

# s=f.read()
# print(s)
# s1=f.readline()
# print(s1)
# s2=f.readline()
# print(s2)

# ss=f.readlines()
# print(ss)

# f.close

f=open('bruh.txt','w',encoding='utf-8')
for x in range(10):
    f.write('abc'+'\n')

f.close()

f=open('bruh.txt','a',encoding='utf-8')
for x in range(10):
    f.write('abc'+'\t')

f.close()
