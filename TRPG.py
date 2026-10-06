import random
import time


#-----------------------------------------------------------------
# initial selection for difficulty/class option and name
# then i ask the user if he want to proceed or change the options
#-----------------------------------------------------------------

# i create a function to determine the difficulty option for the game
def difficulty_selection():
    while True:

        difficulty = input("Choose a difficulty level (Easy, Medium, Hard): ").strip().capitalize() # strip extra whitespaces and ensure proper capitalization (e.g., " archer " -> "Archer")
        if difficulty not in ["Easy", "Medium", "Hard"]:                                            # i check that the user has entered valid input.
            print("Please choose a valid difficulty level.")                                        # if not i ask again
            continue                                                                                # and i repeat the while
        return difficulty

# i create a function to determine the class of the hero for the game
def class_selection():
    while True:
        classe = input("Choose a class (Archer, Paladin, Mage): ").strip().capitalize()
        if classe not in ["Archer", "Paladin", "Mage"]:
            print("Please choose one of the available classes.")
            continue
        return classe

# i create a function to ask the name of the hero of the user
def name_selection():
    while True:
        name = input("Choose a name for your character: ").strip().capitalize()
        if not name:
            print("The name cannot be empty!")
            continue
        return name

# i create a function to ask the user if they are sure about teh chosen options
def are_you_sure(difficulty, classe, name):
    while True:
        print("\n" + "-" * 35)
        print("CHARACTER RECAP")
        print("-" * 35)
        print(f"Name: {name} | Class: {classe} | Difficulty: {difficulty}")
        print("-" * 35)
        sure = input("Would you like to continue with this setup? (Y/N): ").strip().capitalize()

        if sure == "Y":
            break
        elif sure == "N":
            change = input("What do you wish to change? (D=Difficulty, C=Class, N=Name): ").strip().capitalize()
            if change == "D":
                difficulty = difficulty_selection()
            elif change == "C":
                classe = class_selection()
            elif change == "N":
                name = name_selection()
            else:
                print("Invalid option!")
        else:
            print("Please answer Y or N.")

    return difficulty, classe, name         # i return the new difficulty, class, and name value


#-----------------------------------------------------------------
# i define the specifications for each class within a dictionary
# so that I can access each aspect individually.
# i also creat a function for a summary sheet of the hero
#-----------------------------------------------------------------

# dictionary of every class
def crea_eroe(nome, classe):
    if classe == "Archer":
        return {
            "name": nome,
            "class": classe,
            "hp": 75,                       # current hp
            "hp_max": 75,                   # max hp possible
            "attack": 35,                   # default attack power
            "defense": 15,                  # default defense
            "gold": 125,                    # starting gold
            "weapon": "Wood Longbow",
            "armor": "Leather Coat",
            "inventory": ["Health Potion"]  # for the inventory i create a list[] and i give each class a starting potion
        }
    elif classe == "Paladin":
        return {
            "name": nome,
            "class": classe,
            "hp": 100,
            "hp_max": 100,
            "attack": 25,
            "defense": 25,
            "gold": 100,
            "weapon": "Iron Sword",
            "armor": "Chainmail",
            "inventory": ["Health Potion"]
        }
    elif classe == "Mage":
        return {
            "name": nome,
            "class": classe,
            "hp": 60,
            "hp_max": 60,
            "attack": 50,
            "defense": 10,
            "gold": 150,
            "weapon": "Novice Staff",
            "armor": "Cloth Robe",
            "inventory": ["Health Potion"]
        }

# summary sheet of the hero
def mostra_stato(hero):
    print("\n" + "=" * 35)
    print(f"HERO SHEET: {hero['name']} ({hero['class']})")
    print("=" * 35)
    print(f"HP: {hero['hp']}/{hero['hp_max']}")
    print(f"Attack: {hero['attack']}")
    print(f"Defense: {hero['defense']}")
    print(f"Gold: {hero['gold']}")
    print(f"Weapon: {hero['weapon']}")
    print(f"Armor: {hero['armor']}")
    print(f"Inventory: {', '.join(hero['inventory']) if hero['inventory'] else 'Empty'}")
    print("=" * 35 + "\n")

#-----------------------------------------------------------------
# i creates an interactive shop featuring common items available to all
# classes, alongside specific items for the player's chosen class.
#-----------------------------------------------------------------

