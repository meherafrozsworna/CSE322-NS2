# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [10, 20, 30, 40, 50] 
# corresponding y axis values 
y = [444686,671239,582335,640924, 583706] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('Number of flows') 
# naming the y axis 
plt.ylabel('Network throughput') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()