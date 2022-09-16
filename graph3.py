# importing the required module 

import matplotlib.pyplot as plt 
  
# x axis values 
x = [250,500,750,1000,1250] 
# corresponding y axis values 
y = [0.987507,0.982046,0.982133,0.974314,0.952566] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('area size') 
# naming the y axis 
plt.ylabel('Packet delivery ratio') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()