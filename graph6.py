# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [20, 40, 60, 80, 100] 
# corresponding y axis values 
y = [0.251146, 0.197923, 0.174411,0.246205,0.392134] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Number of nodes') 
# naming the y axis 
plt.ylabel('End-to-end Delay') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()