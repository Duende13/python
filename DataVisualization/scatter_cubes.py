import matplotlib.pyplot as plt

x_values = range(1, 5001) # [1,2,3,4,5]
y_values = [x**3 for x in x_values] # [1,4,9,16,25]

plt.style.use('seaborn') 
fig, ax = plt.subplots() 
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Purples,s=10)

# Set chart title and label axes. 
ax.set_title("Cube Numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels. 
ax.tick_params(axis='both', which='major', labelsize=14)

# set the range for each axis
# ax.axis([0, 5100, 0, 130000000000])

plt.show()
# to save it
# plt.savefig('cubes_plot.png', bbox_inches='tight')

