import json


def load_json(path):
    data = []
    with open(path, "r") as file:
        data = json.load(file)
    return data


def write_json(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


class Player:
    def __init__(self, name="", mode="", bag={}):
        self.name = name
        self.mode = mode
        self.bag = bag

    def initCaddie(self):
        self.caddie = GolfCaddie(self, self.mode, self.bag)

    def __str__(self):
        return f"Player {self.name} is using the {self.mode} mode."

    def __repr__(self):
        return f"Player {self.name} is using the {self.mode} mode."

    def get_mode(self):
        while True:
            self.mode = input("What mode would you like to use?(Custom or Pro)\n")

            if self.mode.lower() == "pro" or self.mode.lower() == "custom":
                return

            print("Please input Custom or Pro to select a mode.\n")

    def getNextClub(self):
        return self.caddie.closest_value()


class GolfCaddie:
    def __init__(self, player, mode, bag):
        self.mode = mode
        self.player = player
        self.name = player.name
        self.bag = bag

        if self.mode == "pro":
            self.pro()
        else:
            self.custom()

    def custom(self):
        self.bag = {}
        count = 0

        while True:
            club = input(
                "Please enter the clubs in your bag one at a time. What club would you like to enter first?(Driver, 3-Wood, 5-wood, Hybrid, 3-9, PW, 46-60, putter)\n"
            )
            if club.lower() == "return" or count == 14:
                break

            distance = int(
                input(
                    "Please enter the average yardage you hit the club. For your putter, enter 0.\n"
                )
            )
            self.bag[self.name][club] = distance
            count += 1

    def pro(self):
        print(
            "This setting is using the Tour averages (in carry yards) for Driver, 3-wood, 3-9, PW, 52, 56, 60, Putter.\n"
        )

        self.bag = {
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

    def shot(self):
        shotTypes = ["tee", "fairway", "rough", "sand", "putt"]
        while True:
            shot_type = input(
                "What type of shot are you hitting?(Tee, Fairway, Rough, Sand, Putt)\n"
            ).lower()
            if shot_type in shotTypes:
                return shot_type
            print("Please enter a vaild shot.(Tee, Fairway, Rough, Sand, Putt)\n")

    def putting(self):
        return float(input("Please enter your distance from the hole in feet.\n"))

    def distance(self):  # return true if on green
        while True:
            dist = input(
                "How far are you from the green?(Enter in yards or 0 if you're on the green)\n"
            )

            if dist == "0":
                return float(self.putting()), True

            if dist.isnumeric():
                return float(dist), False

            print("Please enter a valid number or 0 for on the green.\n")

    def closest_value(self):
        dist, green = self.distance()

        if green:
            return "Putter"

        def __map__(x, a, b, c, d):
            return c + (x - a) * (d - c) / (b - a)

        clubs = []
        for club, distance in self.bag.items():
            clubs.append([club, distance])

        clubs.sort(key=lambda x: x[1])

        for i in range(len(clubs) - 1):
            if dist >= clubs[i][1] and dist <= clubs[i + 1][1]:
                return clubs[i + 1], (__map__(dist, 0, clubs[i + 1][1], 0, 1)) * 100


P = Player("Bob", "pro")
P.initCaddie()
print(P.getNextClub())
