import matplotlib.pyplot as plt
import numpy as np

#assuming a normal distrubtion with mean=0 and standard deviation=1
data = np.random.normal(loc = 0, scale = 1, size=1000) 
#np.random module has np.random.normal function that lets u select any number of random numbers from a normal distribution.
#in the syntax, loc denotes mean, scale denotes standard deviation and size denotes number of entries(size=(4,3) would;ve meant 4 rows 3 columns)
xrange = range(len(data)) #this is effectively creating all numbers from 0 to (1000-1), for indexing on x axis
plt.scatter(xrange, data) #Makes a scatter graph with 1000 indexes on x axis, and corresponding values from data on y axis
plt.xlabel("Index")
plt.ylabel("Value")

plt.show()

