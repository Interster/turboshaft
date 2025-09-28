#%%
import scipy.io
import matplotlib.pyplot as plt
import numpy as np

#%%
# Laai die vlugtoetsdata
NG1 = scipy.io.loadmat('data/NG1.mat')
NG2 = scipy.io.loadmat('data/NG2.mat')
T41 = scipy.io.loadmat('data/T41.mat')
T42 = scipy.io.loadmat('data/T42.mat')
time064 = scipy.io.loadmat('data/time0064.mat')

#%%
# Assuming the .mat file contains variables 'x' and 'y' for plotting
# Adjust these keys based on the actual variable names in your .mat file
x = time064['time0064'].flatten()  # Flatten to ensure 1D array
y = NG['NG10064'].flatten()  # Flatten to ensure 1D array

#%%

# plot funksie
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', label='Data from .mat file')  # Blue line plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Data from .mat File')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
# %%
