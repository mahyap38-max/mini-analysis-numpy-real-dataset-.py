import numpy as np

data=np . genfromtxt('winequality-white.csv',delimiter=";",skip_header=1)

#print(data.dtype) #float64

#print(data.shape) #(4898 , 12 )

#print(data.ndim) #2 

#print(data.size) #58776

#print(np.mean(data[:,-1])) #5.87790935075541 mean quality
#print(np.max(data[:,-1]))  #9 max quality
#print(np.min(data[:,-1]))  #3 min quality

#print(np.mean(data[:,-2])) #10.514267047774602  mean alcohol
#print(np.max(data[:,-2]))  #14.2   max alcohol
#print(np.min(data[:,-2]))  #8     min alcohol
#print(np.std(data[:,-1]))  #0.8855481621683543 standard deviation of alcohol


#print(np.mean(data[:,-4])) #3.1882666394446715    mean ph


features=data[:,:-1]
quality=data[:, -1]

#print(np.sum(quality > 5 )) #3258 The number of wines with quality greater than 5

print(np.sum(data[:,-2]> 10))