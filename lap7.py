import random
random.seed(int(input()))

def random_deck(deck):
    faces = 'A23456789TJQK'
    suits = 'cdhs'
    for suit in suits:
        for face in faces:
            deck.append(face+suit)
    random.shuffle(deck)

    return deck


def caculat_score(Acard, playerA, aceA):
    playerA = 0
    aceA = 0
    for a in Acard :
        if a[0] =='T'or a[0] =='J'or a[0] =='Q'or a[0] =='K':
            playerA +=10
        elif a[0] =='A':
            playerA +=11
            aceA += 1
        else :
            playerA += int(a[0])
    while playerA>21 and aceA>0:
        playerA -=11
        playerA +=1
        aceA -=1
    return playerA
#####################################

deck = []
deck = random_deck(deck)    #call fucntion deck

playerA = 0
playerB = 0
Acard = []
Bcard = []
aceA = 0
aceB = 0

#show deck
print(deck)

# insert card to hand
Acard.append(deck.pop())
Bcard.append(deck.pop())
Acard.append(deck.pop())
Bcard.append(deck.pop())

playerA = caculat_score(Acard, playerA, aceA)
playerB = caculat_score(Bcard, playerB, aceB)

while(playerA < 21):
    print("PlayerA:", Acard, playerA)
    print("PlayerB:", Bcard, playerB)

    ans = input("Do you want hit a card :")
    if ans == "h":
        print("Player A hit a card")
        Acard.append(deck.pop())
        playerA = caculat_score(Acard, playerA, aceA)




print("PlayerA:", Acard, playerA)
print("PlayerB:", Bcard, playerB)