import random

def nim_minimal(n):
    return 1

def nim(n):
    return random.choice(range(1,min(n,3)+1))

def nim_best(n):
    taken = n % 4
    if taken:
        return taken
    else:
        return random.choice(range(1,min(n,3)+1))

def nim_human(n):
    while True:
        taken = int(input("There are %d sticks. How many will you like to take (1/2/3)" % n))
        if taken in range(1,min(n,3)+1):
            return taken
        print("Invalid move")

player_pool = [nim_minimal, nim, nim_best, nim_human]
player_pool = {p.__name__:p for p in player_pool}

def select_players():
    players = []

    while len(players) < 2:
        print("There are the players: %e" % "/". join(player_pool.keys()))
        p = input("Name one: ")
        if p not in player_pool.keys():
            print("Invalid Player. Select again: ")
            continue
        players.append(p)
        print("Player %s begins, player %s plays second." % tuple(players))
        return players

def game():
    while True:
       n = int(input("Heap size? "))
       if n > 0: break

    current, other = tuple(select_players())

    while n > 0: 
        print("Heap has %d sticks." % n)
        taken = player_pool[current](n) 
        print("%s takes %d sticks.\n" % (current, taken))
        
        n -= taken
        current, other = other, current
    print("%s has lost." % current)

print(nim_minimal(2))
print(nim(2))
print(nim_best(3))
print(nim_human(3))
print(game())

