import proc as xp
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

ld = xp.DataLoader()

tb = ld.table
leaders = ld.leaders
groups = ld.grouped
mortal = ld.mortality

if not os.path.exists("images"):
    os.mkdir("images")

sns.set()
sns.set_style("whitegrid")

fig, ax = plt.subplots(figsize=(15,7))

koverall = False
klead = False
krates = False
kmortal=False
kmortaldense=True

#
if koverall:
    ax0 = sns.lineplot(x="Date",
                       y="Confirmed",
                       markers=True,
                       color = 'orange',
                       label="Confirmed",
                       data=tb)
    
    ax1 = sns.lineplot(x="Date",
                       y="Recovered",
                       markers=True,
                       data=tb,
                       color = 'blue',
                       label="Recovered",
                       ax = ax0)

    ax2 = sns.lineplot(x="Date",
                       y="Deaths",
                       markers=True,
                       data=tb,
                       color = 'red',
                       label="Deceased",
                       ax = ax1)


#
if klead:
    print("lead:", lead.head)
    
    ax = sns.lineplot(x='Date',
                 y='Confirmed All',
                 hue="Country",
                 data = leaders)
    

if krates:
    print("lead:", leaders.head)
    
    ax0 = sns.lineplot(x='Date',
                      y='Deaths_All_Frac',
                      data = groups,
                      color = "red",
                      label = "Deaths")
    ax0.set(xlabel='Date', ylabel='Percentage')
    

    ax1 = sns.lineplot(x='Date',
                       y='Recovered_All_Frac',
                       data = groups,
                       color = "blue",
                       label = "Recoved",
                       ax = ax0)

    ax1 = sns.lineplot(x='Date',
                       y='World_growth_rate',
                       data = groups,
                       color = "orange",
                       label = "Global Confirmed",
                       ax = ax0)


if kmortal:
    print("mortal:", mortal.head)
    
    #We filter out where mortality rate is above 10% 
    mortal = mortal[mortal.mortality_rate < 10]

    #We want only to plot countries with more than 100 confirmed cases,
    # as the situation evolves, more countries will enter this list.
    mortal = mortal[mortal.Confirmed > 100]

    ax0 = sns.lineplot(x='Date',
                       y='mortality_rate',
                       hue='Country',
                       data = mortal)

    ax0.set(xlabel='Date', ylabel='Mortality Percentage')


if kmortaldense:
    print("mortal density:", mortal.head)
    
    #We filter out where mortality rate is above 10% 
    #mortal = mortal[mortal.mortality_rate < 10]

    #We want only to plot countries with more than 100 confirmed cases,
    # as the situation evolves, more countries will enter this list.
    mortal = mortal[mortal.Confirmed > 100]

    ax0 = sns.lineplot(x='Date',
                       y='dense_normed',
                       hue='Country',
                       data = mortal)

    ax0.set(xlabel='Date', ylabel='Mortality / Population Density')

plt.tight_layout()
plt.show()


#fig.write_image("images/all.png")
