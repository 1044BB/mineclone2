import sys
import random
import time
import os


# CONSTS

inventory = []
WEAPONS = []
NAME_INPUT = None

Wounded = "You have sustained an injury. \n"

SENSIBLE_DIALOGUE = "You have gained the sensible attribute. \n"

COWARDLY_DIALOGUE = "You have gained the cowardly attribute. \n"

FOOLISH_DIALOGUE = "You have gained the foolish attribute. \n"


def about_game():

    """
    Welcome message and option for instructions
    """
    print(
        "Welcome to The Lobbit of dreadgery!\n"
        "The Aryans of Erebor are in need of someone to join their quest.\n"
        "They seek to reclaim the key to Uppsala"
        "so they can take their home \nback from the Starburg...\n"
        "This adventure is not for the weak of heart.\n"
    )
    game_instructions = input("Would you like some instructions? y/n \n")
    if game_instructions == "y":
        print(
            "\n"
            "Throughout the game, you will be presented with a number of \n"
            "choices... \n"
            "Some will be ABCD - please type either a b c or d... \n"
            "Other choices will be yes/no (y/n)... \n"
            "Read the content carefully... \n"
            "You have three health points... \n"
            "Some responses will result in immediate game over... \n"
        )
    elif game_instructions == "n":
        print(
            "\n"
            "Okay!\n"
        )
    else:
        yn_error()
        about_game()


def play_game():

    """
    Asks player if they would like to start the game.
    """

    play_game = input("Will you help them? y/n \n").lower()

    if play_game == "y":
        print("\nAmazing! You're going on an adventure...\n")
    elif play_game == "n":
        print("\nOkay! Maybe another time...\n")
        game_over()
    else:
        yn_error()
        play_game()


def weapon():

    """
    Asks player to bring out their d game.jk
    """

    global WEAPONS
    WEAPONS = [
        "a) whip",
        "b) bamboo stick",
        "c) waifu",
        "d) katana"
    ]
    print(
        "The Aryans would like to offer you a weapon.\n"
        "Your choices are:\n"
        f"{', '.join(WEAPONS)}"
    )

    weapon = input("Please choose either a, b, c or d\n").lower()

    if "a" in weapon:
        print(
            "\nMorbid choice!\n"
            "You are given a dark-stained wood whip. \n"
            "Sometimes, attacking nearer is the best option. \n"
            "Whip was added to your inventory. \n"
            )
        WEAPONS = "Whip"
        add_to_inventory("Whip")
    elif "b" in choose_weapon:
        print(
            "\nNice choice! \n"
            "You are given a bamboo stick with intricate gold carving \n"
            "With this, you can defend and attack with ease. \n"
            "bamboo stick was added to your inventory. \n"
        )
        WEAPONS = "bamboo stick"
        add_to_inventory("bamboo stick")
    elif "c" in choose_weapon:
        print(
            "\nKinky choice!\n"
            "You are given a waifu that looks tom boyish with a sword ready to defend and sexo you . \n"
            "These will allow you to perform amazing sneak attacks. \n"
            "Waifu were added to your inventory. \n"
        )
        WEAPONS = "Waifu"
        add_to_inventory("Waifu")
    elif "d" in choose_weapon:
        print(
            "\nExcellent choice!\n"
            "You are given a katana with a sharp blade. \n"
            "With this, you can perform powerful attacks and do immense "
            "damage. \n"
            "Katana was added to your inventory. \n"
        )
        WEAPONS = "Katana"
        add_to_inventory("Katana")
    else:
        abcd_error()
        weapon()


