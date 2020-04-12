import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.ticker as plticker
import proc as xp
import tools as xt

#

def make_pie(df = None, title='', case = ''):
    print("Pie chart", case)
    print(df)
    df[case] = df[case] / df[case].values.sum() * 100

    percentages = df[case].tolist()
    labels = df['Country'].tolist()

    cc = plt.cycler("color", plt.cm.tab20.colors)
    plt.style.context({"axes.prop_cycle" : cc})
    

    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['text.color'] = '#909090'
    plt.rcParams['axes.labelcolor']= '#909090'
    plt.rcParams['xtick.color'] = '#909090'
    plt.rcParams['ytick.color'] = '#909090'
    plt.rcParams['font.size'] = 20

    elist = [0]*len(percentages)
    elist[0] = 0.1
    explode= tuple( elist )

    ax = plt.gca()
    p = ax.pie(percentages,
               explode=explode,
               labels=labels,  
               #colors=cc,
               autopct='%1.1f%%', 
               shadow=False,
               startangle=15,   
               pctdistance=1.2,
               labeldistance=1.4)
    ax.axis('equal')
    ax.set_title(title, y = 1.08, color = 'black')
    #ax.legend(frameon=False, bbox_to_anchor=(1.5,0.8))
    plt.tight_layout()
#
def plot_report(df : pd.DataFrame(), column : str, title : str, head : int):
    if column == 'Death Rate':
        _df = df[df['Deaths'] >=10 ].sort_values('Death Rate', ascending=False).head(head)
    else:
        _df = df.sort_values(column, ascending=False).head(head)

    #fig, ax = plt.subplots(2, 2, figsize=(15, 10))
    g = sns.barplot(_df[column], _df.index)#, color = 'b')
    plt.title(title, fontsize=12)#, y = 1.1)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.grid(axis='x', linestyle='--')

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

#
def plot_drate(df : pd.DataFrame(), rank:str, title:str, n:int):

    if rank == 'top':
        _df = df[df['Deaths']>=10].sort_values('Death Rate', ascending=False).head(n)
    elif rank == 'bottom':
        _df = df[df['Confirmed']>=500].sort_values('Death Rate').head(n)
    g = sns.barplot(_df['Death Rate'], _df.index)
    plt.title(title, fontsize=14)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.grid(axis='x')
    for i, q in enumerate(_df['Death Rate']):
        g.text(q*1.01, i+0.1, str(round(q,2)))
#
def plot_view(ax, num, col, title):

    ax[num].plot(col, lw=3)
    ax[num].set_title(title)
    ax[num].xaxis.set_major_locator(plt.MaxNLocator(7))

    myFmt = mdates.DateFormatter('%d-%m')
    ax[num].xaxis.set_major_formatter(myFmt)

    #ticks
    loc = plticker.MultipleLocator(base=4.0) # this locator puts ticks at regular intervals
    ax[num].xaxis.set_major_locator(loc)
    #plt.xticks(np.arange(min(x), max(x)+1, 1.0))

    ax[num].grid(True)
    
def country_view(ax, df : pd.DataFrame(), country:str):
    _df = df[df['Country'] == country].groupby('Date')[['Confirmed',
                                                       'Deaths',
                                                       'Recovered',
                                                       'Active']].sum()

    _df['Death Rate'] = _df['Deaths'] / _df['Confirmed'] * 100
    plot_view(ax, (0,0), _df['Confirmed'], 'Confirmed cases')
    plot_view(ax, (0,1), _df['Deaths'], 'Death cases')
    plot_view(ax, (1,0), _df['Active'], 'Active cases')
    plot_view(ax, (1,1), _df['Death Rate'], 'Death rate')
    fig.suptitle(country, fontsize=16)

#options
kshow= True

kpiedeaths = True
kpieconfirmed = True
kcountryview = True
kdeathrates = True
koverview = True
kstates = True
koverall = True
klead = True
krates = True
kmortal= True
kmortaldense = False
odir = "images/eda"



#data
top=10
ld = xp.DataLoader(top=top)
cd = ld.covid_data
tb = ld.table
leaders = ld.leaders
states = ld.states
groups = ld.grouped
mortal = ld.mortality
cty = ld.cty_data
cty_gr = ld.grouped_cty

