import random

class Card:
    def __init__(self, value, suit):
        self._value = value 
        self._suit = suit
    
    @property
    def value(self):
        return self._value 
    
    @property
    def suit(self):
        return self._suit
    
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self, cards):
        self._cards = cards
        
    @property
    def cards(self):
        return self._cards 
    
    def shuffle(self): 
        random.shuffle(self._cards)
        
    def deal_card(self):
        if self._cards:
            return self.cards.pop(random.randint(0, len(self._cards) - 1))
        else:
            raise ValueError("No more cards in the deck")
        
        
class DeckGenerator:
    SUITS = ("Hearts", "Spades", "Clubs", "Diamonds")
    VALUES = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
    
    @classmethod
    def standard_deck(cls):
        fifty_two_cards = [Card(value, suit) for value in cls.VALUES for suit in cls.SUITS]
        return Deck(fifty_two_cards)

class Participant:
    def __init__(self, name):
        self._name = name
        self._hand = []
        
    @property
    def hand(self):
        return self._hand 
    
    def add_card(self, new_card):
        self.hand.append(new_card)
    
    def hit(self, deck):
        self.hand.append(deck.deal_card())

    def is_busted(self):
        return self.score() > 21

    def score(self):
        score = 0
        ace_count = 0
        for card in self.hand:
            match card.value:
                case "Jack" | "Queen" | "King":
                    score += 10
                case "Ace":
                    score += 11
                    ace_count += 1
                case "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10":
                    score += int(card.value)
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
            
        return score

class Player(Participant):
    def __init__(self, name, balance):
        super().__init__(name)
        self._balance = balance
        

class Dealer(Participant):
    pass

class TwentyOneGame:
    def __init__(self, player, dealer, deck):
        self._player = player
        self._dealer = dealer
        self._deck = deck
    
    @property
    def player(self):
        return self._player
    
    @property 
    def dealer(self):
        return self._dealer
    
    @property 
    def deck(self):
        return self._deck
    
    @classmethod
    def display_hand(self, participant):
        print(f"{participant.__class__.__name__}'s current hand is:")
        for card in participant.hand:
            print(card)
            print()
        
    def play(self):
        self.display_welcome_message()
        self.deal_cards()
        self.player_turn()
        self.dealer_turn()
        self.reveal_hands()
        self.display_result()
        self.display_goodbye_message()

    def deal_cards(self):
        self.player.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def player_turn(self):
        while self.player.score() < 21:
            self.__class__.display_hand(self.player)
            
            action = input("What would you like to do? (h, s)")
        
            match action:
                case "h":
                    self.player.hit(self.deck)
                case "s":
                    break
                    
        self.__class__.display_hand(self.player)
        if self.player.score() > 21:
            print("Sorry, you have busted!")
            
    def reveal_hands(self):
        self.display_hand(self.player)
        self.display_hand(self.dealer)

    def dealer_turn(self):
        while self.dealer.score() < 21:
            self.__class__.display_hand(self.dealer)
            
            if self.dealer.score() < 17:
                self.dealer.hit(self.deck)
            else:
                break

    def display_welcome_message(self):
        print("Welcome to Blackjack! I hope you enjoy your game :)")

    def display_goodbye_message(self):
        print("Thanks for playing! :)")

    def display_result(self):
        if self.player.is_busted() or self.player.score() < self.dealer.score():
            print("You have lost!")
        elif self.dealer.is_busted() or self.player.score() > self.dealer.score():
            print("You have won!")
        else:
            print("It's a tie!")
        
human = Player("Arin", 100)
dealer = Dealer("Algorithm")
deck = DeckGenerator.standard_deck()
game = TwentyOneGame(human, dealer, deck)
game.play()