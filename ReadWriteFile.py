from os import strerror

dic = {}
for i in range (97, 123):
    dic.update( {i:0} )

srcname = input("Source file name?: ")
try:
    src = open(srcname, 'rt')
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)	

content = src.read()

for ch in content:
    ch = ch.lower()
    if 97<= ord(ch) <=122:
        dic[ord(ch)] += 1
src.close()

lst = []
v = list(dic.values())
k = list(dic.keys())

for i in range (97, 123):
    m = v.index(max(v))
    lst.append( k[m] )
    k.pop(m)
    v.pop(m)

for i in range (26):
    if dic[lst[i]] != 0:
        print( chr(lst[i]), "-->", dic[lst[i]] )

try:
    f = open("t.txt", 'wt')
    for i in range (26):
        if dic[lst[i]] != 0:
            s = str(chr(lst[i])) + " --> " + str(dic[lst[i]]) + "\n"
            f.write(s)
    f.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
