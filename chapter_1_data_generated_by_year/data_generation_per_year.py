from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [9,4.5]
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14

data = [1,5,6.5,9,12.5,15.5,18,26,33,41,64.2,79,97,120,147,181]
years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
plt.bar([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],data, align="center", alpha=.3 )
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],years, rotation = 60)
plt.yticks([0,25,50,75,100,125,150,175,200],[0,25,50,75,100,125,150,175,200])

plt.ylabel("Data Volume in zetabytes", fontsize=14, labelpad=20)
plt.xlabel("Year", fontsize=14, labelpad=20)
plt.tight_layout()
#plt.show()
plt.savefig("data_generated_per_year.pdf", format="pdf")