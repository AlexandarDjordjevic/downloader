import matplotlib.pyplot as plt
import numpy as np
plt.ion() ## Note this correction

fig, (ax1, ax2) = plt.subplots(2, 1)
# make a little extra space between the subplots
fig.subplots_adjust(hspace=0.5)

index=0
i = 0
x=list()
y=list()
y2=list()

while True:
    print("Temp y: {}", temp_y)
    temp_y2=np.random.random();
    if index > 30:
        index -= 1
        x.pop(0)
        y.pop(0)
        y2.pop(0)
    x.append(i);
    y.append(temp_y);
    y2.append(temp_y2);
    ax1.cla()
    plt.yscale('linear')
    ax1.plot(x, y);
    ax2.cla()
    ax2.plot(x, y2);
    i += 1
    index += 1
    plt.show()
    plt.pause(0.01) #Note this correction