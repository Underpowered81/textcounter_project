import matplotlib.pyplot as mt
import matplotlib.pyplot as plt
import numpy as np

a = input("Digite su primera palabra")
b = input("Digite su segunda palabra")
c = input("Digite su tercera palabra")
d = input("Digite su cuarta palabra")
e = input("Digite su quinta palabra")
f = input("Digite su sexta palabra")





x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title(a)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)
plt.title(b)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])


plt.subplot(2, 3, 3)
plt.plot(x,y)
plt.title(c)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)
plt.title(f)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)
plt.title(d)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.title(e)
plt.show()
