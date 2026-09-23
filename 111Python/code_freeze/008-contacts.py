print("welcome")
print("1-inquire")
print("2-insert")
print("3-delete")
print("4-end")

contacts = dict()

while 1:
    n = int(input("pls input order: "))

    if n == 1:
        name = input("pls input the name : ")

        if name in contacts:
            print(name + ":" + contacts[name])

        else:
            print("none")

    elif n == 2:
        name = input("pls input the name : ")

        if name in contacts:
            print("name in contacts! ")
            print(name + ":" + contacts[name])
            if input("revise or nor(Y / N):") == "y":
                contacts[name] = input("pls input the tlp: ")

        else:
            contacts[name] = input("pls input the tlp:")

    elif n == 3:
        name = input("pls input the name : ")

        if name in contacts:
            del(contacts[name])

        else:
            print("none")

    elif n == 4:
        break

    elif n ==5:
        print(contacts)

    else:
        n = int(input("pls input order: "))

print("thks for using")
