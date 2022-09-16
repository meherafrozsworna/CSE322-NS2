# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [250,500,750,1000,1250] 
# corresponding y axis values 
y = [559997,594971,617757,456878,366397] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('area size') 
# naming the y axis 
plt.ylabel('Network throughput') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()