import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')

# Data in the data.csv file are:
#       Responder_id,LanguagesWorkedWith
#       1,HTML/CSS;Java;JavaScript;Python
#       2,C++;HTML/CSS;Python

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

# print(language_counter) # prints out for about 28 languages
# print(language_counter.most_common(15))
# which prints out:
# [('JavaScript', 59219), ('HTML/CSS', 55466), ('SQL', 47544), ('Python', 36443), ('Java', 35917),
# ('Bash/Shell/PowerShell', 31991), ('C#', 27097), ('PHP', 23030), ('C++', 20524), ('TypeScript', 18523),
# ('C', 18017), ('Other(s):', 7920), ('Ruby', 7331), ('Go', 7201), ('Assembly', 5833)]

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# print(languages)
# print(popularity)
# which prints out two lists:
# ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
# [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]

languages.reverse()     # Reverse the order of the items in the list
popularity.reverse()    # so that the largest bar will be at the top

# plt.bar(languages, popularity) # this produces a chart where all the x-axis labels (which are languages) over-write eachother
# Horizontal bar chart which expects y-values first
plt.barh(languages, popularity)


# row = next(csv_reader)
# print(row)  # prints --> {'Responder_id': '1', 'LanguagesWorkedWith': 'HTML/CSS;Java;JavaScript;Python'}
# print(row['LanguagesWorkedWith'])   # prints --> HTML/CSS;Java;JavaScript;Python
# prints --> ['HTML/CSS', 'Java', 'JavaScript', 'Python']
# print(row['LanguagesWorkedWith'].split(';'))

plt.title('Most Popular Languguages')
# plt.xlabel('Programming Languages')
# plt.ylabel('Number of People Who Use')
# plt.ylabel('Programming Languages') # rather obvious so don't really need it
plt.xlabel('Number of People Who Use')

plt.tight_layout()

plt.show()


# # # # # # # # # # # # # # # # # #
# C O N T E R S  I N  P Y T H O N #
# # # # # # # # # # # # # # # # # #
#
# Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.

# >>> from collections import Counter
# >>> c = Counter(['Python', 'JavaScript'])
# >>> c
# Counter({'Python': 1, 'JavaScript': 1})
# >>> # So Counter keeps a reord of how many times it has seem the items

# >>> c.update(['C++', 'Python'])
# >>> c
# Counter({'Python': 2, 'JavaScript': 1, 'C++': 1})
# >>> # So, Python count has gone up by 1 and created a new counter for C++
# >>>
