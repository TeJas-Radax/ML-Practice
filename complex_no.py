import math

class complex_number():


    def __init__(self,real,img):
        self.real=real
        self.img=img
        #print("{}+{}i".format(real,img))

    def addNo(num1,num2):
        re1=num1.real+num2.real
        img1=num1.img+num2.img
        return complex_number(re1,img1)



    def subNo(num1,num2):
        re1 = num1.real - num2.real
        img1 = num1.img - num2.img
        return complex_number(re1, img1)

    def mulNo(num1,num2):
        x_real=( (num1.real*num2.real)+(num1.img*num2.img)*(-1) )
        x_img=( (num1.real*num2.img)+(num2.real*num1.img) )
        return complex_number(x_real,x_img)


    def absNo(num1):

        x=math.sqrt((num1.real**2)+(num1.img**2))
        return (x)


    def ConjugateNo(num1):
        return complex_number(num1.real,(num1.img)*(-1))

    def Args(num1):
        z=math.atan((num1.img/num1.real))
        return z

