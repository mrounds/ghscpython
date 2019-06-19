import random
def main():
    """ Main method """
    choice = input("type 'rock', 'paper' or 'scissors': ")
    x = random.randrange(1,4)
    y = 0
    if choice=="rock":
        y = 1
    elif choice=="paper":
        y = 2
    elif choice=="scissors":
        y = 3
    if x==1 and y==1:
        print("tie")
    elif x==2 and y==2:
        print("tie")
    elif x == 3 and y == 3:
        print("tie")
    elif x==1 and y==2:
        print("paper beats rock, user wins!")
    elif x == 2 and y == 1:
        print("paper beats rock, cpu wins!")
    elif x==1 and y==3:
        print("rock beats paper, user wins!")
    elif x == 3 and y == 1:
        print("rock beats paper, cpu wins!")



if __name__ == "__main__":
    main()
