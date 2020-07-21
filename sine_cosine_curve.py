import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)


plt.plot(x,y,x,z)

# naming the x axis 
plt.xlabel('x values from 0 to 4pi')
	
# naming the y axis 
plt.ylabel('sin(x) and cos(x)') 
	
# giving a title to my graph
plt.title('Sin and Cos Plot from 0 to 4pi')
	
# function to show the plot 
plt.show()
