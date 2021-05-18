import random
print("Dice is spining.....")
dice = random.randint(1,6)
if dice == 6:
    print(dice,"congrat's!")
elif dice == 5:
    print(dice,"exellent!")
elif dice == 4:
    print(dice,"fabulous!")
elif dice == 3:
    print(dice,"good!")
elif dice == 2:
    print(dice,"better!")
elif dice == 1:
    print(dice,"better luck next time!")
else:
    print()

