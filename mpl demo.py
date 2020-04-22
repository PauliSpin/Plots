from matplotlib import pyplot as plt

# Ages
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Salaries
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# plt.plot(ages_x, dev_y)   Use this if you are going to add to the legend explicitly
plt.plot(ages_x, dev_y, label='All Devs')


# Median Python Developer Salaries by Age

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, label='Python')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

# Could add legends in the order that we created them in the plot above:
# plt.legend(['All Devs', 'Python'])
# But you have to knowthe order, so not really preferred
plt.legend()    # Already included the legends in the 'label=' statements above
plt.show()
