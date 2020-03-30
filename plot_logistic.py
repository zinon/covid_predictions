import matplotlib.pyplot as plt
import numpy as np
# 100 linearly spaced numbers
x1=15
x = np.linspace(0, x1, 100)
x0 = 5
N=10e3
k=0.9
# the function, which is y = x^2 here
y = N / (1 + np.exp(-k*(x - x0)))

circle1 = plt.Circle( (x0, N/2.), radius=0.2, color='blue')

# setting the axes at the centre
fig = plt.figure(figsize=(10.,7.))
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.ylabel('f(t)')
plt.xlabel('t')


#plt.gcf().gca().add_artist(circle1)
ax.add_artist(circle1)

# plot the function
plt.plot(x,y, 'r')

a=1
plt.plot([x0-a, x0+a], [N/4., 3/4.*N], color='k', linestyle='-', linewidth=2)
plt.plot([0, x1], [N, N], color='k', linestyle='--', linewidth=1)



    
# show the plot
plt.show()