# catalog of common and class-specific items available in the shop,
# structured as a nested dictionary.
CATALOG = {
    "Common": {
        "Health Potion": {"price": 30, "type": "potion", "heal": 40},
        "Greater Potion": {"price": 60, "type": "potion", "heal": 80}
    },
    "Archer": {
        "Reinforced Bow": {"price": 80, "type": "weapon", "bonus_attack": 15},
        "Elven Bow": {"price": 150, "type": "weapon", "bonus_attack": 30},
        "Studded Leather Armor": {"price": 70, "type": "armor", "bonus_defense": 10}
    },
    "Paladin": {
        "Steel Sword": {"price": 80, "type": "weapon", "bonus_attack": 12},
        "Warhammer": {"price": 140, "type": "weapon", "bonus_attack": 25},
        "Plate Armor": {"price": 90, "type": "armor", "bonus_defense": 20}
    },
    "Mage": {
        "Crystal Staff": {"price": 90, "type": "weapon", "bonus_attack": 20},
        "Runic Staff": {"price": 160, "type": "weapon", "bonus_attack": 40},
        "Arcane Robe": {"price": 65, "type": "armor", "bonus_defense": 12}
    }
}


def shop(hero):
    while True:
        print("\n" + "-" * 35)
        print(f"WELCOME TO THE SHOP (Gold available: {hero['gold']})")
        print("-" * 35)
        # temporary dictionary to pair menu index numbers with item details
        available_items = {}
        idx = 1
        # unpack each item name and its properties (price, stats) from the "Common" catalog
        for item_name, info in CATALOG["Common"].items():
            available_items[idx] = (item_name, info)
            print(f"{idx}. {item_name} - {info['price']} Gold (Heal: +{info['heal']} HP)")
            idx += 1

        # loop through each class-specific item for the player's chosen class
        hero_class = hero["class"]
        for item_name, info in CATALOG[hero_class].items():
                available_items[idx] = (item_name, info)
                if info["type"] == "weapon":
                    print(f"{idx}. [Weapon] {item_name} - {info['price']} Gold (+{info['bonus_attack']} ATK)")
                else:
                    print(f"{idx}. [Armor] {item_name} - {info['price']} Gold (+{info['bonus_defense']} DEF)")
                idx += 1
        # add the option to leave the shop
        print(f"{idx}. Exit Shop")

        # read the user input and clean leading/trailing whitespaces
        choice = input("\nSelect an item to buy: ").strip()

        # input validation: ensure the user entered digits only
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        # check if the user selected 'Exit Shop'
        if choice == idx:
            print("Thank you for visiting!")
            break

        # process the purchase if a valid item index was selected
        elif choice in available_items:
            item_name, info = available_items[choice]

            # verify if the hero has sufficient funds
            if hero["gold"] >= info["price"]:
                hero["gold"] -= info["price"]

                # apply purchase logic based on item category
                if info["type"] == "potion":
                    hero["inventory"].append(item_name)
                    print(f"\nYou bought a {item_name}!")
                elif info["type"] == "weapon":
                    hero["weapon"] = item_name
                    hero["attack"] += info["bonus_attack"]
                    print(f"\nYou equipped {item_name}! Your attack increases to {hero['attack']}.")
                elif info["type"] == "armor":
                    hero["armor"] = item_name
                    hero["defense"] += info["bonus_defense"]
                    print(f"\nYou equipped {item_name}! Your defense increases to {hero['defense']}.")
            else:
                print("\nYou don't have enough gold!")
        else:
            print("Invalid choice!")


#-----------------------------------------------------------------
# monsters dictionary, combat management and potion usage
#-----------------------------------------------------------------

# monsters dictionary
def generate_monster(difficulty_multiplier):
    monster_types = [
        {"name": "Goblin", "hp": 40, "attack": 17, "defense": 6, "gold": 20},
        {"name": "Skeleton", "hp": 55, "attack": 20, "defense": 10, "gold": 25},
        {"name": "Orc", "hp": 80, "attack": 28, "defense": 15, "gold": 40},
        {"name": "Drake", "hp": 100, "attack": 36, "defense": 18, "gold": 70}
    ]
    # i extract at random one of the monsters for combat
    base = random.choice(monster_types)
    return {
        "name": base["name"],
        "hp": int(base["hp"] * difficulty_multiplier),              # scaling the attributes with the specific difficulty multiplier
        "hp_max": int(base["hp"] * difficulty_multiplier),
        "attack": int(base["attack"] * difficulty_multiplier),
        "defense": base["defense"],
        "gold": int(base["gold"] * difficulty_multiplier)
    }

