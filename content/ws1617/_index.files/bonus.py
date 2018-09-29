from sys import argv

bonus = False

def print_hangman():
    if bonus:
        print("bonus is enabled")
    print("normal execution")

if __name__ == '__main__':
    bonus = '-b' in argv
    print_hangman()
