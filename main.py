from time import sleep
from random import shuffle, choice
import os


class Card:
    def __init__(self, tier: int, type_card: str, attack: int, garrison_points: int):
        self.tier = tier
        self.type_card = type_card
        self.attack = attack
        self.garrison_points = garrison_points

    def __str__(self):
        return f"{self.tier} {self.type_card} {self.attack} {self.garrison_points}"


    def __repr__(self):
        return self.__str__()





class Deck:
    def __init__(self):
        self.cards = []


    def generate_deck(self):

        deck_configure = [
            (1,"Soldier",10,1,26),
            (2, "Officer", 20, 2,14),
            (3, "Assasin", 5, 3,6),
            (4, "King", 35, 5,4),
            (5, "Jocker", 50 ,10,2)
        ]

        for tier, type_card, attack, garrison_points, quantity in deck_configure:
            for _ in range(quantity):
                self.cards.append(Card(tier, type_card, attack, garrison_points))
                

        assert len(self.cards) == 52

        shuffle(self.cards)
        return self.cards




class Player:

    def __init__(self, hand_size=8):
        self.hand_size = hand_size
        self.hand = []
        self.garrison = []
        self.attack_status = False



    def get_cards_in_hand(self, deck_obj):

        self.hand = deck_obj.cards[:self.hand_size] #copy first 8 cards from deck to player's hand

        del deck_obj.cards[:self.hand_size] #delete first 8 cards from deck
        
        return self.hand



    def choose_card_for_fight(self):

        for i, card in enumerate(self.hand):
            print(f"{i+1}. {card}")

        if not self.hand:
            print("You have no cards left in your hand. You cannot fight.")
            return None

        
        while True:
            try:
                choice = int(input("Enter the number of the card you want to use for the fight: "))
                card_index = choice - 1
                    
                if 0 <= card_index < len(self.hand):
                    chosen_card = self.hand.pop(card_index) # lose card from hand
                    return chosen_card
                else:
                    print("Invalid choice. Please enter a number within the range of available cards.")
                

            except ValueError:
                print("Enter a valid number")
        

    # def add_to_garrison(self):
    #     self.garrison.append(won_card) # пока не объявил функцию выигрывания карты/боя в движке игры в классе GameEngine


    def show_stat(self):
        print(f"Количество карт в руке: {len(self.hand)}")

    def get_total_garrison_points(self):
        sum_of_points = len(self.garrison) * 1
        return sum_of_points
        