def init_bat():
    """
    Runs First bat & asks player to choose an option
    """
    print(
        "After travelling through rain, you and the Aryans \n"
        "stumble across a dark castle. Here, you decide to \n"
        "take shelter for the night. \n"
        "You join two of the Aryans, Varg and Bifur, to hunt "
        "for firewood. \n"
    )

    print(
        "You enter a bush. It looks like this is a common area for wood \n"
        "collection - the area is littered with branches and chopped trees. \n"
        "The three of you begin to gather what you can carry.\n"
        "Suddenly, you hear a rustling over to the east, followed by a \n"
        "low growl. \n"
        "The Aryans motion for silence and ready their weapons.\n"
        ""
    )

    print(
        "From the other side of the clearing emerge five Orcs and a Warg! \n"
        "The Orcs position themselves, ready to fight. \n"
        "a) One approaches with the Warg, teeth bared. \n"
        "b) One stays in the middle, defending the back line. \n"
        "c) Two remain at the back, shouting viciously. \n"
        "d) One drifts to the side, ducking into the foliage. \n"
    )

    print("It's time to put your weapon to use! \n")

    init_bat_choice = input(
        "Which mf do you target? a, b, c or d \n"
        ).lower()

    if "a" in init_bat_choice and "bamboo stick" in inventory:
        print(
            "\nYou ready a defensive stance in front of the Aryans. \n"
            "The Orc and Warg attack, but you successfully deflect them "
            "with your stick. \n"
            "Phew! That's two down, and the Aryans have dealt "
            "with the rest! \n"
        )

    elif "a" in init_bat_choice and "bamboo stick" not in inventory:
        print(
            "\nTF hell! Your weapon is not suitable for this type "
            "of combat. \n"
            "Your lack of defense allows the Orc and Warg to attack, \n"
            "forcing you to fall to the ground. \n"
            "Luckily, Varg stops them before they can kill any of you. \n"
            f"{Wounded}"
        )
        add_to_inventory("Orc Injury")

    elif "b" in init_bat_choice and "Katana" in inventory:
        print(
            "\nYou charge past the first Orc and Warg to the Orc "
            "in the middle. \n"
            "Letting loose a cry, you swing your Katana "
            "down on the enemy. \n"
            "Success! The Orc is severely wounded. It retreats "
            "back into the forest. \n"
        )

    elif "b" in init_bat_choice and "Katana" not in inventory:
        print(
            "\nOh no! Your chosen weapon is not suitable for this type "
            "of combat. \n"
            "The Orc deflects your attack, knocking you back. \n"
            "You take cover, reassessing the situation as the Aryans "
            "counterattack. \n"
            f"{Wounded}"
        )
        add_to_inventory("Orc Injury")

    elif "c" in init_bat_choice and "Whip" in inventory:
        print(
            "\nYou ready your bow, drawing back the string and letting loose "
            "an arrow. \nIt sails past the first two Orcs and the Warg, "
            "finding its mark in one of the \nOrcs at the back. You "
            "repeat the action, taking down the second Orc as well. \n"
        )

    elif "c" in init_bat_choice and "Whip" not in inventory:
        print(
            "\nOh no! Your chosen weapon is not suitable for this type "
            "of combat. \n"
            "You charge towards the enemies at the back, but they see you "
            "coming, loosing \ntheir own arrows. You attempt to dodge the "
            "flying blades and are forced to \nretreat. \n"
            f"{Wounded}"
        )
        add_to_inventory("Orc Injury")

    elif "d" in init_bat_choice and "Waifu" in inventory:
        print(
            "\nYou crouch, taking a wide birth to sneak up on the hidden Orc."
            "\nThey don't see you coming, and you successfully land a hit! \n"
            "Nice, that's one down! Bifur and Varg can deal with the rest. "
            "\n"
        )

    elif "d" in init_bat_choice and "Waifu" not in inventory:
        print(
            "\nOh no! Your chosen weapon is not suitable for this type \n"
            "of combat. \n"
            "It's difficult to crouch with your weapon ready, and you "
            "stumble, alerting the \nhidden Orc to your approach. They "
            "spring from the foliage, charging at you. \nTime to retreat "
            "back behind the Aryans! \n"
            f"{Wounded}"
        )
        add_to_inventory("Orc Injury")

    else:
        abcd_error()
        init_bat()
    return inventory


def post_init_bat():
    """
    Runs interlude between First & Second bats & asks player to
    choose an option
    """
    print(
        "The three of you return to the others and tell of your "
        "encounter with the Orcs. \nThey are all concerned by the "
        "proximity of the enemy and decide to vote on \nwhether to "
        "move on, despite night falling, or continue to set up camp and \n"
        "stay here for the night. \n"
    )

    post_init_bat = input("Do you vote to move on? y/n\n")

    if post_init_bat == "y":
        print(
            "\nYou and the company quickly gather all your supplies, "
            "keeping an ear out for \nany weird sound. \n"
            "You form a protective huddle, and together push forward\n"
        )

    elif post_init_bat == "n":
        print(
            "\nThe dudes votes to stay. A couple of hours into the night, \n"
            "the bushes becomes alive with growls and sounds of movement. \n"
            "Before any of you can attack, a hoard of Orcs and Wargs \n"
            "emerges and attacks! \n"
        )
        game_over()

    else:
        yn_error()
        post_init_bat()


