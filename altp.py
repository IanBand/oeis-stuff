import math
import matplotlib.pyplot as plt

range_ = range(0,200)
seq = []
s = 0
for i in range_:
    if i % 2 == 0:
        s += i
    else:
        s = s % i
    seq.append(s)

plt.scatter(range_, seq, 0.1)

#for i in range(0, 20):
#    print(str(seq[i]) + ','),
plt.show()

