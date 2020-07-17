import csv  
from matplotlib import pyplot as plt  
import numpy as np
import operator

filename='Stressed.csv' 
with open(filename) as f: #開啟這個檔案，並將結果檔案物件儲存在f中  
    reader = csv.reader(f)  #建立一個閱讀器reader
    count = 0
    stress_wife_data, stress_hosband_data=[],[]
    for row in reader:
        if count >=1:
            stress_wife_data.append(float(row[0]))
            stress_hosband_data.append(float(row[1]))
        count += 1
filename='NotStressed.csv' 

with open(filename) as f: #開啟這個檔案，並將結果檔案物件儲存在f中  
    reader = csv.reader(f)  #建立一個閱讀器reader
    count = 0
    notStress_wife_data, notStress_hosband_data=[],[]
    for row in reader:
        if count >=1:
            notStress_wife_data.append(float(row[0]))
            notStress_hosband_data.append(float(row[1]))
        count += 1

fig,axes=plt.subplots(2,2)
ax1=axes[0,0]
ax2=axes[0,1]
ax3=axes[1,0]
ax4=axes[1,1]
# fig=plt.figure(dpi=48,figsize=(10,6))  
ax1.plot(stress_wife_data, stress_hosband_data, 'ro', label = "Stressed") 
ax1.plot(notStress_wife_data, notStress_hosband_data, 'bx', label = "NotStressed") 
ax1.set_title('basic scatter plot',fontsize=10) 
ax1.set_xlabel('wife',fontsize=5)  
ax1.set_ylabel('hosband',fontsize=5)  
ax1.legend(loc = "upper right", fontsize=5)

#######################################################################
filename='Stressed.csv' 
with open(filename) as f: #開啟這個檔案，並將結果檔案物件儲存在f中  
    reader = csv.reader(f)  #建立一個閱讀器reader
    count = 0
    train_stress_wife_data, train_stress_hosband_data=[],[]
    test_stress_wife_data, test_stress_hosband_data=[],[]
    for row in reader:
        if count >=1 and count <= 100:
            train_stress_wife_data.append(float(row[0]))
            train_stress_hosband_data.append(float(row[1]))
        elif count > 100:
            test_stress_wife_data.append(float(row[0]))
            test_stress_hosband_data.append(float(row[1]))
        count += 1

filename='NotStressed.csv' 

with open(filename) as f: #開啟這個檔案，並將結果檔案物件儲存在f中  
    reader = csv.reader(f)  #建立一個閱讀器reader
    count = 0
    train_notStress_wife_data, train_notStress_hosband_data=[],[]
    test_notStress_wife_data, test_notStress_hosband_data=[],[]
    for row in reader:
        if count >=1 and count <= 100:
            train_notStress_wife_data.append(float(row[0]))
            train_notStress_hosband_data.append(float(row[1]))
        elif count > 100:
            test_notStress_wife_data.append(float(row[0]))
            test_notStress_hosband_data.append(float(row[1]))
        count += 1


ax2.plot(train_stress_wife_data, train_stress_hosband_data, 'ro', label = "Stressed") 
ax2.plot(train_notStress_wife_data, train_notStress_hosband_data, 'bx', label = "NotStressed") 
ax2.set_title('train',fontsize=10) 
ax2.set_xlabel('wife',fontsize=5)  
ax2.set_ylabel('hosband',fontsize=5)  
ax2.legend(loc = "upper right", fontsize=5)

ax3.plot(test_stress_wife_data, test_stress_hosband_data, 'ro', label = "Stressed") 
ax3.plot(test_notStress_wife_data, test_notStress_hosband_data, 'bx', label = "NotStressed") 
ax3.set_title('test',fontsize=10) 
ax3.set_xlabel('wife',fontsize=5)  
ax3.set_ylabel('hosband',fontsize=5)  
ax3.legend(loc = "upper right", fontsize=5)
# plt.show()  

##給出訓練資料以及對應的類別
dataset = []
labels = []
inputs = []
inputs_label = []
def create_dataset():
    for i in range(0, len(train_stress_wife_data)):
        dataset.append( [train_stress_wife_data[i], train_stress_hosband_data[i] ])

    for i in range(0, len(train_notStress_wife_data)):
        dataset.append( [train_notStress_wife_data[i],train_notStress_hosband_data[i] ])
    for i in range(0, len(train_stress_wife_data)):
        labels.append( 'stress')
    for i in range(0, len(train_notStress_wife_data)):
        labels.append( 'notStress')
    
    for i in range(0, len(test_stress_wife_data)):
        inputs.append( [test_stress_wife_data[i], test_stress_hosband_data[i] ])
    for i in range(0, len(test_notStress_wife_data)):
        inputs.append( [test_notStress_wife_data[i], test_notStress_hosband_data[i] ])
    for i in range(0, len(test_stress_wife_data)):
        inputs_label.append( 'stress')
    for i in range(0, len(test_notStress_wife_data)):
        inputs_label.append( 'notStress')
    

def classify(input, dataSet, label, k):
    classes =""
    dataSet = np.array(dataSet)
    dataSize = dataSet.shape[0]
    ## 重複input為dataSet的大小
    diff = np.tile(input, (dataSize, 1)) - dataSet
    sqdiff = diff**2
    ## 列向量分別相加，得到一列新的向量
    squareDist = np.array([sum(x) for x in sqdiff])
    dist = squareDist**0.5
    
    ## 對距離進行排序
    ## argsort()根據元素的值從大到小對元素進行排序，返回下標
    sortedDistIndex = np.argsort(dist)
    
    classCount = {}
    for i in range(k):
        ## 因為已經對距離進行排序，所以直接迴圈sortedDistIndx
        voteLabel = label[sortedDistIndex[i]]
        ## 對選取的k個樣本所屬的類別個數進行統計
        ## 如果獲取的標籤不在classCount中，返回0
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    ## 選取出現的類別次數最多的類別
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
    
    return classes

result_list = []
def inputClassify(inputs, k):
    result = 0
    for i in range(0, len(inputs_label)):
        # print(classify(inputs[i], dataset, labels, k))
        if (classify(inputs[i], dataset, labels, k) == inputs_label[i]):
            result += 1
    result_list.append(result/len(inputs_label))


create_dataset()

for i in range(2, 21):
    inputClassify(inputs, i) 
print(result_list)
ax4.plot([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], result_list, 'R', label = "Train") 
ax4.set_title('test',fontsize=10) 
ax4.set_xlabel('k',fontsize=5)  
ax4.set_ylabel('acc',fontsize=5)  
plt.show()  