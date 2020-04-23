from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# slices = [120, 80, 30, 20]
# labels = ['Sixty', 'Forty', 'Extra1', 'Extra2']
# colors = ['blue', 'red', 'yellow', 'green']
# colors = ['#008fd5', '#fc4f30', '#e5af37', '#6d904f']

# Language Popularity
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097,
#           23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell',
#           'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

# Pie Charts always look better and are more informative for 5 or less data slices
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# Want to explode (emphasize) python and the fraction 0.1 represents how much
# the radius wants to be exploded out by (10% in this case).
# The fraction is the proportion of the radius that the point
# of the slice is moved out from the centre of the pie
explode = [0, 0, 0, 0.1, 0]
# plt.pie(slices, labels=labels, colors=colors,
#         wedgeprops={'edgecolor': 'black'})

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

# Colors:
# Blue =  # 008fd5
# Red =  # fc4f30
# Yellow =  # e5af37
# Green =  # 6d904f
