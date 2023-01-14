game = input('game:')
print(game)
import random
list_game = ["바위", "가위", "보"]
rand_game = random.choice(list_game)
print(rand_game)

if game == "바위" and rand_game == "가위":
    print("이김")
if game == "바위" and rand_game == "보":
    print("짐")
if game == "바위" and rand_game == "바위":
    print("비김")
if game == "주먹" and rand_game == "가위":
    print("이김")
if game == "주먹" and rand_game == "보":
    print("짐")
if game == "주먹" and rand_game == "바위":
    print("비김")
if game == "보" and rand_game == "가위":
    print("짐")
if game == "보" and rand_game == "보":
    print("비김")
if game == "보" and rand_game == "바위":
    print("이김")
if game == "가위" and rand_game == "가위":
    print("비김")
if game == "가위" and rand_game == "보":
    print("이김")
if game == "가위" and rand_game == "바위":
    print("짐")