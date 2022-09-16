# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [10, 20, 30, 40, 50] 
# corresponding y axis values 
y = [0.990775, 0.991226, 0.968536,0.987447, 0.970952] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Number of flows') 
# naming the y axis 
plt.ylabel('Packet delivery ratio') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()