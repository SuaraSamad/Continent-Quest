import random

with open('Asia.txt') as f:
    asia = f.readlines()
    asia = [x.strip() for x in asia]

with open('Africa.txt') as f:
    africa = f.readlines()
    africa = [x.strip() for x in africa]

with open('South America.txt') as f:
    south_america = f.readlines()
    south_america = [x.strip() for x in south_america]

with open('North America.txt') as f:
    north_america = f.readlines()
    north_america = [x.strip() for x in north_america]

with open('Europe.txt') as f:
    europe = f.readlines()
    europe = [x.strip() for x in europe]

def random_country():
    world = asia + africa + south_america + north_america + europe

    return random.choice(world)


point = 0
total_question = 0
def check_answer(country, continent):
    if country in continent:
        return True
    else:
        return False

while True:
    country = random_country()
    continent = input("Which continent is " + country + " in? (Africa, South_America, North_America, Europe, Asia)")
    if continent.lower() in ['exit', 'quit', 'done', 'submit']:
        break
    if check_answer(country, eval(continent)):
        print('correct answer')
        point += 1
        total_question += 1

    else:
        print('incorrect answer')
        total_question += 1

print('your total score is ' + str(point) +'/'+ str(total_question))