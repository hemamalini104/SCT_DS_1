import matplotlib.pyplot as plt
import numpy as np
ages = [22, 21, 25, 23, 22, 24, 26, 21, 24, 25, 22, 23, 24, 26, 27, 22, 23, 25]
plt.figure(figsize=(8, 6))
plt.hist(ages, bins=np.arange(20, 30), color='skyblue', edgecolor='black')
plt.title('Age Distribution', fontsize=15)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()
