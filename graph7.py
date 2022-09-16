# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [20, 40, 60, 80, 100] 
# corresponding y axis values 
y = [0.996516, 0.988879, 0.973856, 0.99267, 0.986457] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Number of nodes') 
# naming the y axis 
plt.ylabel('Packet delivery ratio') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()