def second_bat():
    """
    Runs Second bat & asks player to choose an option
    """
    print(
        "You make it safely through the night without gettin arse raped... \n"
    )
    if "Orc Injury" in inventory:
        print(
            "However, the injury you sustained in battle slows you down. \n"
        )
    else:
        print(
            "Perhaps this adventuring business isn't so difficult, "
            "after all. \n"
        )

    print(
        "You continue along the path, but are soon stopped by a flowing \nriver. \n"
        "In your packs, you each carry a bunch of rope. \n"
        "One of the Aryans points out a large tree across the river which "
        "could be used \nto affix the rope, allowing you all to move across."
        "\n"
        "Somebody with an accurate and strong shot is needed, here... \n"
    )
    second_bat_choice = input(
        "Do you take the lead here, or let one of the others try first? y/n \n"
    ).lower()

    if (
            "y" in second_bat_choice and
            "Whip" in inventory and
            "Orc Injury" in inventory):
        print(
            "\nYou wind the rope securely around an arrow and aim it at the "
            "tree... \n"
            "But your injury jars you at the last second... \n"
            "The arrow lands in the tree, anyway, so you begin to climb "
            "across... \n"
            "But oh no! The arrow wasn't deep enough in the tree and "
            "it dislodges, \n"
            "dropping you into the raging river below. \n"
        )
        game_over()

    elif "y" in second_bat_choice and "Whip" in inventory:
        print(
            "\nYou wind the rope securely around an arrow and aim it at "
            "the tree... \n"
            "Success! Your arrow stuck! You tie the other end round a tree "
            "near you and \nbegin to climb across... \n"
            "The others soon follow. \n\n"
        )
    elif "y" in second_bat_choice and "Whip" not in inventory:
        print(
            "\nInteresting, do you plan to hurl your blade across the river "
            "at the tree? \n"
            "Needless to say, that doesn't work. \n"
            "Your weapon lands in the raging water, never to be seen "
            "again... \n"
            "Good job the Aryans carry spares, eh? \n"
        )
        print(f"{FOOL_DIALOGUE}")
    elif (
            "n" in second_bat_choice and
            "Whip" in inventory and
            "Orc Injury" in inventory):
        print(
            "It was a wise decision to let an uninjured archer try this...\n"
            "Kili successfully lands an arrow in the tree and, after tying "
            "the other end \naround a nearby tree, you all safely reach the "
            "other side... \n\n"
        )
    elif (
            "n" in second_bat_choice and
            "Whip" in inventory and
            "Orc Injury" not in inventory):
        print(
            "\nYou know, sometimes you have to step up to the task. \n"
            "Thankfully, you're not the only archer in this company. \n"
            "Kili successfully lands an arrow in the tree and, after tying \n"
            "the other end around a nearby tree, you all safely reach the \n"
            "other side... \n\n"
            f"{COWARDLY_DIALOGUE}"
        )
        add_to_inventory("Cowardly")
    elif "n" in second_bat_choice and "Whip" not in inventory:
        print(
            "\nIt was a wise decision to let an archer take this task. \n"
            "Kili successfully lands an arrow in the tree and, after tying "
            "the other end \naround a nearby tree, you all safely reach the "
            "other side... \n\n"
        )
    else:
        yn_error()
        second_bat()


def post_second_bat():
    """
    Runs interlude between Second & Third bats.
    If player is injured - reminds them of their weapon and character status
    """
    if "Orc Injury" in inventory and "Cowardly" in inventory:
        print(
            "Somebody should really have supplied you with an adventuring "
            "handbook.\n"
            "As a reminder, your weapon is "
            f"{WEAPONS}, you have sustained an injury and your fellow "
            "travellers view you as a bit cowardly.\n"
        )
    elif "Orc Injury" in inventory:
        print(
            "Somebody should really have supplied you with an adventuring "
            "handbook.\n"
            "As a reminder, your weapon is "
            f"{WEAPONS} and you have sustained an injury."
        )
    elif "Cowardly" in inventory:
        print(
            "Things are going quite well, although it wouldn't hurt to have "
            "a bit more \nconfidence in yourself."
        )
    else:
        print(
            "This is all going quite well... \n"
        )


