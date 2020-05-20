player1=int(input('Enter the runs scored by 1st playern'))
player2=int(input('\nEnter the runs scored by 2nd player'))
player3=int(input('\nEnter the runs scored by 3rd player'))

rate1 = player1 * 100 / 60
rate2 = player2 * 100 / 60
rate3 = player3 * 100 / 60

print('\n\n strike rate of player 1 is : ', rate1)
print('\n strike rate of player 2 is : ', rate2)
print('\n strike rate of player 3 is : ', rate3)

print('\n\n the runs scored by player1 in 120 balls is : ',player1*2)
print('\n the runs scored by player1 in 120 balls is : ', player2*2)
print('\n the runs scored by player1 in 120 balls is : ', player3*2)

print('\n\n the maximum number of sixes hitted by player 1 is : ',rate1//6)
print('\n the maximum number of sixes hitted by player 1 is : ', rate2//6)
print('\n the maximum number of sixes hitted by player 1 is : ',rate3//6) 
