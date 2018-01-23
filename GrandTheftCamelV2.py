#!/usr/bin/python3
# GrandTheftCamelV2.py by: Steven D Morrison
# this is a text based game that takes user input and outputs a random 
# response it is an updated version of camel.py
# the object of the game is to cross the desert without being killed or your 
# camel being killed.
import random

class title:
    def intro(self):
        print ('Grand Theft Camel')
        print ('\nWelcome to Grand Theft Camel!')
        print ('by: Steven D Morrison')
        print("\nYou have stolen a camel to make your way across the great Mobi desert.")
        print("The natives want their camel back and are chasing you down!")
        print("Survive your desert trek and out run the natives.")
        print("\nYour resources are limited so use them wisely")
        try:
            input("\nPress enter to continue")
        except SyntaxError:
            pass

class loops:

    def main_loop(self):
        dist_trav = 0
        dist_natives = -20
        canteen_level = 5
        camel_tired = 0
        thirst = 0
        done = False
        while done == False:
            print('''
            0. Quit.
            1. Drink from your canteen.
            2. Ahead moderate speed.
            3. Ahead full speed.
            4. Stop for the night.
            5. Status check.\n
            ''')
            user_input = int(input('\nChoose a number 0-5 and press Enter: '))
            if user_input == 0:
                raise SystemExit
            if user_input == 1:
                if canteen_level > 0:
                    canteen_level -= 1
                if thirst == 0:
                    print("You weren't thirsty")
                    print("but i suppose the middle of a dessert\nis a fine place to indulge in fineries")
                if thirst > 0:
                    print("Your thirst is quenched")
                    thirst = 0

                else:
                    print("Your Canteen is Empty")

            if user_input == 2:
                travel = random.randint(5, 12)
                print("you have traveled", travel, "miles")
                dist_trav = dist_trav + travel
                thirst = thirst + 1
                camel_tired += 1
                dist_natives = (dist_natives + random.randint(7, 14)) - travel
                if dist_trav >= 50:
                    oasis = random.randint(1, 100)
                    if oasis > 85 and oasis <= 100:
                        print("You stubled upon an oasis in the sands\nyour camel is well rested and your canteen is full")
                        print("your thirst is also quenched")
                        thirst = 0
                        camel_tired = 0
                        canteen_level = 5

            if user_input == 3:
                travel = random.randint(10, 20)
                print("you have traveled", travel, "miles")
                dist_trav = dist_trav + travel
                thirst = thirst + 1
                camel_tired += random.randint(1, 3)
                dist_natives = (dist_natives + random.randint(7, 14)) - travel
                if dist_trav >= 50:
                    oasis = random.randint(1, 100)
                    if oasis > 85 and oasis <= 100:
                        print("You stubled upon an oasis in the sands\nyour camel is well rested and your canteen is full")
                        print("your thirst is also quenched")
                        thirst = 0
                        camel_tired = 0
                        canteen_level = 5


            if user_input == 4:
                camel_tired = 0
                print("you find a secluded place to stop for the night")
                print("The Camel is Happy and Well Rested")
                dist_natives = dist_natives + random.randint(10, 15)

            if user_input == 5:
                print("Miles Traveled: ", dist_trav)
                print("Drinks left in Canteen: ", canteen_level)
                print("The natives are ", dist_natives, " miles behind you")

        #while done == False:
            if not done and thirst > 4 and thirst < 6:
                print("You are getting thirsty")
            if not done and thirst >= 6:
                print("You have DIED!! of thirst!!!")
                done = True

            if not done and camel_tired >= 5 and camel_tired < 8:
                print("your camel is getting tired")
            if not done and camel_tired >= 8:
                print("Your Camel has DIED!!! GAME OVER")
                done = True

            if not done and dist_natives >= -15:
                print("“The natives are getting close!”")
            if not done and dist_natives >= 0:
                print("The Natives have Caught and Beheaded you!! Game Over!!")
                done = True

            if not done and dist_trav >= 200:
                print("You made it across the desert! You won!")
                done = True

        if done == True: #Game over Logic
            print("\nYou traveled", dist_trav, "miles across the dessert sands")
            if dist_trav < 200:
                print("Better Luck Next Time")
                knewGame = str(input("play again?: type y for yes or n to quit "))

                if knewGame == 'y' or 'Y' or 'yes' or 'Yes' or 'YES':
                    return main()
                else:
                    raise SystemExit

















def main():



    new_camel = title()
    new_camel.intro()



    loopy = loops()
    loopy.main_loop()










if __name__ == "__main__": main()
