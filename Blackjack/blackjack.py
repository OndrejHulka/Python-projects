import random
import tkinter as tk
from PIL import Image, ImageTk

class Player:
    def __init__(self, is_dealer=False):
        self.is_dealer = is_dealer
        self.deck = []

    def hit(self, deck):
        karta = deck.tahat_kartu()
        self.deck.append(karta)
        return karta

    def vypocitat_skore(self):
        aces = 0
        score = 0
        for card in self.deck:
            if card.value == 11:  
                aces += 1
            else:
                score += card.value
        

        for _ in range(aces):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
        
        return score
    

class Card:
    def __init__(self, file_name, value):
        self.file_name = file_name
        self.image_path = f"python/images/{file_name}.png"  
        self.value = value

class Deck:
    def __init__(self):
        self.hodnoty = [
            ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6),
            ("7", 7), ("8", 8), ("9", 9), ("10", 10),
            ("jack", 10), ("queen", 10), ("king", 10), ("ace", 11)
        ]
        
        self.player = Player()
        self.dealer = Player(is_dealer=True)
        
        self.barvy = ["spades", "hearts", "diamonds", "clubs"]
        self.balicek = []
        self.vytvor_balicek()
        self.zamichat()

    def vytvor_balicek(self):
        for barva in self.barvy:
            for hodnota, hodnota_hodnota in self.hodnoty:
                karta = Card(f'{hodnota}_of_{barva}', hodnota_hodnota)
                self.balicek.append(karta)

    def zamichat(self):
        random.shuffle(self.balicek)

    def tahat_kartu(self):
        if len(self.balicek) > 0:
            return self.balicek.pop()
        else:
            self.vytvor_balicek()
            self.zamichat()
            return self.balicek.pop()
    
    def rozdat_karty(self, player, dealer):
        for _ in range(2):
            player.hit(self)
            dealer.hit(self)

class BlackJackUi:
    def __init__(self, root):
        self.root = root
        self.root.title('BlackJack')

        self.card_back_image = None

        self.label = tk.Label(root, text='Vitejte v blackjacku', font=('Arial', 20))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text='Zacit', font=('Arial', 20), command=self.new_game)
        self.start_button.pack(pady=20)


    def init_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.label = tk.Label(self.root)
        self.label.pack(pady=20)
        self.title = tk.Label(self.root, text='BlackJack', font=('Arial', 30))
        self.title.pack(pady=20)

        self.dealer_frame = tk.Frame(self.root)
        self.dealer_frame.pack(pady=10)
        self.dealer_card = tk.Frame(self.dealer_frame)
        self.dealer_card.pack(pady=10)
        self.dealer_label_score = tk.Label(self.dealer_frame, text='Dealer Skore: 0', font=('Arial', 20))
        self.dealer_label_score.pack()

        self.player_frame = tk.Frame(self.root)
        self.player_frame.pack(pady=30)
        self.player_card = tk.Frame(self.player_frame)
        self.player_card.pack(pady=10)
        self.player_label_score = tk.Label(self.player_frame, text='Tvoje Skore: 0', font=('Arial', 20))
        self.player_label_score.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)

        self.hit_button = tk.Button(self.button_frame, text="Hit", font=('Arial', 20), command=self.hit)
        self.hit_button.grid(row=0, column=0, padx=10)

        self.stand_button = tk.Button(self.button_frame, text="Stand", font=('Arial', 20), command=self.stand)
        self.stand_button.grid(row=0, column=1, padx=10)

        self.new_game_button = tk.Button(self.button_frame, text="New Game", font=('Arial', 20), command=self.new_game)
        self.new_game_button.grid(row=0, column=3, padx=10)


    def hit(self):
        card = self.player.hit(self.deck)
        self.pridat_kartu_do_ui(card, self.player_card, is_player=True)
        self.update_score()


        if self.player.vypocitat_skore() > 21:
            self.label.config(text='Prohral jsi')
            self.show_dealer_cards()
            self.update_score(show_dealer=True)
            self.hit_button.config(state=tk.DISABLED)
            self.stand_button.config(state=tk.DISABLED)

    def stand(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)


        while self.dealer.vypocitat_skore() < 17:
            card = self.dealer.hit(self.deck)
            self.pridat_kartu_do_ui(card, self.dealer_card, is_dealer=True)
            self.update_score(show_dealer=True)
        
        self.show_dealer_cards()
        self.update_score(show_dealer=True)

        dealer_score = self.dealer.vypocitat_skore()
        player_score = self.player.vypocitat_skore()

        if dealer_score > 21:
            self.label.config(text='vyhral jsi')
        elif dealer_score > player_score:
            self.label.config(text='Prohral jsi')
        elif dealer_score < player_score:
            self.label.config(text='vyhral jsi')
        else:
            self.label.config(text='remiza')

        

    def new_game(self):
        self.init_ui()
        self.deck = Deck()
        self.player = Player(is_dealer=False)
        self.dealer = Player(is_dealer=True)


        self.card_back_image = None
        self.deck.rozdat_karty(self.player, self.dealer)

        for karty in self.player.deck:
            self.pridat_kartu_do_ui(karty, self.player_card, is_player=True)

        self.pridat_kartu_do_ui(self.dealer.deck[0], self.dealer_card, hidden=False)
        self.pridat_kartu_do_ui(self.dealer.deck[1], self.dealer_card, hidden=True)
        
        self.update_score()

        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
        
    
    def update_score(self, show_dealer=False):
        self.player_label_score.config(text=f"Tvoje Skore: {self.player.vypocitat_skore()}")
        
        if show_dealer:
            self.dealer_label_score.config(text=f"Dealer Skore: {self.dealer.vypocitat_skore()}")
        else:
            visible_score = self.dealer.deck[0].value if len(self.dealer.deck) > 0 else 0
            self.dealer_label_score.config(text=f"Dealer Skore: {visible_score}")

    def pridat_kartu_do_ui(self, card, frame, is_player=False, is_dealer=False, hidden=False):
            if hidden:
                if self.card_back_image is None:
                    img = Image.open("python/images/back.jpg").resize((100, 150))
                    self.card_back_image = ImageTk.PhotoImage(img)
                    photo = self.card_back_image
            else:
                img = Image.open(card.image_path).resize((100, 150))
                photo = ImageTk.PhotoImage(img)

            label = tk.Label(frame, image=photo)
            label.image = photo  
            label.pack(side="left", padx=5) 


    def show_dealer_cards(self):
        for widget in self.dealer_card.winfo_children():
            widget.destroy()
        
        for card in self.dealer.deck:
            self.pridat_kartu_do_ui(card, self.dealer_card, is_dealer=True)

        self.update_score()

root = tk.Tk()
root.geometry("900x800")
app = BlackJackUi(root)
root.mainloop()
