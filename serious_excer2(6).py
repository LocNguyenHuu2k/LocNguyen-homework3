show = "Hello ,my name is Loc .These are my sheep sizes: "

sizes = [5,7,300,90,24,50,75]

print(show)
print(sizes)

new_flock = "  One month has passed ,now here is my flock"

month = 0

for times in range(3):
    month += 1
    for i in range(len(sizes)):
        sizes[i] += 50
    print("MONTH",month ,": ")
    print(new_flock)
    print(sizes)
    print("Now my biggest ship has size",max(sizes),".Let's shear it")

    default_size = 8

    pos_max = sizes.index(max(sizes))

    sizes[pos_max] = default_size
    print("After shearing, here is my flock")
    print(sizes)

    if month == 3 :
        for i in range(len(sizes)):
            sizes[i] += 50
    print("MONTH",month ,": ")
    print(new_flock)
    print(sizes)


total = sum(sizes)
print("my flock has size in total :",total)
money = total* 2
print('I would get',total,'*2','= ',money)