class GameEngine:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.neutral_deck = []
        self.table = []
        self.deck = Deck()
        # self.deck.generate_deck()



    def deal_cards_to_player(self, player):# for each player in first round
        player.get_cards_in_hand(self.deck)
        return player.hand


    def choose_card(self):
        
        chosen_card_player_1 = None
        chosen_card_player_2 = None

        if self.player_1.attack_status == True and self.player_2.attack_status == False:
            print("--- Ход Атакующего (Игрок 1) ---")
            chosen_card_player_1 = self.player_1.choose_card_for_fight()
            self.hiding_enter()
            self.table.append(chosen_card_player_1)
            print("\n--- Ход Защищающегося (Игрок 2) ---")
            chosen_card_player_2 = self.player_2.choose_card_for_fight()
            self.hiding_enter()
            self.table.append(chosen_card_player_2)
        
        elif self.player_2.attack_status == True and self.player_1.attack_status == False:
            print("--- Ход Атакующего (Игрок 2) ---")
            chosen_card_player_2 = self.player_2.choose_card_for_fight()
            self.hiding_enter()
            self.table.append(chosen_card_player_2)
            print("\n--- Ход Защищающегося (Игрок 1) ---")
            chosen_card_player_1 = self.player_1.choose_card_for_fight()
            self.hiding_enter()
            self.table.append(chosen_card_player_1)


        # self.clear_table() # не нужна здесь так как еще не разыгран раунд
        return chosen_card_player_1, chosen_card_player_2
    
    
    
    # function of clearing table after each round
    def clear_table(self):
        self.table.clear()
        return self.table





    def choose_winner_of_round(self, card1, card2):


        if card1.tier == 3 and (card2.tier == 4 or card2.tier == 5):
            
            self.player_1.garrison.extend((card1, card2))
            self.player_1.attack_status = True
            self.player_2.attack_status = False
            self.clear_table()
            return self.player_1
        
        
        elif card2.tier == 3 and (card1.tier == 4 or card1.tier == 5):
            self.player_2.garrison.extend((card1, card2))
            self.player_2.attack_status = True
            self.player_1.attack_status = False
            self.clear_table()
            return self.player_2


        elif card1.attack < card2.attack:
            self.player_2.garrison.extend((card1, card2))
            self.player_2.attack_status = True
            self.player_1.attack_status = False
            self.clear_table()
            return self.player_2


        elif card1.attack > card2.attack:
            self.player_1.garrison.extend((card1, card2))
            self.player_1.attack_status = True
            self.player_2.attack_status = False
            self.clear_table()
            return self.player_1

        
        
        
        else:
            self.neutral_deck.extend((card1, card2))
            
            print(f"Длина колоды сброса: {len(self.neutral_deck)}")




            if self.player_1.attack_status:
                self.player_1.attack_status = False
                self.player_2.attack_status = True
                self.clear_table()
                return None
            else:
                self.player_1.attack_status = True
                self.player_2.attack_status = False
                self.clear_table()
                return None


    # refiel hands
    def supply_phase(self):
        if len(self.deck.cards) >= 2:
            self.player_1.hand.append(self.deck.cards.pop(0))
            self.player_2.hand.append(self.deck.cards.pop(0))

        elif len(self.deck.cards) == 1:
            if self.player_1.attack_status:
                self.player_1.hand.append(self.deck.cards.pop(0))
            else:
                self.player_2.hand.append(self.deck.cards.pop(0))

    
    # A function for hiding entered values
    def hiding_enter(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        return



    
    def start_game(self):
        #deal cards to players first deal 8 cards to each player
        self.deck.generate_deck()
        self.deal_cards_to_player(self.player_1)
        self.deal_cards_to_player(self.player_2)

        
        print(f"Длина колоды: {len(self.deck.cards)}")
        print(f"Количество карт в руке у Игрока 1: {len(self.player_1.hand)}")
        print(f"Количество карт в руке у Игрока 2: {len(self.player_2.hand)}")


        # choice first attack player randomly
        first_attacker = choice([self.player_1, self.player_2])
        first_attacker.attack_status = True

        if first_attacker == self.player_1:
            print("Жребий брошен! Первым атакующим игроком выбран случайным образом Игрок 1")
            self.player_2.attack_status = False
        else:
            print("Жребий брошен! Первым атакующим игроком выбран случайным образом Игрок 2")
            self.player_1.attack_status = False

        
        round_num = 1

        # game loop
        while True:
            # check if game is over
            if len(self.deck.cards) == 0 and (len(self.player_1.hand) == 0 and len(self.player_2.hand) == 0):
                print("\n🛑 Матч окончен! Все ресурсы истощены.")
                if len(self.player_1.garrison) > len(self.player_2.garrison):
                    print("Игрок 1 победил!")
                    break
                elif len(self.player_1.garrison) < len(self.player_2.garrison):
                    print("Игрок 2 победил!")
                    break
                else:
                    print("Ничья")
                    break


            print(f"\n--- РАУНД {round_num} ---")
            # +1 cards
            self.supply_phase()

            
            p1_card, p2_card = self.choose_card()
            print(f"Количество карт на столе: {len(self.table)}")

            print("\n♠️♣️ ВСКРЫТИЕ КАРТ ♥️♦️")
            print(f"Игрок 1 выбрал: {p1_card}")
            print(f"Игрок 2 выбрал: {p2_card}")
            input("\nНажмите Enter, чтобы рассчитать победителя раунда...")

            # pick winner of round 
            next_attacker = self.choose_winner_of_round(p1_card, p2_card)
            print(f"Количество карт на столе: {len(self.table)}")

            if next_attacker == self.player_1:
                print("\n🎉Победитель раунда Игрок 1! 🎉")
            
            
            elif next_attacker == self.player_2:
                print(f"\n🎉Победитель раунда Игрок 2! 🎉")

            elif not next_attacker:
                print("\n🤝 Ничья! Обе карты отправляются в колоду сброса карт")


            
            round_num += 1
            
            print(f"Игрок 1: {len(self.player_1.garrison)} очков, Игрок 2: {len(self.player_2.garrison)} очков")
            print(f"Количество карт в колоде: {len(self.deck.cards)}")
            input("Нажмите Enter, чтобы продолжить...")





def main():
    p1 = Player()
    p2 = Player()

    game = GameEngine(p1, p2)
    game.start_game()










    # print("--- ШаГ 0: Создание игроков ---")
    # p1 = Player()
    # p2 = Player()
    # print("--- Игроки созданы ---\n")
    
    # # init game engine
    # game_engine = GameEngine(p1, p2)
    # test_deck = game_engine.deck

    # print("--- ШАГ 1 Инициалзация игры ---")
    # print(f"В колоде создано карт {len(test_deck.cards)}")




    # print(f"Карт в руке у игрока 1 до раздачи: {len(p1.hand)}")
    # print(f"Карт в руке у игрока 2 до раздачи: {len(p2.hand)}")




    # print("\n--- ШАГ 2: Раздача карт ---")
    
    # print("-> Карты разданы Игроку 1")
    # hand_player_1 = game_engine.deal_cards_to_player(p1)
    # print(f"Карт в руке у игрока 1 после раздачи: {len(hand_player_1)} (должно быть 8)")
    # print(f"В колоде стало карт {len(test_deck.cards)} (должно быть 44)")


    # print("\n-> Карты разданы Игроку 2")
    # hand_player_2 = game_engine.deal_cards_to_player(p2)
    # print(f"В руке у игрока 2 после раздачи: {len(hand_player_2)} (должно быть 8)")
    # print(f"В колоде стало карт {len(test_deck.cards)} (должно быть 36)")


    # print("\n--- ШАГ 3: Проверка уникальности карт ---")
    # print(f"Карты в руке у игрока 1: {p1.hand}")
    # print(f"Карты в руке у игрока 2: {p2.hand}")


    # print("\n--- ШАГ 4: Старт игры ---")
    # table, chosen_card_player_1, chosen_card_player_2 = game_engine.choose_card()


    # print(f"\n--- ШАГ 5: Выбор карт игроками ---")
    # print(f"Игрок 1 выбрал карту: {chosen_card_player_1}")
    # print(f"Игрок 2 выбрал карту: {chosen_card_player_2}")

    # print(f"Количество карт на руке игрока 1 после выбора 1ой карты: {len(p1.hand)}")
    # print(f"Количество карт на руке игрока 2 после выбора 1ой карты: {len(p2.hand)}")



    # print("\n--- ШАГ 6: Проверка количества карт ---")
    # print(f"Всего карт в игре: {len(p1.hand) + len(p2.hand) + len(test_deck.cards) + len(table)}")



























if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Программа закрывается через 2 секунды...")
        sleep(2) 