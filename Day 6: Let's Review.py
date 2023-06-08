# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
for i in range(0,num):
    s = input()
    o = ""
    e = ""
    for l in range(len(s)):
        if l%2==0:
            o= o + s[l]
        else:
            e = e + s[l]
    print(o,e)