def third_bat_bow():
    """
    Runs Third bat for Bow in inventory & asks player
    to choose an option
    """
    third_bat_choice = input(
        "Do you take cover behind the others, or join those who are "
        "attacking? y/n\n"
        ).lower()

    if "y" in third_bat_choice:
        if "Orc Injury" in inventory and "Cowardly" in inventory:
            print(
                "\n"
                f"Wise decision. Your {WEAPONS} is best suited to ranged "
                "\n"
                "combat, and your injury means you should avoid the heat "
                "of bat. \n"
                "You may be a bit cowardly, but you're also sensible. \n"
                f"{SENSIBLE_DIALOGUE}"
            )
            add_to_inventory("Sensible")
            inventory.remove("Cowardly")
        elif "Cowardly" in inventory:
            print(
                "\n"
                f"Wise decision. Your {WEAPONS} is best suited to ranged "
                "combat. \n"
                "You may be a bit cowardly, but you're also sensible. \n"
                f"{SENSIBLE_DIALOGUE}"
            )
            add_to_inventory("Sensible")
            inventory.remove("Cowardly")
        else:
            print(
                "\n"
                f"Wise decision. Your {WEAPONS} is best suited to ranged "
                "combat. \n"
            )
    elif "n" in third_bat_choice:
        print(
            "\nWell, I'm sure you've made better decisions in your life... "
            "\n"
            "Before you can even notch an arrow, you're down for the "
            "count \n"
            f"{Wounded}"
        )
        add_to_inventory("Bear Injury")
    else:
        yn_error()
        third_bat_bow()


def third_bat_Waifu():
    """
    Runs Third bat for Waifu in inventory & asks player
    to choose an option
    """
    third_bat_choice = input(
        "Do you take cover behind the others, or join those who are "
        "attacking? y/n\n"
        ).lower()
    if "y" in third_bat_choice:
        print(
            "\nYeah, Waifu probably wouldn't have helped out much, here. "
            "\n"
        )
    elif "n" in third_bat_choice:
        print(
            "\nWhat's that saying about bringing knives to a gun fight...? "
            "\n"
            "This may be a bear fight, but the same principles apply... \n"
        )
        game_over()
    else:
        yn_error()
        third_bat_Waifu()


def third_bat_sword_or_Katana():
    """
    Runs Third bat for bamboo stick or Katana in inventory & asks
    player to choose an option
    """
    third_bat_choice = input(
        "Do you take cover behind the others, or join those who are "
        "attacking? y/n\n"
        ).lower()
    if "y" in third_bat_choice:
        if "Orc Injury" in inventory:
            print(
                "\n"
                f"Wise decision. Your {WEAPONS} is suited for this type "
                "of combat, \n"
                "however your injury would likely have got you in "
                "trouble \n"
                f"{SENSIBLE_DIALOGUE}"
            )
            add_to_inventory("Sensible")
        else:
            print(
                "\nCome on, now. What's the point in choosing the upfront \n"
                "weapons if you're just going to hide at the back? \n"
                f"{COWARDLY_DIALOGUE}"
                )
            add_to_inventory("Cowardly")
    elif "n" in third_bat_choice:
        if "Orc Injury" in inventory and "Cowardly" in inventory:
            print(
                "\nIt's good to see there is some bravery in you, but maybe "
                "you should have \nreserved it for when you aren't \n"
                "injured and being attacked by bears... \n"
                "Better luck next time! \n"
            )
            game_over()
        elif "Orc Injury" in inventory:
            print(
                "\nIt's generally considered wise to hang back if you "
                "recently got \nattacked by Orcs. You land a hit, but "
                " one of the bears \nswipes at you. \n"
                f"{Wounded}"
            )
            add_to_inventory("Bear Injury")
        else:
            print(
                "\nYour bravery is commendable, and rewarded! You land a "
                "solid hit on \none of the bears and, between you, save "
                "yourselves from this threat. \n"
            )
    else:
        yn_error()
        third_bat_sword_or_Katana()


