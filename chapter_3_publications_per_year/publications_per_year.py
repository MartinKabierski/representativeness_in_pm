from collections import Counter

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = [9,5]
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18
#plt.rcParams['xlabel.labelsize'] = 20
#plt.rcParams['ylabel.labelsize'] = 20

pubs=Counter([2021,2016,2019,2018,2010,2021,2021,2021,2022,2012,2020,2011,2011,2011,2020,2021,2022,2021,2018,2015,2011,2017,2017,2013,2017,2023,2011,2010,2018,2016,2007,2004,2003,2004,2004,2021,2017,2011,2021,2008,2010,2010,2006])
pubs=Counter([2021, 2019, 2018, 2021, 2021, 2021, 2021, 2020, 2011, 2011, 2020, 2021, 2021, 2017, 2013, 2017, 2023, 2018, 2016, 2007, 2021, 2017, 2011, 2021, 2010, 2006])
print(pubs.keys())
print(pubs)

pubs= [1,1,0,0,0,3,0,1,0,0,1,1,2,1,2,9,0,1]
years = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
#years = ["03","'04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]

plt.bar([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],pubs, align="center", alpha=.3 )
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],years, rotation = 60)
plt.yticks([0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9])

plt.ylabel("# Publications", fontsize=20, labelpad=20)
plt.xlabel("Publication Year", fontsize=20, labelpad=20)
plt.tight_layout()
#plt.show()
plt.savefig("publications_per_year.pdf", format="pdf")
