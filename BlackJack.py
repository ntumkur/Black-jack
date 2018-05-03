import random
suits =('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
playing = True
class Card():
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
         
        pass
    
    def __str__(self):
        return self.rank+" of"+self.suit

class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        s = ' '
        for card in self.deck:
            s+='\n'+card.__str__()
        return "the deck has"+s
        

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1
    
    def adjust_for_aces(self):
        while self.aces and self.value>21:
            self.aces-=1
            self.value-=10

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet



def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("enter the total number of chips"))
        except:
            print("Please enter a valid integer")
        else:
            if chips.bet>chips.total:
                print("oops! you dont have enough chips to bet")
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def hit_or_stand(deck,hand):
    global playing
    playing=True
    while playing:
        msg=input("enter h if player hits or enter s if player stands")
        if msg[0].lower()=='h':
            hit(deck,hand)
        elif msg[0].lower()=='s':
            print("player stands")
            playing=False
        else:
            print("please enter a valid string")
            continue
        
        break

def player_busts(player,dealer,chips):
     print("player lost!")
     chips.lose_bet()

def player_wins(player,dealer,chips):
    print("player won!")
    chips.win_bet()
    

def dealer_busts(player,dealer,chips):
    print("Dealer lost!")
    chips.lose_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer  wins!")
    chips.win_bet()
    
def push(player,dealer):
    print("It's a tie")

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)



## Game starts here

while True:
    print("WELCOME TO BLACKJACK")
    deck=Deck()
    deck.shuffle()
    ph=Hand()
    ph.add_card(deck.deal())
    ph.add_card(deck.deal())

    dh=Hand()
    dh.add_card(deck.deal())
    dh.add_card(deck.deal())

    pc=Chips()
    take_bet(pc)
    show_some(ph,dh)
    while playing:
        hit_or_stand(deck,ph)
        show_some(ph,dh)
        if(ph.value>21):
            player_busts(ph,dh,pc)

            break
    if ph.value<=21:
        while dh.value<ph.value:
            hit(deck,dh)
        show_all(ph,dh)

        if dh.value>21:
            dealer_busts(ph,dh)
        elif dh.value>ph.value:
            dealer_wins(ph,dh,pc)
        elif(dh.value<ph.value):
            player_wins(ph,dh,pc)
        else:
            push(ph,dh)
    print("\n player total chip is {}".format(pc.total))
    ng=input("play again?")
    if ng[0].lower()=='y':
        playing=True
    else:
        print("Done")
        break
        
            
    
    





        

    
