import random
id = random.randint(0000, 9999)
while len(str(id)) != 4:
    id = random.randint(0000, 9999)
print(id)