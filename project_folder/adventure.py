import random

inventory = ["Dagger"]

playerHealth = 20
lakeHealth = 30
dragonHealth = 50
def lakeAttack ():
    global playerHealth
    damage = random.randint(0,5)
    playerHealth -= damage
    return damage

def dragonAttack ():
    global playerHealth
    damage = random.randint(0,10)
    playerHealth -= damage
    return damage

def daggerAttack ():
    global lakeHealth, dragonHealth
    damage = random.randint(0,5)
    lakeHealth -= damage
    dragonHealth -= damage
    return damage

def tridentAttack ():
    global lakeHealth, dragonHealth
    damage = random.randint(0,10)
    lakeHealth -= damage
    dragonHealth -= damage
    return damage

def swordAttack ():
    global lakeHealth, dragonHealth
    damage = random.randint(0,20)
    lakeHealth -= damage
    dragonHealth -= damage
    return damage

def addToInventory(weapon):
    inventory.append(weapon)

name = input("Greetings, traveler. Welcome to your journey. Let's start by asking your name. What is your name? ")

print()

gameStart = input("It's nice to meet you " + name + ". In this adventure, you will be lost in the woods, looking for a way out. There are several dangerous paths you will find along the way. Are you willing to partake in this journey? (yes/no) ")
print()
if gameStart == "yes":
    print("Great! Let's begin. You open your eyes and find yourself leaned up against the trunk of a tree. The only items in your possession are the clothes on your body and a dagger in your pocket. As you look at your surroundings, you notice there is a path.")
    choice01 = input("Will you follow the path? (yes/no) ")

    print()
    
    if choice01 == "yes":
        print("You stand and approach the dirt path. As you follow the path, you can see that it diverges in two different directions.")
        choice02 = input("On the left, you see that the forest is thicker and all seems grim. Very little light is showing through the trees. You aren't even sure you will make it through without a flashlight. To the right, the density of the forest doesn't seem to change. It appears safer, and you think you hear civilization ahead. Which way do you go? (left/right) ")
        
        print()

        if choice02 == "left":
            print("You gaze down the left path with uncertainty. You take a breath to ready yourself before continuing ahead.")
            print("As you continue to walk, the dirt road winds around, going in all kinds of directions until it feels that you are more lost than before. You finally stumble upon some signage that might give some clue as to where you have found yourself. Unfortunately, the signs are all warnings for monsters that lurk ahead. The one mentioned most is a mysterious lake creature that is known to take the lives of innocent travelers.")
            choice03 = input("Do you proceed? (yes/no) ")
            print()

            if choice03 == "yes":
                print("You're braver than you seem. The threat of lake monsters doesn't dampen your determination. You trek along, watching for potential dangers. As you near the lake, you notice a light glimmering off the path.")
                choice04 = input("Do you risk investigating the mysterious light? (yes/no) ")
                print()
                if choice04 == "yes":
                    print("You follow the light, throwing aside all caution. As you creep closer, you recognize the object that is emitting the light to be a trident that looks as if it had been abandoned long ago.")
                    choice05 = input("Do you take the trident? (yes/no) ")
                    print()
                    if choice05 == "yes":
                        print("You add the trident to your inventory.")
                        addToInventory("Trident")

                    elif choice05 == "no":
                        print("You do not gain any new inventory.")
                    
                    print("After investigating the light off the path, you return to your original path.")

                elif choice04 == "no":
                    print("You decide not to investigate the light and continue on the original path.")

                print("Eventually, the dirt path becomes sand and stone. A large lake is at the end of the path. Everything seemed a bit too quiet.")
                choice06 = input("Do you proceed? (yes/no) ")
                if choice06 == "yes":
                    print("You approach the lake cautiously. You bend down, inspecting the water that was too blue. Curiously, you reach a hand out, touching the water. It seemed to be a normal lake. Your gaze lifts and suddenly from the middle of the lake, you see a giant serpant-like creature looming over you.")

                    while playerHealth > 0 and lakeHealth > 0:

                        battle_choice = input(f"The lake monster approaches you. Choose your weapon: {', '.join(inventory)}? ")

                        if "Trident" in inventory and battle_choice.lower() == "trident":
                            tridentAttack()
                            print(f"You attack the lake monster with the Trident, dealing damage! Lake health is now {lakeHealth}.")
                            print()
                        elif battle_choice.lower() == "dagger":
                            daggerAttack()
                            print(f"You attack the lake monster with the Dagger, dealing damage! Lake health is now {lakeHealth}.")
                            print()
                        else:
                            print("Invalid choice. You fumble in your attempt to attack.")
                        
                        lakeAttack()
                        print(f"The lake monster counter-attacks! You take damage. Player health is now {playerHealth}.")
                        print()

                        if playerHealth <= 0:
                            print("You Died.")
                        if lakeHealth <= 0:
                            print("The lake serpant recoils to the final blow before ultimately collapsing in defeat. You look upon the corpse, victorious. As the water settles, you notice small creatures emerging from the water. You watch them approach you curiously until you recognize them as water nymphs. Realization washes over you that you've just killed their leader, making you now the leader of the water nymphs. Before you can even protest, the nymphs grab you by the ankles and drag you to the depths of the lake. Looks like you don't get to return home.")
        

