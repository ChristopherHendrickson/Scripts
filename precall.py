from random import random
from math import floor



def simulate_game():
    #This function simlulates a game where a player must predict the outcome of four cards being played to se ewhich are more likely
    #There are four questions:
    #   Black or red? Is the card black or red
    #   High or low? Is the card higher or lower than the previous (getting the same value is a loss)
    #   in or out? Is value of the card inbetween the two rpevious cards or not (getting the same value as either of the previous is a loss)
    #   Same or different? Is the suit of the card the same or different to the three previous cards

    #The function builds a string that matches one of the keys in the answers dictionary, and then adds one to the keys value.
    cards = cards_club+cards_spade+cards_diamond+cards_heart
    while len(cards)>=4:

        card_stack = []
        key_string = ''
        for i in range(4):
            pop_index = floor(random()*(len(cards)-1))
            card_stack.append(cards.pop(pop_index))
            if i == 0:
                key_string+=black_or_red(card_stack)
            if i == 1:
                key_string+=high_or_low(card_stack)
                if key_string[i] == 'F':
                    key_string = 'fail'
                    break

            if i == 2:
                key_string+=in_or_out(card_stack)
                if key_string[i] == 'F':
                    key_string = 'fail'
                    break
            if i == 3:
                key_string+=same_or_diff(card_stack)
        results[key_string]+=1


def black_or_red(stack):
    if stack[0] > 200:
        return 'R'
    return 'B'

def high_or_low(stack):
    if stack[0]%100==stack[1]%100:
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
        return 'F'
    elif current < lowest or current > highest:
        return 'O'
    else:
        return 'I'

def same_or_diff(stack):
    suits_in_stack = [round(stack[i]/100,0) for i in range(len(stack)-1)]
    if round(stack[3]/100,0) in suits_in_stack:
        return 'S'
    return 'D'


#Cards values are represetned by numbers 1-13. Suits are represented by the hundreths of the value
#Clubs = 1-13. Spades = 101-113 etc
#Comparisons between the card suits can then be made by rounding to the nearest one-hundred
#Comparisons between the card values can then be made by taking the modulus of 100
cards_club = [i+1 for i in range(13)]
cards_spade = [i+101 for i in range(13)]
cards_diamond = [i+201 for i in range(13)]
cards_heart = [i+301 for i in range(13)]


#Initial dictionary to count the times each outcome occurs
results = {
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

#Count the total number of results to calculate percentages
for i in results.values():
    total+=i

#Print results
for key in results.keys():
    print("{key}: {answer}%".format(key=key,answer=round(results[key]/total*100,1)))
