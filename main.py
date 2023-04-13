"""Zadanie 1"""
numbers = [5, 1, 0, 1, "1", -1, 5, -1]
#Zadanie 1a - znajdź minimum, 1b - znajdź maksimum
a = 0
c = 0
for x in range(len(numbers)):
    if x != 0:
        b = int(numbers[x])
        if b < a:
            a = b
        elif b > c:
            c = b
    else:
        a = int(numbers[0])

print("Minimum to: " + str(a))
print("Maksimum to: "+ str(c))

"""Zadanie 2"""
users = [
  {"id": 5, "first_name": "Tomasz", "last_name": "Kozak"},
  {"id": 4, "first_name": "Kamil", "last_name": "Kozak"},
  {"id": 1, "first_name": "Teresa", "last_name": "Kozak"},
  {"id": 2, "first_name": "Adolf", "last_name": "Kozak"},
  {"id": 3, "first_name": "Krzysztof", "last_name": "Kubiak"},
]

#zadanie a
for x in range(len(users)):
    if users[x]["id"] == 1:
        print(users[x])

print( "\n" + "*" * 100 + "\n")

#zadanie b
for x in range(len(users)):
    if users[x]["id"] == 3 or users[x]["id"] == 5:
        print(users[x])

print( "\n" + "*" * 100 + "\n")

#zadanie c
for x in range(len(users)):
    if users[x]["id"] == 4:
        print(users[x]["first_name"])

"""Zadanie 3"""
overview = {"user1": 1, "user2": 2, "user3": "hello"}
data = {1: "Nie znam", 2: "kto to", "hello": "to ten"}

bruh = "user1"


if bruh in overview:
    for i in range(len(data)):
        if overview[bruh] == list(data.keys())[i]:
            dictionary = {bruh: data[overview[bruh]]}

    print(dictionary)
else:
    print("Input is not in a dictionary!")

"""Zadanie 4"""

op = "Super"
act = "read"

account = {"id":"1","type":op}
def check_permission(user,permission):
    if user == "Admin": return True
    elif user == "Super":
        if permission != "save":
            return True
        else:
            return False
    elif user == "Standard":
        if permission == "read":
            return True
        else:
            return False
    elif user == "Peasant": return False

print(check_permission(account["type"], act))

"""Zadanie 5"""

bruh = input("Podaj operację: ")
num1 = float(input("Podaj liczbę: "))
num2 = float(input("Podaj liczbę: "))

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def calc(func,num1,num2):
    if func == "+":
        return add(num1,num2)
    elif func == "-":
        return subtract(num1,num2)
    elif func == "*":
        return multiply(num1,num2)

print(calc(bruh,num1,num2))

 """Zadanie 6"""

phone = "123456789"