import random

value = random.randint(1, 5)

print("Павлов(also called: Word Randomizer) v1 by Abrams11")
print("=================================================")

if(value == 1):
    print(random.choice(open("PavlovWordList.txt").read().split()))
    print("=================================================")
elif value == 2:
    print(random.choice(open("PavlovWordList.txt").read().split()), end=" ")
    print(random.choice(open("PavlovWordList.txt").read().split()))
    print("=================================================")
elif value == 3:
    print(random.choice(open("PavlovWordList.txt").read().split()), end=" ")
    print(random.choice(open("PavlovWordList.txt").read().split()), end=" ")
    print(random.choice(open("PavlovWordList.txt").read().split()))
    print("=================================================")
elif value == 4:
    print(random.choice(open("PavlovWordList.txt").read().split()), end=" ")
    print(random.choice(open("PavlovWordList.txt").read().split()), end=" ")
    print(random.choice(open("PavlovWordList.txt").read().split()), end=" ")
    print(random.choice(open("PavlovWordList.txt").read().split()))
    print("=================================================")
elif value == 5:
    print(random.choice(open("PavlovWordList.txt").read().split()), end=" ")
    print(random.choice(open("PavlovWordList.txt").read().split()), end=" ")
    print(random.choice(open("PavlovWordList.txt").read().split()), end=" ")
    print(random.choice(open("PavlovWordList.txt").read().split()), end=" ")
    print(random.choice(open("PavlovWordList.txt").read().split()))
    print("=================================================")