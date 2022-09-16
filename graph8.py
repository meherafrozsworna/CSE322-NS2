# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [20, 40, 60, 80, 100] 
# corresponding y axis values 
y = [0.00301974, 0.0101946, 0.0251118, 0.00637349, 0.0126193] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Number of nodes') 
# naming the y axis 
plt.ylabel('Packet drop ratio') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()