import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

# CSV data load is much faster with pandas

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()     # Reverse the order of the items in the list
popularity.reverse()    # so that the largest bar will be at the top

# plt.bar(languages, popularity) # this produces a chart where all the x-axis labels (which are languages) over-write eachother
# Horizontal bar chart which expects y-values first
plt.barh(languages, popularity)


plt.title('Most Popular Languguages')

plt.xlabel('Number of People Who Use')

plt.tight_layout()

plt.show()
