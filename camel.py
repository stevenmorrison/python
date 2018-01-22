import random

print("Welcome to Grand Theft Camel!")
print("by: Steven D Morrison")
print("")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.")
print("\n")

 
done = False
if done == True:
    print("you traveled", dist_trav, "across the dessert sands")
    if dist_trav < 200 and dist_natives < 0:
        raise SystemExit("Better Luck Next Time")
    else:
        raise SystemExit("Thank you for playing!!")
                
dist_trav = 0
dist_natives = -20
canteen_level = 5
camel_tired = 0
thirst = 0
                
while done == False:
    if not done and thirst > 4 and thirst < 6:
        print("You are getting thirsty")
    if not done and thirst >= 6:
        print("You have DIED!! of thirst!!!")
        done = True
        
    if not done and camel_tired >= 5 and camel_tired < 8:
        if not done:
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
            
    if not done:
        
        print('''
        0. Quit.
        1. Drink from your canteen.
        2. Ahead moderate speed.
        3. Ahead full speed.
        4. Stop for the night.
        5. Status check.\n
        ''')
                                    
        choice = int(input("Your choice: "))
     
        if choice == 0:
            done = True
                                    
        if choice == 5:
            print("Miles Traveled: ", dist_trav)
            print("Drinks left in Canteen: ", canteen_level)
            print("The natives are ", dist_natives, " miles behind you")
                                    
        if choice == 4:
            camel_tired = 0
            print("you find a secluded place to stop for the night")
            print("The Camel is Happy and Well Rested")
            dist_natives = dist_natives + random.randint(10, 15)
            
        if choice == 3:
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

        if choice == 2:
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
        
        if choice == 1:
            if canteen_level > 0:
                if thirst == 0:
                    print("You weren't that thirsty")
                    print("but i suppose the middle of a dessert\nis a fine place to indulge in fineries")
                if thirst > 0:
                    print("Your thirst is quenched")
                    thirst = 0
                canteen_level -= 1
            else:
                print("Your Canteen is Empty")
                    