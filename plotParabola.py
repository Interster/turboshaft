#%%
import numpy as np
import matplotlib.pyplot as plt

# Create x values from -10 to 10
x = np.linspace(-10, 10, 100)

# Calculate y values for y = x² (standard parabola)
y = x**2

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', linewidth=2, label='y = x²')
plt.title('Parabola: y = x²', fontsize=14, fontweight='bold')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.show()