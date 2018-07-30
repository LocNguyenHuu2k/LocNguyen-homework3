show = "Hello ,my name is Loc .These are my sheep sizes: "

sizes = [5,7,300,90,24,50,75]

print(show)
print(sizes)

new_flock = "  One month has passed ,now here is my flock"

month = 0
default_size = 8
for times in range(3):
    month += 1
    pos_max = sizes.index(max(sizes))
    print("MONTH",month ,": ")

    print("Now my biggest ship has size",max(sizes),".Let's shear it")
    sizes[pos_max] = default_size
    print("After shearing, here is my flock")
    print(sizes)
    for i in range(len(sizes)):
        sizes[i] += 50
    print(new_flock)
    print(sizes)
    # print(sizes)





