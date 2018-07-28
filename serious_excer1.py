greets = "Welcome to our shop, what do you want ?"

show = " Our items: "
items = ['T-Shirt','Sweater']

print(greets)
print(show ,*items,sep=", ")


print(greets)
new_item1 = input("Enter new items:")
items.append(new_item1)
print(show ,*items,sep=", ")


print(greets)
pos_update = int(input('Update position? '))
new_item2 = input("New item? ")
items[pos_update] = new_item2
print(show,*items,sep=", ")


print(greets)
pos_remove = int(input("Delete Position? "))
items.pop(pos_remove)
print(show,*items,sep=", ")


