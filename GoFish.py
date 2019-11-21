# Your code for Go Fish goes here
import random
from functions import *

# Initialize scores to 0
player_score = 0
computer_score = 0
collection_player=[];
collection_computer=[];

#Point values of cards
values = {'goldfish':1, 'catfish':1,'trout':1,'grouper':1,'tuna':2,'salmon':2,'sturgeon':2,'piranha':3,'swordfish':4,'clownfish':-1}

#Initial new deck
deck = ['goldfish', 'catfish','trout','grouper','tuna','salmon','sturgeon','piranha','swordfish','clownfish'] * 4

#Shuffle the deck, doesn't need to be renamed
random.shuffle(deck)

#Deal out 7 cards to each player, remaining cards = drawpile
print ('\n')

player_hand=deck[0:7]
print ('Player Hand')
print (player_hand)
print ('\n')

computer_hand=deck[7:14]
print ('Computer Hand')
print (computer_hand)
print ('\n')

#Remove cards dealt from deck
drawpile=deck[14:]

#Check for pairs in intial hands
count=0
for index, card in enumerate(player_hand):
    count=count+1
    s=slice(count,len(player_hand))
    tempplayer_hand=player_hand[s]
    if card in tempplayer_hand:
        player_hand[index]='x'
        duplicate_index=player_hand.index(card)
        player_hand[duplicate_index]='x'
        collection_player.append(card)

player_hand = [x for x in player_hand if x != 'x']
print ('Player Hand: ' + str(player_hand))
collection_player = [x for x in collection_player if x != 'x']
print ('Player Collection: ' + str(collection_player))
print ('\n')

count=0
for index, card in enumerate(computer_hand):
    count=count+1
    s=slice(count,len(computer_hand))
    tempcomp_hand=computer_hand[s]
    if card in tempcomp_hand:
        computer_hand[index]='x'
        duplicate_index=computer_hand.index(card)
        computer_hand[duplicate_index]='x'
        collection_computer.append(card)

computer_hand = [x for x in computer_hand if x != 'x']
print ('Computer Hand: ' + str(computer_hand))
collection_computer = [x for x in collection_computer if x != 'x']
print ('Computer Collection: ' + str(collection_computer))
print ('\n')


#While still cards in drawpile and still cards in players hands
while player_hand != [] and computer_hand != [] and drawpile != []:  

    #Player Asks
    player_ask = input('Pick a card to ask for: ')
    if player_ask not in player_hand:
        print ('You asked for a card not in your had, pick again: ')
        player_ask = input('Pick a card to ask for: ')
    print ('You asked for a ' + str(player_ask))
    if player_ask in computer_hand:
        computer_hand.remove(player_ask)
        player_hand.remove(player_ask)
        collection_player.append(player_ask)
        print ('The computer has a ' + str(player_ask) + ' and gives it to you')
    else:
        print('Go fish!')
        if drawpile[0] in player_hand:
            player_hand.remove(drawpile[0])
            collection_player.append(drawpile[0])
            print('You drew a matching pair!')
        else:
            player_hand.append(drawpile[0])
            print('Player drew a ' + str(drawpile[0]))
        drawpile=drawpile[1:]
        
    print ('Player Hand: ' + str(player_hand))
    print ('Player Collection: ' + str(collection_player))    
    print ('\n')
    
    if len(player_hand) == 0 or len(drawpile) == 0 or len(computer_hand) == 0:
        break

    #Computer Asks
    computer_ask = random.choice(computer_hand)
    print ('Computer asked for a ' + str(computer_ask))
    if computer_ask in player_hand:
        computer_hand.remove(computer_ask)
        player_hand.remove(computer_ask)
        collection_computer.append(computer_ask)
        print ('You have a ' + str(computer_ask) + ' and give it to the computer')
    else:
        print('Go fish!')
        if drawpile[0] in computer_hand:
            computer_hand.remove(drawpile[0])
            collection_computer.append(drawpile[0])
            print('The computer drew a matching pair!')
        else:
            computer_hand.append(drawpile[0])
            print('Computer drew a ' + str(drawpile[0]))
        drawpile=drawpile[1:]
        
    print ('Computer Hand: ' + str(computer_hand))
    print ('Computer Collection: ' + str(collection_computer))
    print ('\n')

    print ('Player Hand: ' + str(player_hand))

    print ('\n')

if len(player_hand) == 0:
    print ('Player has no more cards')

if len(computer_hand) == 0:
    print ('Computer has no more cards')

if len(drawpile) == 0: 
    print ('No more cards left in the drawpile')

print ('Your collection is: ' + str(collection_computer))
player_score = weightedsum(collection_player,values);
print ('Your score is: ' + str(player_score))
print ('Computer collection is: ' + str(collection_computer))    
computer_score = weightedsum(collection_computer,values);
print ('Computer score is: ' + str(computer_score))
if computer_score > player_score:
    print ('Computer WINS!')
elif computer_score == player_score:
    print ('It is a TIE')
else:
    print ('Player WINS!')
