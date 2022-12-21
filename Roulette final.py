from random import randint


class Roulette:
    def __init__(self):
        self.numlist = []
        print("Welcome to Roulette, place numbers and bets")
        while True:
            try:
                self.s1 = int(input("How many numbers would you like to bet on?\n"))
                if self.s1 > 36:
                    print("Less than 36 please")
                    continue
            except ValueError:
                print("Integers numbers only")
            else:
                break
        for x in range(0, self.s1):
            while True:
                try:
                    self.s2 = int(input("Pick a number from 0 to 36: "))
                    if self.s2 > 36:
                        print("Must be 36 or lower")
                        continue
                except ValueError:
                    print("Integers only")
                    continue
                else:
                    self.numlist.append(self.s2)
                    break
        print(f"Your numbers are {self.numlist}")

    def chips(self):
        self.stack = 100
        while True:
            try:
                self.bet = float(input(f"You have {self.stack}, what's your bet"))
                if self.bet > self.stack:
                    print("Not enough chips")
                    continue
                else:
                    pass
            except ValueError:
                print("Invalid bet, try again")
                continue
            else:
                self.stack = self.stack - self.bet
                break

    def spinr(self):
        self.spin = int(randint(0, 36))
        print(f"The roulette spins and lands on: {self.spin}")

    def win(self):
        if self.spin not in self.numlist:
            print("You lose")
            print(f"Your balance is: {self.stack}")
        else:
            print("You win")
            self.stack = self.stack + (1 / self.s1) * 36 * self.bet
            print(f"You have {self.stack} chips")


test = Roulette()
test.chips()
test.spinr()
test.win()


def play_again():
    new_game = input("Want to play again? y/n")
    while True:
        if new_game not in ["y", "n"]:
            print("Invalid input")
            new_game = input("Want to play again? y/n").lower()
            continue
        elif "y" in new_game:
            test = Roulette()
            test.chips()
            test.spinr()
            test.win()
            play_again()
            break
        else:
            print("Thanks for playing")
            break


play_again()