# potion usage
def use_potion(hero):
    # create an empty list to collect the potions found.
    potions = []
    # check every item in the hero's inventory.
    for item in hero["inventory"]:
        if "Potion" in item:
            potions.append(item)
    # if the list of potions is empty, we notify the player.
    if not potions:
        print("\nYou have no potions in your inventory!")
        return False
    # take the first potion found in the inventory.
    selected_potion = potions[0]
    # determine the healing amount based on the name.
    if selected_potion == "Health Potion":
        heal = 40
    else:
        heal = 80
    # apply the heal without exceeding maximum HP.
    hero["hp"] = min(hero["hp_max"], hero["hp"] + heal)

    hero["inventory"].remove(selected_potion)
    print(f"\nYou used a {selected_potion}! Recovered {heal} HP. (Current HP: {hero['hp']}/{hero['hp_max']})")
    return True

# combat management
def combat(hero, multiplier):
    monster = generate_monster(multiplier)
    print("\n" + "-" * 35)
    print(f"A MONSTER APPEARS! A {monster['name']} blocks your path!")
    print("-" * 35)

    # combat goes on till the monster or the hero is dead
    while hero["hp"] > 0 and monster["hp"] > 0:
        print(
            f"\n--- {hero['name']} (HP: {hero['hp']}/{hero['hp_max']}) vs {monster['name']} (HP: {monster['hp']}/{monster['hp_max']}) ---")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Attempt Escape")

        choice = input("What do you want to do? ").strip()

        if choice == "1":
            # hero's Turn
            raw_damage = hero["attack"] + random.randint(-5, 5)  # simulation of dice combat with high or low damage roll
            damage = max(5, raw_damage - monster["defense"])        # deliver the accurate damage taking into account the defense attribute
            monster["hp"] -= damage
            print(f"\nYou attack the {monster['name']} dealing {damage} damage!")

        elif choice == "2":
            if not use_potion(hero):
                continue

        elif choice == "3":
            if random.random() < 0.4:
                print("\nYou managed to escape successfully!")
                return True
            else:
                print("\nEscape attempt failed!")
        else:
            print("Invalid action!")
            continue

        # monster Turn (if still alive)
        if monster["hp"] > 0:
            time.sleep(1)
            raw_monster_damage = monster["attack"] + random.randint(-3, 3)
            monster_damage = max(3, raw_monster_damage - hero["defense"])
            hero["hp"] -= monster_damage
            print(f"The {monster['name']} attacks you dealing {monster_damage} damage!")

    if hero["hp"] > 0:
        print(f"\nYou defeated the {monster['name']}! You earned {monster['gold']} gold!")
        hero["gold"] += monster["gold"]
        return True
    else:
        print("\nYou were defeated in battle... GAME OVER.")
        return False


#-----------------------------------------------------------------
# main
#-----------------------------------------------------------------

def main():
    print("Welcome TRPG, a small text based Rpg!")

    difficulty = difficulty_selection()
    classe = class_selection()
    name = name_selection()

    difficulty, classe, name = are_you_sure(difficulty, classe, name)

    # Encounter configuration and difficulty multiplier
    if difficulty == "Easy":
        total_encounters = 5
        multiplier = 0.8
    elif difficulty == "Medium":
        total_encounters = 10
        multiplier = 1.0
    else:
        total_encounters = 15
        multiplier = 1.25

    hero = crea_eroe(name, classe)
    completed_encounters = 0

    print(f"\nYour journey begins! You must survive {total_encounters} encounters to win.")

    while completed_encounters < total_encounters and hero["hp"] > 0:
        print(f"\nQuest Progress: Encounter {completed_encounters + 1} of {total_encounters}")
        print("1. Proceed to next encounter")
        print("2. Visit the Shop")
        print("3. Display Hero Sheet")
        print("4. Abandon Quest")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            victory = combat(hero, multiplier)
            if victory:
                completed_encounters += 1
            else:
                break
        elif choice == "2":
            shop(hero)
        elif choice == "3":
            mostra_stato(hero)
        elif choice == "4":
            print("\nYou abandoned the quest. Goodbye!")
            break
        else:
            print("Invalid option.")

    if hero["hp"] > 0 and completed_encounters == total_encounters:
        print("\nCONGRATULATIONS! You cleared all encounters and completed the Quest!")

    print("Press enter to exit...")


if __name__ == "__main__":
    main()