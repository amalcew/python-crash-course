import matplotlib.pyplot as plt

x = list(range(1, 1001))
y = [x**2 for x in x]
plt.scatter(x, y, c=y, cmap=plt.cm.Reds, edgecolor='none', s=10)

plt.title("Squares", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.show()
