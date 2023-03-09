#!/usr/bin/python
import json

# mode = ""
# clubs = {club:distance}
# shot_type = ""
# dist = 0
# gdist = 0
# u_name = ""

# Dictionary needs to be a key of the name with a value dictionary of the clubs values


class golf_cad:
    def get_name():
        global u_name
        u_name = input("Please enter your name with no spaces.\n")

    def load_json():
        with open("user_data.json", "r") as file:
            data = json.load(file)
        return

    def write_json():
        with open("user_data.json", "w") as file:
            json.dumps(bag, file)
        return

    def get_mode():
        global mode
        while True:
            mode = input("What mode would you like to use?(Custom or Pro)\n")
            if mode.lower() == "pro" or mode.lower() == "custom":
                break
            else:
                print("Please input Custom or Pro to select a mode.\n")
                continue

    # clubs = [Driver, 3-wood,...,putter]
    # cdist = [250,230,...,green]

    def custom():
        global bag
        global u_name
        bag = {}
        clubs = []
        cdist = []
        while True:
            club = input(
                "Please enter the clubs in your bag one at a time. What club would you like to enter first?(Driver, 3-Wood, 5-wood, Hybrid, 3-9, PW, 46-60, putter)\n"
            )
            distance = input(
                int(
                    "Please enter the average yardage you hit the club. For your putter, enter 0.\n"
                )
            )
            if club.lower() == "return":
                for club, distance in zip(clubs, cdist):
                    bag[u_name][club] = distance
                break
            elif len(clubs) < 14:
                clubs.append(club)
                cdist.append(distance)
                if len(clubs) == 14:
                    for club, distance in zip(clubs, cdist):
                        bag[u_name][club] = distance
                    break
                else:
                    continue
            else:
                print("There are too many clubs in your bag.\n")
                break
        return bag

    def pro():
        print(
            "This setting is using the Tour averages (in carry yards) for Driver, 3-wood, 3-9, PW, 52, 56, 60, Putter.\n"
        )
        global bag
        bag = {
            "Driver": 275,
            "3-wood": 243,
            "3": 212,
            "4": 203,
            "5": 194,
            "6": 183,
            "7": 172,
            "8": 160,
            "9": 148,
            "PW": 136,
            "52": 120,
            "56": 110,
            "60": 100,
            "putter": 0,
        }

    def sortBag():
        global bag
        global sorted_bag
        global sorted_clubs_by_distance
        sorted_clubs_by_distance = sorted(
            bag.items(), key=lambda x: int(x[1]), reverse=True
        )
        sorted_bag = dict(sorted_clubs_by_distance)

    def shot():
        global shot_type
        while True:
            shot_type = input(
                "What type of shot are you hitting?(Tee, Fairway, Rough, Sand, Putt)\n"
            )
            if (
                shot_type.lower() == "tee"
                or shot_type.lower() == "fairway"
                or shot_type.lower() == "rough"
                or shot_type.lower() == "sand"
                or shot_type.lower() == "putt"
            ):
                break
            else:
                print("Please enter a vaild shot.(Tee, Fairway, Rough, Sand, Putt)\n")
                continue

    def distance():
        global dist
        global gdist
        while True:
            dist = float(
                input(
                    "How far are you from the green?(Enter in yards or 0 if you're on the green)\n"
                )
            )
            if dist == 0:  # and shot_type.lower() == "putt":
                gdist = input("Please enter your distace from the hole in feet.\n")
                break
            elif isinstance(float(dist), int) or isinstance(float(dist), float):
                break
            else:
                print("Please enter a valid number or 0 for on the green.\n")
                continue

    def closest_value():
        global res_club, res_dist, dist
        res_club, res_dist = min(sorted_bag.items(), key=lambda x: abs(dist - x[1]))
        # res_club, res_dist = min(
        #     sorted_bag.items(),
        #     key=lambda x: abs(dist - x[1]) if (dist < x[1]) else 0.0,
        # )
        # return res_club, res_dist

    def putting():
        print(
            "This will return the PGA Tour putting stats to the closest number to the one entered.\n"
        )

    def club_choice():
        global dist, res_club, res_dist, per_dist
        # golf_cad.closest_value()
        per_dist = (dist / res_dist) * 100
        percent = "%"
        print(
            "The correct club is {0}: {1} at {2:.2f}{3} for a {4} yard shot.\n".format(
                res_club, res_dist, per_dist, percent, dist
            )
        )
        # print(
        #     "This will return the club choice based on carry distances and the swing percentage needed.\n"
        # )

    if __name__ == "__main__":
        print("Welcome to the Golf Caddie!\n")
        get_name()
        get_mode()
        if mode.lower() == "custom":
            custom()
        else:
            pro()
        sortBag()
        while True:
            user_input = input(
                "If you would like to exit the program, type: exit or hit enter to continue.\n"
            )
            if user_input.lower() == "exit":
                break
            shot()
            distance()
            closest_value()
            if shot_type.lower() == "putt" and dist == 0:
                putting()
            else:
                club_choice()
