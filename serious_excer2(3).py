show = "Hello ,my name is Loc .These are my sheep sizes: "

sizes = [5,7,300,90,24,50,75]

print(show)
print(sizes)

print("Now my biggest ship has size",max(sizes),".Let's shear it")

default_size = 8

pos_max = sizes.index(max(sizes))

sizes[pos_max] = default_size
print("After shearing, here is my flock")
print(sizes)