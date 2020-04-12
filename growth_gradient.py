import matplotlib.pyplot as plt
import numpy as np
import proc as xp
import xquery as xq
import tools as xt

odir = 'images/doubling_time'
query_raw = xq.Query("Base", "Date > '2020-03-01'")
query_derived = xq.Query("Recent", "")#RecentDays <=15 ")

y_data_label = 'Confirmed All'

asia = ['Mainland China', 'South Korea', 'Iran']
europe = ['Germany',  'UK', 'Italy', 'Spain', 'France']#, 'Greece']#, 'Cyprus']
amerika = ['US']
countries = europe + amerika # + asia
#countries = ['Germany']

fig, ax = plt.subplots(figsize=(15,7))
    
for country in countries:
    dloader = xp.DataLoader(query = query_raw, countries = [country])
    df = dloader.leaders
    if  query_derived.query:
        df = df.query( query_derived.query )
    x = df['Days'].to_numpy()
    dx = x[1] - x[0]
    y = df[y_data_label].to_numpy()
    dy = np.gradient(y, dx )
    k = dy/y
    T = np.log(2)/k
    
    
    plt.plot(x,
             T,
             label=country)
         

plt.legend(loc='upper left', fontsize=18)
plt.grid(axis='x', linestyle='--')
plt.grid(axis='y', linestyle='--')
#plt.tight_layout()
ax.set(xlabel='Day', ylabel='doubling time')
    
xt.save(fig = plt, fn = xt.name(odir, "pie_confirmed_gradients"))
plt.show()
plt.close('all')
