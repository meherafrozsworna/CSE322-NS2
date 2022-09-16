# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [250,500,750,1000,1250] 
# corresponding y axis values 
y = [0.0116212,0.0168662,0.017341,0.0242787,0.0474342] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('area size') 
# naming the y axis 
plt.ylabel('Packet drop ratio') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()