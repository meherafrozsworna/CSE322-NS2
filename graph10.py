# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [10, 20, 30, 40, 50] 
# corresponding y axis values 
y = [0.139307, 0.140433, 0.16642, 0.225228,0.24838 ] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Number of flows') 
# naming the y axis 
plt.ylabel('End-to-end Delay') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()