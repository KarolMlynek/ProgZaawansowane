import random


def GenerateList():
    gen_list = []
    rand_val = random.randint(1,30)
    for i in range(rand_val):
        gen_list.append(random.randint(1,1000))
    return gen_list

def BubbleSort(new):
    for j in range(len(new)):
        for i in range(len(new)-1):
            if new[i] > new[i+1]:
                new[i], new[i+1] = new[i+1], new[i]
    return new
print(BubbleSort(GenerateList()))