# figure
sns.set()
sns.set_style("whitegrid")


#plot
if kpieconfirmed:
    fig, ax = plt.subplots(figsize=(15, 10))
    #plt.figure(figsize=(20,10))
    make_pie(df = cty_gr, title='Confirmed cases', case = 'Confirmed')
    xt.save(fig = fig, fn = xt.name(odir, "pie_confirmed"))

if kpiedeaths:
    #plt.figure(figsize=(20,10))
    fig, ax = plt.subplots(figsize=(15, 10))
    make_pie(df = cty_gr, title='Deaths', case = 'Deaths')
    xt.save(fig = plt, fn = xt.name(odir, "pie_deaths"))
    
if kcountryview:
    country = "Germany"
    fig, ax = plt.subplots(2, 2, figsize=(15,9))
    ## Rotate date labels automatically
    fig.autofmt_xdate()
    country_view(ax, cd, country)
    xt.save(fig=plt, fn = xt.name(odir, country+"_view"))
     
if kdeathrates:
    plt.figure(figsize=(15,10))
    plt.subplot(211)
    plot_drate(cty, 'top','Highest death rate top %i (>=10 deaths)'%(top), top)
    plt.subplot(212)
    plot_drate(cty, 'bottom','Lowest death rate top %i (>=500 confirmed)'%(top), top)

    plt.tight_layout()    
    xt.save(fig=plt, fn = xt.name(odir, "top_death_rates"))
    
if koverview:
    plt.figure(figsize=(15, 15))
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
    fig, ax = plt.subplots(figsize=(15,10))

    ax0 = sns.lineplot(x="Date",
                       y="Confirmed",
                       markers=True,
                       color = 'orange',
                       label="Confirmed",
                       marker = "o",
                       data=tb,
                       ax = ax)
    
    ax1 = sns.lineplot(x="Date",
                       y="Recovered",
                       markers=True,
                       data=tb,
                       color = 'blue',
                       marker = "*",
                       label="Recovered",
                       ax = ax0)

    ax2 = sns.lineplot(x="Date",
                       y="Deaths",
                       markers=True,
                       data=tb,
                       color = 'red',
                       marker = "^",
                       label="Deceased",
                       ax = ax1)

    ax.set(xlabel='Date', ylabel='Number of cases')
    ax.legend()
    xt.save(fig, xt.name(odir, "overall"))
#
if klead:
    print("lead:", leaders.head)

    fig, ax = plt.subplots(figsize=(15,10))
    ax0 = sns.lineplot(x='Date',
                       y='Confirmed All',
                       hue="Country",
                       markers = True,
                       data = leaders,
                       ax = ax)
    ax.legend()
    xt.save(fig, xt.name(odir, "leaders"))

if kstates:
    print("states:", states.head)

    fig, ax = plt.subplots(figsize=(15,10))
    ax0 = sns.lineplot(x='Date',
                       y='Confirmed',
                       hue="State",
                       data = states,
                       markers = True,
                       ax = ax)
    ax.legend()
    xt.save(fig, xt.name(odir, "states"))

if krates:
    ymin = 0
    ymax = 70
    print("lead:", leaders.head)
    fig, ax = plt.subplots(figsize=(15,10))
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
    fig, ax = plt.subplots(figsize=(15,10))
    #We filter out where mortality rate is above 15% 
    mortal = mortal[mortal['Mortality'] < 15]

    #We want only to plot countries with more than 100 confirmed cases,
    # as the situation evolves, more countries will enter this list.
    mortal = mortal[mortal.Confirmed > 100]

    #format date
    myFmt = mdates.DateFormatter('%d-%m')
    ax.xaxis.set_major_formatter(myFmt)

    #ticks
    loc = plticker.MultipleLocator(base=2.0) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc)
    #plt.xticks(np.arange(min(x), max(x)+1, 1.0))

    ## Rotate date labels automatically
    fig.autofmt_xdate()

    ax0 = sns.lineplot(x='Date',
                       y='Mortality',
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



