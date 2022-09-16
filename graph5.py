# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [20, 40, 60, 80, 100] 
# corresponding y axis values 
y = [709192,525554,464428,512539,526873] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Number of nodes') 
# naming the y axis 
plt.ylabel('Network throughput') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()