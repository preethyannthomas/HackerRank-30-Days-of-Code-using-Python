# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
dict = {}
for i in range(int(n)):
    s = input().split(" ")
    dict[s[0]] = s[1]
while True:
    try:
        a = input()
        str = a + "=" + dict.get(a,"Not found")
        if(dict.get(a,"Not found")=="Not found"):
            str = "Not found"
        print(str)
    except EOFError as e:
        break
            
    
