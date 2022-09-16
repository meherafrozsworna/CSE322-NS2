# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [10, 20, 30, 40, 50] 
# corresponding y axis values 
y = [0.00848708, 0.0080429, 0.030643,0.0118002,0.027972 ] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Number of flows') 
# naming the y axis 
plt.ylabel('Packet drop ratio') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()