# ...

                elif choice06 == "no":
                    print("You decide to turn back. There may be another way home. Good luck, travler.")
                    ##end
            elif choice03 == "no":
                print("Perhaps another time, traveler. Good luck finding your way home.")

        elif choice02 == "right":
            print("You decide to take the right path. As you walk, you feel a sense of safety and hear distant sounds of what could be civilization.")
            choice07 = input("Do you proceed? (yes/no) ")
            print()
            if choice07 == "yes":
                print("As you follow the path, the sound of chatter and footsteps can be heard. Eventually, you happen upon a village.")
                choice08 = input("Will you go to the village? (yes/no) ")
                if choice08 == "yes":
                    print("You enter the village. A few of the village folk greet you, welcoming you to their home. Around you are shops, an inn, and a people bustliing about.")
                    choice09 = input("Would you like start a conversation with anyone? (yes/no) ")
                    if choice09 == "yes":
                        print("You approach one of the town's folk and strike up a conversation. The woman turns to you and smiles. 'Oh, hello! You must be new here.' You nod your head. 'What's your name?' You give her your name. 'It's nice to meet you " + name +". My name is Miriam. I'm one of the shopkeepers. Are you here for the quest?' Your head tilts to the side, inquisitive. 'You haven't heard?' You shake your head. 'Oh! Most travelers who come through are looking for the lost princess. A dragon took her a few weeks back. The king is devastated and offering a very big reward for anyone who can slay the dragon.' Reward? You like the sound of that.")
                        choice10 = input("Would you like to partake in this quest? (yes/no) ")
                        if choice10 == "yes":
                            print("'Great! Take this. It will help you on your journey.' You are handed a sword. 'The dragon lives in the cave at the top of the mountain. There is where the princess is most likely hidden.' ")
                            addToInventory("Sword")
                            print("Now that you are equipped with your new sword and have a new quest, it's time that you head to the mountain to find the dragon. You follow the path all the way up the mountain until you finally reach a cave. You slowly draw your sword, looking from side to side. You then spot the dragon that is larger than life. Its colossal eye opens now that the beast has sensed you.")
                            
                            while playerHealth > 0 and dragonHealth > 0:

                                battle_choice = input(f"The dragon approaches you. Choose your weapon: {', '.join(inventory)}? ")

                                if "Sword" in inventory and battle_choice.lower() == "sword":
                                    swordAttack()
                                    print(f"You attack the dragon with the sword, dealing damage! Dragon health is now {dragonHealth}.")
                                    print()
                                elif battle_choice.lower() == "dagger":
                                    daggerAttack()
                                    print(f"You attack the dragon with the dagger, dealing damage! Dragon health is now {dragonHealth}.")
                                    print()
                                else:
                                    print("Invalid choice. You fumble in your attempt to attack.")
                                
                                dragonAttack()
                                print(f"The dragon counter-attacks! You take damage. Player health is now {playerHealth}.")
                                print()

                                if playerHealth <= 0:
                                    print("You Died.")
                                if dragonHealth <= 0:
                                    print("The dragon falls in defeat. You look upon its corpse, victorious. From further into the cave you here a voice. You go to investigate and discover a princess! She looks as if she's been locked away in the cave for a long time. She shows you the way back to her home. The kingdom thanks you and rewards you generously for saving their princess. They even help you return home! Welcome home, travler. Thanks for playing.")

                        elif choice10 == "no":
                            print("Miriam nods in understanding. 'It is a big undertaking. Good luck on your travels.'")

                    elif choice09 == "no":
                        print("You spend some time in town but ultimately decide it would be best to get going. You continue following the path, eventually following it up a mountain. At the end of the path, there is a large cave. Before you even get the chance to turn back, a large, angry dragon emerges from the cave.")

                        while playerHealth > 0 and dragonHealth > 0:

                            battle_choice = input(f"The dragon approaches you. Choose your weapon: {', '.join(inventory)}? ")

                            if "Sword" in inventory and battle_choice.lower() == "Sword":
                                swordAttack()
                                print(f"You attack the dragon with the sword, dealing damage! Dragon health is now {dragonHealth}.")
                                print()
                            elif battle_choice.lower() == "dagger":
                                daggerAttack()
                                print(f"You attack the dragon with the Dagger, dealing damage! Dragon health is now {dragonHealth}.")
                                print()
                            else:
                                print("Invalid choice. You fumble in your attempt to attack.")
                            
                            dragonAttack()
                            print(f"The dragon counter-attacks! You take damage. Player health is now {playerHealth}.")
                            print()

                            if playerHealth <= 0:
                                print("You Died.")
                            if dragonHealth <= 0:
                                print("The dragon falls in defeat. You look upon its corpse, victorious. From further into the cave you here a voice. You go to investigate and discover a princess! She looks as if she's been locked away in the cave for a long time. She shows you the way back to her home. The kingdom thanks you and rewards you generously for saving their princess. They even help you return home! Welcome home, travler. Thanks for playing. ")

                elif choice08 == "no":
                    print("You decide to continue down the path instead. You were never very social anyway.")
            
            elif choice07 =="no":
                print("Perhaps there is another way out. Good luck, travler.")

    elif choice01 == "no":
        print("Those who do not engage in adventure will not make it beyond this point. Thank you for your time, travler.")

elif gameStart == "no":
    print("That's okay. Safe travels.")

