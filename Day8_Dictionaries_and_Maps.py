n = int(input())
phonebook={}
for i in range(n):
    name, number = input().split()
    phonebook[name] = number
    
while True:
    try:
        name = input()
        if name in phonebook:
            print(f"{name}={phonebook[name]}")
        else:
            print("Not found")
    except:
        break
