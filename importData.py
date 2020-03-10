import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

x= []

paths=["B:\M.sc. Industrial IT and Automation\Hard & Soft sensors\Tutorial 5\Extracted Flow data\Annular\exp_33.anc","B:\M.sc. Industrial IT and Automation\Hard & Soft sensors\Tutorial 5\Extracted Flow data\Plug\exp_01.anc","B:\M.sc. Industrial IT and Automation\Hard & Soft sensors\Tutorial 5\Extracted Flow data\Slug\exp_03.anc","B:\M.sc. Industrial IT and Automation\Hard & Soft sensors\Tutorial 5\Extracted Flow data\Stratified\exp_36.anc","B:\M.sc. Industrial IT and Automation\Hard & Soft sensors\Tutorial 5\Extracted Flow data\Wavy\exp_50.anc"]

for path in paths:
    dataFile = open(path,"r")
    dataset=re.split(r"## frame ",dataFile.read())
    dataset.pop(0) #removes non unvanted data
    dataFile.close()
    for frame in dataset:  
        datapoints=re.findall(r"\D\d[.]\d\d\d",frame)
        frameData= []
        for data in datapoints:
            frameData.append(float(data))
        x.append(frameData)

z = np.linspace(1,x.__len__(),x.__len__())
y = x
plt.xlabel("z-axis")
plt.ylabel("Y-axis")
plt.title("Dataset")
for i in range(len(y[0])):
    plt.plot(z,[pt[i] for pt in y])
plt.legend()
plt.show()

#file.close()

