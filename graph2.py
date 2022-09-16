# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [250,500,750,1000,1250] 
# corresponding y axis values 
y = [0.177915,0.151388,0.0872559,0.287111,0.495966] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('area size') 
# naming the y axis 
plt.ylabel('End-to-end Delay') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()