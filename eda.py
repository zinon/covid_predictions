import proc as xp
import tools as xt
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
import pandas as pd
#
def plot_report(df : pd.DataFrame(), column : str, title : str, head : int):
    if column == 'Death Rate':
        _df = df[df['Deaths'] >=10 ].sort_values('Death Rate', ascending=False).head(head)
    else:
        _df = df.sort_values(column, ascending=False).head(head)

    #fig, ax = plt.subplots(2, 2, figsize=(15, 10))
    g = sns.barplot(_df[column], _df.index, color = 'b')
    plt.title(title, fontsize=12)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.grid(axis='x')

    for p in g.patches:
        width = p.get_width()
        f = 1.
        if width < 100:
            f = 1.1
        elif width < 1000:
            f = 1.05
        elif width < 10000:
            f = 1.01
        
        #plt.text(width*f,
        #         p.get_y(), #+0.55*p.get_height(),
        #         '{:1.0f}'.format(width),
        #         ha='center', va='center')
    
    #for p in g.patches:
    #    g.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
    
    for i, v in enumerate(_df[column]):
        if column == 'Death Rate':
            g.text(v*1.01, i+0.2, str(round(v,2)), size =10)
        else:
            g.text(v*1.01, i+0.2, str(int(v)), size = 10)

   
#options
kshow= True

koverview = True
koverall = True
klead = True
krates = True
kmortal= True
kmortaldense = False
odir = "images"


#data
top=10
ld = xp.DataLoader(top=top)
tb = ld.table
leaders = ld.leaders
groups = ld.grouped
mortal = ld.mortality
cty = ld.cty_data

# figure
sns.set()
sns.set_style("whitegrid")


#plot
if koverview:
    plt.figure(figsize=(15, 9))
    plt.subplot(411)
    plot_report(cty, 'Confirmed','Confirmed cases top %i countries'%(top), top)
    plt.subplot(412)
    plot_report(cty, 'Deaths','Death cases top %i countries'%(top), top)
    plt.subplot(413)
    plot_report(cty, 'Active','Active cases top %i countries'%(top), top)
    plt.subplot(414)
    plot_report(cty, 'Death Rate','Death rate top %i countries (>=10 deaths only)'%(top), top)
    plt.tight_layout()
    
    xt.save(fig=plt, fn = xt.name(odir, "overview"))
    
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


    


if kshow:
    plt.tight_layout()
    plt.show()



