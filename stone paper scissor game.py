
while True:
    import random

    def play():
        user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        opponent = random.choice(['r', 'p', 's'])

        if user == opponent:
            return 'game tie'
        # r > s, s > p, p > r
        if win(user, opponent):
            return 'dear user, YOU WON'

        return 'You lost'

    def win(user, opponent):
        if (user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') \
            or (user == 'p' and opponent == 'r'):
            return True

    print(play())
