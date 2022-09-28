from platform import libc_ver
import time
import random
import re
from elo import elo_rating


class Anime:
    def __init__(self, name, rating = 1000):
        self.name = name
        # raise exception if not string?
        self.rating = rating
        # self.ranking
        # use ranking attribute instead of dictionary with keys, use indexs?

    def __str__(self):
        return f"{self.name}, elo:{self.rating}"

rankings = []
watchlist = []
menu_options = """
                > add an anime to ranking (1)
                > add an anime to watch list (2)
                > do a random ranking (3)
                > view rankings (4)
                > pick an anime to watch (5)
                > exit program and save (6)
               """
menu_options_num = 6

def make_choice(num_options):
    choice = int(input("Enter choice: > "))
    while not(0 < choice <= num_options):
        print("Not a valid choice")
        choice = input("> ")
    return choice


# prints the main menu
def print_menu():
    print("What would you like to do?")
    print(menu_options)
    choice = make_choice(menu_options_num)
    
    if choice == 1:
        add_anime_to_ranking()
        print_menu()
    elif choice == 2:
        add_anime_to_watchlist()
        print_menu()
    elif choice == 3:
        random_ranking()
        print_menu()
    elif choice == 4:
        print("Which would you like to view"
                "> Top 10 rankings (1)\n> Full rankings (2)")
        choice = int(input("Enter your choice > "))
        if choice == 1:
            print_rankings(True) 
        else:
            print_rankings(False)
        print_menu()
    elif choice == 5:
        chose_anime_to_watch()
        print_menu()
    elif choice == 6:
        print("\nGoodbye")
        time.sleep(0.5)
        return



def add_anime():
    print("\nType the name of the anime and press \'enter\' when done.")
    name = input("> ")
    anime = Anime(name)
    print(f"\n{anime.name} was successfully added")
    return anime


# add_anime_to_ranking: adds a new anime to the rankings
def add_anime_to_ranking():
    anime = add_anime()

    if len(rankings) == 0:
        rankings.append(anime)
        print("\nPress enter to return to main menu")
        input()
        return
    
    do_rankings(anime)

    rankings.append(anime)
    rankings.sort(key = lambda anime : anime.rating, reverse = True)
    print(f"""The final ranking for {anime.name} is {rankings.index(anime) + 1}
    out of {len(rankings)} animes""")
    print("\nPress enter to return to main menu")
    input()


# do rankings: takes in an anime, matches it against the current animes 
#              listed in the program for up to 10 animes, and updates the elo
#              scores and rankings accordingly
# anime_a: the new anime to be added

def do_rankings(anime_a):
    num_anime = len(rankings)
    if num_anime > 10:
        max = 10
    else:
        max = len(rankings)
    animes = random.sample(rankings, max)

    print(" Select the option you prefer more by selecting the corresponding"
           "number and hitting \'enter\'")

    for anime_b in animes:
        rank(anime_a, anime_b)



# rank: prompts the user to chose between two animes
#       calculates and updates the elo scores for each option 
#       accordingly based of the user's input
# anime_a: the first anime
# anime_b: the second anime
def rank(anime_a, anime_b):
    print("\nWhich anime was better")
    print(f"{anime_a.name} (1)\n{anime_b.name} (2)")
    choice = make_choice(2)
    
    if choice == 1:
        score_a = 1
    else:
        score_a = 0
    
    elo_a, elo_b = elo_rating(anime_a.rating, anime_b.rating, score_a)
    anime_a.rating = elo_a
    anime_b.rating = elo_b


def random_ranking():
    num_animes = len(rankings)
    if num_animes > 20:
        max = 20
    else:
        max = (num_animes // 2) * 2  # make max an even number

    animes = random.sample(rankings, max)
    i = 0  # index
    while not i >= max:
        rank(animes[i], animes[i + 1])
        i += 2
    rankings.sort(key = lambda anime : anime.rating, reverse = True)
    print_rankings(True)


# line_to_anime: converts a given string to an object of class Anime
def line_to_anime(line):
    name, other, rating = re.split(r",|:", line)
    return Anime(name, float(rating))

# print rankings: prints the current rankings to the terminal
# top_ten: an bool parameter indicating the number of animes to print,
#       the top 10 or the full list
def print_rankings(top_ten):
    print("\nYour top anime are...\n")
    time.sleep(0.5)
    index = 0
    for anime in rankings:
        print(f"{index}. {anime}")
        index += 1
        if top_ten:
            if index == 10:
                break
    print("\nPress enter to return to main menu")
    input()


def add_anime_to_watchlist():
    anime = add_anime()
    watchlist.append(anime)
    watchlist.sort(key=lambda anime:anime.name)
    print("\nPress enter to return to main menu")
    input()

def chose_anime_to_watch():
    anime = random.choice(watchlist)
    print("The next anime you should start is ...")
    time.sleep(0.5)
    print(f"\n{anime.name}")
    print("Press enter to return to main menu")
    input()

# MAIN
print("Welcome to Alexis's anime watch list")

with open("ranking_list.txt", 'r') as rankings_list:
    for line in rankings_list:
        rankings.append(line_to_anime(line))

with open("watch_list.txt", 'r') as watch_list:
    for line in watch_list:
        watchlist.append(Anime(line))

time.sleep(0.5)
print_menu()

with open("ranking_list.txt", 'w') as rankings_list:
    for anime in rankings:
        rankings_list.write(str(anime) + '\n')

with open("watch_list.txt", 'w') as watch_list:
    for anime in watchlist:
        watch_list.write(anime.name)



