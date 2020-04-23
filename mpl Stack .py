from matplotlib import pyplot as plt

# Stack plots are good for tracking totals and their breakdown


plt.style.use("fivethirtyeight")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Points scored in every minute of the game for each point
player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['player1', 'player2', 'player3']
colors = ['#6d904f', '#fc4f30', '#008fd5']
# in the first minute, the total points for the team = 3

# Distribution of minutes in the first minute which gives a simple pie chart
# plt.pie([1, 1, 1], labels=['Player1', 'Player2', 'Player3'])

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc='upper left')

# plt.legend(loc=(0.07, 0.05)) # place legend 7% from the left(y-axis) and 5% from the botton (x-axis)

plt.title('My Awesome Stack Plot')
plt.tight_layout()
plt.show()

# Colors:
# Blue =  #008fd5
# Red =  #fc4f30
# Yellow =  #e5af37
# Green =  #6d904f
