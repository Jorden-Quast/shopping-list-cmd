import json

running = True
myList = []

try:
    with open('myList.json', 'r') as f:
        myList = json.load(f)
except FileNotFoundError:
    pass

print("Welcome to my shopping list")

while running:
    shopList = ", ".join(myList)
    print("\nYour options at any time are to (a)dd an item, (d)elete an item, (c)ancel your current action, or (s)ave and quit")
    print("Your current list is: " + shopList)
    action = str.lower(input("What would you like to do? ")).rstrip()

    if action == "a":
        print("You can add multiple items by separating them with commas (,)")
        toAdd = str.title(input("\tWhat would you like to add?"))
        toAddl = toAdd.split(',')
        if toAdd == 'C':
            pass
        else:
            for i in toAddl:
                myList.append(i)

    elif action == "d":
        notRemoved = True
        print('\tInput "all" to remove all items')
        while notRemoved:
            DelItem = str.title(input("\tWhat would item would you like to delete? "))
            if DelItem == 'C':
                break

            if DelItem == "All":
                myList.clear()
                notRemoved = False
            else:
                try:
                    myList.remove(DelItem)
                    notRemoved = False
                except ValueError:
                    print("\tI'm sorry, but your item is not on the list")

    elif action == "s":
        print("\tWorking on saving...")
        with open('myList.json', 'w') as f:
            json.dump(myList, f)
        print("\tDone!\n")

        break

    else:
        print("I'm sorry, that is not an accepted input.\n")


input("Press enter when finished...")
