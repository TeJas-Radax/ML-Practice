
# coding: utf-8

# In[10]:


#Linear Regression 
'''y = mx + b
   m is the slope and b is the y-intercept
   code for m and b
'''


from statistics import mean
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

class Linear_Regression():
    
    
    
    def fit(self,x,y):
        self.x=x
        self.m=( ( (mean(x)*mean(y)) - (mean(x*y)) ) / (((mean(x))**2)-(mean(x**2))) )
    
        self.b= mean(y) - self.m*(mean(x))
        
        #Calculation of Regression Line
        self.regression_line=[(self.m*x)+self.b for x in x_train]
        
        return self
    
    
    def predict(self,x_test): #prediction
        m=self.m
        b=self.b
        predict_y=[(self.m*x)+self.b for x in x_test]

        return predict_y
    
    def accuracy(self, x_test, y_test):
        pred_y=self.predict(x_test)
        y_test1=[j for j in y_test]
        acc=0
        noo=0
        for i in range(int(len(pred_y))):
            if abs(pred_y[i]-y_test1[i])<=(y_test1[i]-(y_test1[i]*0.8)) or abs(pred_y[i]-y_test1[i])>=(y_test1[i]+(y_test1[i]*0.8)):
                acc+=1
        return acc/int(len(pred_y))
    
    def plot(self,plot_x, plot_y, color='k'):
        plt.scatter(plot_x, plot_y, color=color)
        plt.plot(self.x,self.regression_line)
        plt.show()
    

#Testing Model
iris = pd.read_csv(r'C:\Users\TeJas\Desktop\Python Practice\Machine Learning\Data\iris data\iris.data.txt')
iris_data=iris['1']
iris_target=iris['2']
x_train, x_test, y_train, y_test = train_test_split(iris_data, iris_target, test_size=0.3, random_state=0)


clf=Linear_Regression()
clf.fit(x_train,y_train)
prd=clf.predict(x_test)
ac=clf.accuracy(x_test,y_test)
print(ac,prd)
clf.plot(x_test,y_test)