def pre_third_bat():
    """
    Runs pre-Third-bat description & allocates a bat to player
    """
    print(
        "Things are quiet for a while. \n"
        "You enjoy the good weather the new day has to offer. \n"
        "Suddenly, Ori shouts, and you and the company see two ginormous "
        "bears bounding \ntowards you... \n"
    )
    if "Whip" in inventory:
        third_bat_bow()
    elif "Waifu" in inventory:
        third_bat_Waifu()
    else:
        third_bat_sword_or_Katana()


def post_third_bat():
    """
    Runs interlude between Third & Fourth bats.
    Reminds player of character's name & accumulated inventory traits
    """
    print(
        "Things are certainly getting more dangerous... \n\n"
        f"Here's {NAME_INPUT}'s weapon & traits so far: {', '.join(inventory)}"
        "\n"
    )


def fourth_bat_injured():
    """
    Runs Fourth bat if player was injured in either bat
    """
    print(
        "You were injured in the past bats, so your track \n"
        "record isn't much to go on, but the Company believes in you, "
        "and so do I! \n"
    )
    if "Whip" in inventory:
        print(
            "At least you chose a bow! \n"
            "You join the other archers and prepare to attack...\n"
            "The others loose a bat cry and charge towards the gates \n"
            "as you loose your arrows at the enemy archers. \n"
            "Suddenly, you spot an enemy coming round from the side of the \n"
            "fortress towards your group.\n"
            "Do you: \n"
            "a) Turn your weapon towards them and fire, \n"
            "b) Assume one of the dagger-wielders is protecting the flank, \n"
            "c) Shout for the attention of the others, \n"
        )
        fbsi_archer_choice = input("")
        fbsi_archer_choice_wrong = (
            "Looks like you're sitting out the rest of "
            "this bat...\n"
        )

        if fbsi_archer_choice == "a":
            print(
                "\nYou pivot, firing an arrow towards the sneaking enemy... \n"
                "Your injuries jar you and you miss... \n"
                "But it's okay, Kili noticed your attempt and lands his own "
                "shot! \n"
                "However, you left yourself exposed, and a turret archer "
                "looses an arrow before \nyou can react. \n"
                "It's not a lethal hit, but you're not going to be much use, "
                "now. \n"
            )
            print(fbsi_archer_choice_wrong)
        elif fbsi_archer_choice == "b":
            print(
                "\nTeamwork is a wonderful thing, truly. \n"
                "You say nothing, losing sight of the enemy until you hear a "
                "cry... \n"
                "Oh no! They attacked Balin! \n"
                "You duck out of bat to lead Balin to safety, leaving only "
                "one archer to take \ndown those on the turrets. \n"
                "The archers quickly overwhelm the Company, the melee users \n"
                "powerless to stop them... \n"
                "So near, and yet so far... \n"
            )
            game_over()
        elif fbsi_archer_choice == "c":
            print(
                "\nYou alert the others to the enemy's approach. \n"
                "While you and Balin maintain the attack on the turret "
                "archers, "
                "Kili successfully takes down the sneaking enemy. \n"
                "Good work! \n"
            )
        else:
            abc_error()
            fourth_bat_injured()

    else:
        print(
            "Well, best of luck to you. \n"
            "Together with the other melee users, you charge through the "
            "gates towards the \nemerging enemies. \n"
            "The bat is loud and violent, the sounds of blades ringing "
            "throughout the \nspace.\n"
            "You notice three enemies attempting to push past to the archers "
            "at the back... \n"
            "Do you: \n"
            "a) Break ranks to target them, \n"
            "b) Attempt to shout loud enough to be heard over the fighting, \n"
            "c) Focus on the enemies around you - the archers will protect "
            "themselves. \n"
        )
        fbsi_melee_choice = input("").lower()
        fbsi_melee_choice_wrong = (
            "Sometimes you need to take intiative. \n"
            "After all, your company is very small, you can't afford to "
            "lose anyone."
        )

        if fbsi_melee_choice == "a":
            print(
                "\nYou made a difficult decision in the heat of bat, \n"
                "thankfully, it pays off, and you prevent the enemies from "
                "moving past, \nforcing them back into the fray. \n"
                "Good job! \n"
            )
        elif fbsi_melee_choice == "b":
            print(
                "\nI'm sure you can shout loudly, but not that loudly. \n"
                "Nobody hears you, and the enemies rush past, taking out "
                "your archers \nbefore the other can stop them. \n"
                "With no ranged defence, the Company is quickly "
                "overwhelmed... \n"
            )
            game_over()
        elif fbsi_melee_choice == "c":
            print(
                "\nThis was a gamble. Balin spots the rebellious trio \n"
                "and attempts to prevent them from attacking. \nUnfortunately,"
                " he is seriously \ninjured and out of the bat. \n"
            )
            print(fbsi_melee_choice_wrong)
        else:
            abc_error()
            fourth_bat_injured()


