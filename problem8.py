

print("Enter Player1 name")
user1 = input()
print("Enter Player2 name")
user2 = input()


print("Select Rock,Paper or scissors "+user1)
u1 = input()
print("select Rock,Paper or scissors "+user2)
u2 = input()


def selectWinner(u1,u2,user1,user2):
    if(u1 == u2):
        print("It's a tie")
    elif (u1 == 'Rock' and u2 == 'scissors') or (u1 == 'scissors' and u2 == 'Paper') or (u1 == 'Paper' and u2 == 'Rock'):
        print(user1+" wins")
    elif (u2 == 'Rock' and u1 == 'scissors') or (u2 == 'scissors' and u1 == 'Paper') or (u2 == 'Paper' and u1 == 'Rock'):
        print(user2+" wins")


selectWinner(u1,u2,user1,user2)

