import proc as xp
import tools as xt
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
#        
#options
kshow=True
koverall = True
klead = True
krates = True
kmortal= True
kmortaldense = False
odir = "images"


#data
ld = xp.DataLoader()
tb = ld.table
leaders = ld.leaders
groups = ld.grouped
mortal = ld.mortality


# figure
sns.set()
sns.set_style("whitegrid")


#plot
if koverall:
    fig, ax = plt.subplots(figsize=(15,7))
    
    ax0 = sns.lineplot(x="Date",
                       y="Confirmed",
                       markers=True,
                       color = 'orange',
                       label="Confirmed",
                       data=tb,
                       ax = ax)
    
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

    ax.legend()
    xt.save(fig, xt.name(odir, "overall"))
#
if klead:
    print("lead:", leaders.head)

    fig, ax = plt.subplots(figsize=(15,7))
    ax0 = sns.lineplot(x='Date',
                       y='Confirmed All',
                       hue="Country",
                       data = leaders,
                       ax = ax)
    ax.legend()
    xt.save(fig, xt.name(odir, "leaders"))

if krates:
    ymin = 0
    ymax = 70
    print("lead:", leaders.head)
    fig, ax = plt.subplots(figsize=(15,7))
    ax0 = sns.lineplot(x='Date',
                      y='Deaths_All_Frac',
                      data = groups,
                      color = "red",
                       label = "Deaths",
                       ax = ax)
    

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
    ax.set(xlabel='Date', ylabel='Percentage')
    ax.set_ylim([ymin,ymax])
    start, end = ax.get_ylim()
    stepsize = 2
    ax.yaxis.set_ticks(np.arange(start, end, stepsize))

    ax.legend()
    xt.save(fig, xt.name(odir, "rates"))
        
if kmortal:
    print("mortal:", mortal.head)
    fig, ax = plt.subplots(figsize=(15,7))
    #We filter out where mortality rate is above 10% 
    mortal = mortal[mortal.mortality_rate < 10]

    #We want only to plot countries with more than 100 confirmed cases,
    # as the situation evolves, more countries will enter this list.
    mortal = mortal[mortal.Confirmed > 100]

    ax0 = sns.lineplot(x='Date',
                       y='mortality_rate',
                       hue='Country',
                       data = mortal,
                       ax = ax)

    ax.set(xlabel='Date', ylabel='Mortality Percentage')
    ax.legend()
    
    xt.save(fig, xt.name(odir, "mortality"))

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

    xt.save(fig, xt.name(odir, "mortality_normalized_per_pop_density"))

    
plt.tight_layout()

if kshow:
    plt.show()