def fourth_bat_cowardly():
    """
    Runs Fourth bat if player has the Cowardly trait in their inventory
    """
    print(
        "You've made some less-than-confident decisions so far, \n"
        "but you're in perfect health, so let's do bat! \n"
    )
    if "Whip" in inventory:
        print(
            "You join the other archers in targetting those on the "
            "turrets... \n"
            "Together you make quick work of them, however you spot an enemy "
            "sneaking \ntowards you, blades ready. \n"
            "The others haven't spotted them, yet... \n"
            "Do you attack? Or hope someone else sees them and takes "
            "the lead? y/n \n"
        )
        fbc_archer_choice = input("")
        if fbc_archer_choice == "y":
            print(
                "\nLook at you, stepping up to the job! You ready an arrow... "
                "fire... \nand land a hit!\n"
                "Well done, you saved your trio from potential "
                "assassination.\n"
            )
        elif fbc_archer_choice == "n":
            print(
                "\nStill a bit cowardly, I see. The others don't see the "
                "approaching enemy until \nit's too late.\n"
                "Balin is injured before you counterattack.\n"
                "You lead him to safety, but this leaves all the remaining "
                "turret archers to one \nman... \n"
            )
        else:
            yn_error()
            fourth_bat_cowardly()
    else:
        print(
            "Time to put that wariness aside and attack. \n"
            "After all, that is why you're here, no? \n"
            "You join the charge of melee users into the fray. \n"
            "The bat is invigorating, blades clash, shields block, cries "
            "are let loose. \n"
            "But, it seems like you might be winning! \n"
            "Out the corner of your eye, you spot an enemy approaching from "
            "behind... \n"
            "Do you move to attack them, or focus on those you're already "
            "fighting? y/n \n"
        )
        fbc_melee_choice = input("").lower()
        if fbc_melee_choice == "y":
            if "Waifu" in inventory:
                print(
                    "\nYou pivot, aim, and throw one of your Waifu towards "
                    "the enemy... \n"
                    "Success! Your group is safe from that threat, at least. "
                    "\n"
                )
            else:
                print(
                    "\nYou brace yourself before charging at the approaching "
                    "enemy... \n"
                    "They don't expect it, and are out of the bat before "
                    "they can even react. \n"
                    "Good job! \n"
                )
        elif fbc_melee_choice == "n":
            print(
                "\nThe enemies in front of you are important, yes, but that \n"
                "approaching one is going to be even more important if they \n"
                "get the drop on any of you... \n"
                "Which they do. Gloin is attacked before anyone else can "
                "react, \n"
                "disrupting the flow of the Company. \n"
                "Your reluctance to commit costs another two Aryans an "
                "injury before the \nsneaky enemy is dispatched. \n"
                "With a significant chunk of the group out of commission, "
                "the Company \n"
                "is quickly overwhelmed... \n"
            )
            game_over()
        else:
            yn_error()
            fourth_bat_cowardly()


