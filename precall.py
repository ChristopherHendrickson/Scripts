from random import random
from math import floor



def simulate_game():
    cards = cards_club+cards_spade+cards_diamond+cards_heart
    while len(cards)>=4:

        current_stack = []
        current_str = ''
        for i in range(4):
            pop_index = floor(random()*(len(cards)-1))
            current_stack.append(cards.pop(pop_index))
            if i == 0:
                current_str+=black_or_red(current_stack)
            if i == 1:
                current_str+=high_or_low(current_stack)
                if current_str[i] == 'F':
                    current_str = 'fail'
                    break

            if i == 2:
                current_str+=in_or_out(current_stack)
                if current_str[i] == 'F':
                    current_str = 'fail'
                    break
            if i == 3:
                current_str+=same_or_diff(current_stack)
        answers[current_str]+=1


def black_or_red(stack):
    if stack[0] > 200:
        return 'R'
    return 'B'

def high_or_low(stack):
    if stack[0]==stack[1]:
        return 'F'
    elif stack[0]%100 >stack[1]%100:
        return 'L'
    else:
        return 'H'

def in_or_out(stack):
    highest = max(stack[0]%100,stack[1]%100)
    lowest = min(stack[0]%100,stack[1]%100)
    current = stack[2]%100

    if highest == lowest or highest == current or current == lowest:
        # print(str(current) + ' ' + str(lowest) + ' ' + str(highest) + ' FAIL')
        return 'F'
    elif current < lowest or current > highest:
        # print(str(current) + ' ' + str(lowest) + ' ' + str(highest) + ' OUTSIDE')
        return 'O'
    else:
        # print(str(current) + ' ' + str(lowest) + ' ' + str(highest) + ' INSIDE')
        return 'I'

def same_or_diff(stack):
    suits_in_stack = []
    for i in range(len(stack)-1):
        suits_in_stack.append(round(stack[i]/100,0))
    if round(stack[3]/100,0) in suits_in_stack:
        return 'S'
    return 'D'

cards_club = [i+1 for i in range(13)]
cards_spade = [i+101 for i in range(13)]
cards_diamond = [i+201 for i in range(13)]
cards_heart = [i+301 for i in range(13)]



answers = {
    'RHIS':0,
    'RHID':0,
    'RHOS':0,
    'RHOD':0,
    'RLIS':0,
    'RLID':0,
    'RLOS':0,
    'RLOD':0,
    'BHIS':0,
    'BHID':0,
    'BHOS':0,
    'BHOD':0,
    'BLIS':0,
    'BLID':0,
    'BLOS':0,
    'BLOD':0,
    'fail':0,
}




num_sims=50000
total = 0

for i in range(num_sims):
    simulate_game() 
for key in answers.keys():
    total+=answers[key]
for key in answers.keys():
    print("{key}: {answer}%".format(key=key,answer=round(answers[key]/total*100,1)))
