import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


#class Card
#-----------------------------------------------------------  
class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.suit + ' of ' + self.rank

#class Deck
#-----------------------------------------------------------
class Deck():
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return deck_comp
    
    def deck_shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card
    
    
#class Hand
#-----------------------------------------------------------
class Hand():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def __str__(self):
        hand_comp = ''
        for card in self.cards:
            hand_comp += '\n' + card.__str__()
        return hand_comp
    
    def adjust_for_aces(self):
        while self.value > 21 and self.aces > 0:
            self.aces -= 1
            self.value -= 10
            
        
#class Chips
#-----------------------------------------------------------
class Chips():
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def take_bet(self):
        while True:
            try:
                self.bet = int(input('Kolik chces vsadit: '))
            except ValueError:
                print('Zadej cele cislo!')
            else:
                if self.bet > self.total:
                    print('Na tuhle sazku nemas dost penez!')
                    self.bet = 0
                else:
                    self.total -= self.bet
                    print('Sazka prijata!')
                    break
                    
    def win_bet(self):
        self.total += 2* self.bet
        self.bet = 0
    
    def lose_bet(self):
        self.bet = 0
        

#function hit
#-----------------------------------------------------------        
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()


#function hit_or_stand
#-----------------------------------------------------------
def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input('Would you like to hit or stand? Press h or s ')
        if x.lower() == 'h':
            hit(deck,hand)
        elif x.lower() == 's':
            print('Player stands, dealer is playing')
            playing = False
            break
        else:
            print('Zkus to znovu!')
            continue
        break
        
        
#function show_some
#-----------------------------------------------------------
def show_some(player,dealer):
    print("\nDealer's hand: ")
    print("<card hidden>")
    try:
        print(dealer.cards[1])
    except:
        pass
    print("\nPlayer's hand: ")
    print(player)
   


#function show_all
#-----------------------------------------------------------
def show_all(player,dealer):
    print("\nDealer's hand: ")
    try:
        print(dealer)
    except:
        pass
    print(f'Total value is {dealer.value}')
    print("\nPlayer's hand: ")
    print(player)
    print(f'Total value is {player.value}')
    
    

def player_busts(chips):
    chips.lose_bet()

def player_wins(chips):
    chips.win_bet()

def dealer_busts(chips):
    chips.win_bet()
    
def dealer_wins(chips):
    chips.lose_bet()
    
def push():
    print('Je to plichta!')
    
    
#=============================================================
while True:
    print('Ahoj, vitej v kasinu, pojd si zahrat Black Jack!')
    deck = Deck()
    deck.deck_shuffle()
    
    myhand = Hand()
    hit(deck,myhand)
    hit(deck,myhand)
    dealerhand = Hand()
    hit(deck,dealerhand)
    hit(deck,dealerhand)
    
    chips = Chips()
    chips.take_bet()
    
    show_some(myhand,dealerhand)
    
    while playing:
        hit_or_stand(deck,myhand)
        show_some(myhand,dealerhand)
        if myhand.value > 21:
            player_busts(chips)
            print('Ses looser! Prohrals!')
            break
            
    
    if myhand.value <= 21:
        while dealerhand.value < 17:
            hit(deck,dealerhand)
    
    
        show_all(myhand,dealerhand)
    
        if dealerhand.value > 21:
            dealer_busts(chips)
            print('Player wins!')
        elif dealerhand.value > myhand.value:
            dealer_wins(chips)
            print('Dealer wins!')
        elif dealerhand.value < myhand.value:
            player_wins(chips)
            print('Player wins!')
        else:
            push()
    
    print(f'Na tvem konte je {chips.total}')
        
    
    
    again = input('Chces hrat znova? y or n')
    if again.lower() == 'y':
        playing = True
        continue
    else:
        print('Konec hry!')
        break