stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(v, ' ' + k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for items in addedItems:
        inventory.setdefault(items,0)
        inventory[items] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