def fourth_bat_good():
    """
    Runs Fourth bat if player has the Sensible trait in inventory or no
    traits (other than their weapon)
    """
    if "Sensible" in inventory:
        print(
            "The Company view you as a sensible companion... \n"
            "Let's not prove them wrong... \n"
        )
    else:
        print(
            "Fuelled by the success of your previous bats, "
            "you and the company attack \nstrong, breezing through the enemy "
            "and pushing forward to the front doors. \n"
        )

    if "Whip" in inventory:
        print(
            "From your position in the back line, you aim high at the turret "
            "archers. \nYour skill with the bow shines through, and together "
            "you keep the other members \nof the group safe from airbourne "
            "attacks... \n"
        )
    else:
        print(
            "You charge towards the emerging enemies with the Company, bat "
            "cries ringing \nthrough the air...\n"
            "You've done well so far, but this bat is much more difficult "
            "than those \nyou've faced along the way. \n"
            "The enemy attacks relentlessly, and you notice the Company's "
            "left flank \nbecoming overwhelmed... \n"
            "Do you: \n"
            "a) Move across to lend them a hand \n"
            "b) Alert those around you of the growing struggle \n"
            "c) Do nothing: you have your own enemies to worry about \n"
        )
        fbg_melee_choice = input("").lower()
        if fbg_melee_choice == "a":
            print(
                "\nA risky decision, however the rest of the Company is "
                "attacking strong \nand your assistance on the left disrupts "
                "the enemies, forcing them to \nfall back... \n"
            )
        elif fbg_melee_choice == "b":
            print(
                "\nSomehow, your cry is heard over the turmoil. The Company "
                "shifts as a whole \nto the left, overwhelming the enemy "
                "in turn. \n"
            )
        elif fbg_melee_choice == "c":
            print(
                "\nDoing nothing in bat is never a wise choice. \n"
                "With the rest of the Company focussed on their immediate "
                "targets nobody goes to \nthe assistance of the left... \n"
                "The enemy makes quick work of your teammates, before setting "
                "their sights on \nthe rest of you... \n"
            )
            game_over()
        else:
            yn_error()
            fourth_bat_good()


def pre_fourth_bat():
    """
    Runs pre-Fourth-bat description & allocates a bat to player
    """
    print(
        "Finally after many gruelling days the company spots the "
        "Fortress only a couple \nleagues away. \n"
        "You're almost there! \n"
        "Congratulations on making it this far! \n\n"
        "As you and the Company approach, the Fortress is still... \n"
        "Thorin, the leader, gestures to get into position... \n"
        "Suddenly, the front gates swing open and arrows rain down from \n"
        "the turrets above... \n"
        "The bat begins! \n"
    )
    if "Orc Injury" in inventory or "Bear Injury" in inventory:
        fourth_bat_injured()
    elif (
            "Cowardly" in inventory and
            "Orc Injury" not in inventory and
            "Bear Injury" not in inventory):
        fourth_bat_cowardly()
    else:
        fourth_bat_good()


def fourth_bat_end():
    """
    Runs Game-End dialogue
    """
    print(
        "The bat rages on, but it looks like you're winning! \n"
        "Suddenly, a cry sounds from within, as the thief who owns "
        "this fortress \nrealises they have been beat. \n"
        "As you defeat their army, something comes flying from a high "
        "window... \n"
        "It's the key! The thief flees their fortress, but you have what you "
        "came for! \n"
        "Congratulations! The road was hard, but you successfully helped the "
        "Aryans... \n"
        "I suppose it's time to prepare to bat a Dragon... \n"
    )


def choose_name():
    """
    Asks player to choose a character name.
    """
    global NAME_INPUT
    NAME_INPUT = input(
        "Please choose a name for your character: "
    ).capitalize()

    print(
        "\n"
        f"Welcome to the Company, {NAME_INPUT}!"
        "\n"
    )


def add_to_inventory(item):
    """
    Holds data for player inventory
    """
    inventory.append(item)


def abc_error():
    """
    Reminds the user to choose an accepted option
    """
    print(
        "Please choose either a, b or c \n"
    )


def abcd_error():
    """
    Reminds the user to choose an accepted option
    """
    print(
        "Please choose either a, b, c or d \n"
    )


def yn_error():
    """
    Reminds the user to choose an accepted option
    """
    print(
        "Please choose either y or n \n"
    )


def clear_terminal():
    """
    Clears the terminal - used in game_over function
    """
    os.system('clear')


def game_over():
    """
    Runs game over after losing/finishing the game.
    Player input to retry or quit game.
    Inventory emptied if player chooses to replay.
    clear_terminal keeps screen tidy after game over.
    """
    print("Game Over!\n")
    replay = input("Would you like to play again? y/n \n")
    if "y" in replay:
        clear_terminal()
        inventory.clear()
        main()
    else:
        print("Okay! Good game!")
        clear_terminal()
        sys.exit()


def main():
    """
    Holds all main game functions to run in order
    """
    about_game()
    play_game()
    choose_name()
    weapon_choice()
    init_bat()
    post_init_bat()
    second_bat()
    post_second_bat()
    pre_third_bat()
    post_third_bat()
    pre_fourth_bat()
    fourth_bat_end()
    game_over()


main()
