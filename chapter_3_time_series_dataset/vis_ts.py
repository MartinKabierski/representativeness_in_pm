
from matplotlib import pyplot as plt
from sktime.datasets import load_from_tsfile

train_x, train_y = load_from_tsfile("Crop_TRAIN.ts", return_data_type="numpy2d")
print(train_y)
plt.rcParams['figure.figsize'] = [14, 6]

f, axis = plt.subplots(nrows=3, ncols=8, sharey="all", layout="constrained")
print(axis)
for y in range(1,25):
    x_relevant = []
    for idx,x in enumerate(train_x):
        if int(train_y[idx]) == y:
            x_relevant.append(x)
    [axis[(y-1)//8, (y-1)%8].plot(x, c="royalblue", alpha=.1, rasterized=True) for x in x_relevant]
    axis[(y - 1) // 8, (y - 1) % 8].set_xlabel("Class "+str(y), fontsize=16)
#plt.show()

plt.savefig("timeseries_classes.pdf", format="pdf")