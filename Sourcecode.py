import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree , DecisionTreeClassifier
import matplotlib.pyplot as plt 
from tkinter import *
import tkinter.ttk as ttk

def splitData(data):
    x = data.values[:, 1:13]
    y = data.values[:, 13]
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state=100)
 
    return x, y, xTrain, xTest, yTrain, yTest

    
def plotDecisionTree(forest, treeNumber, att, target):
    fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=800)
    plot_tree(forest.estimators_[treeNumber - 1],feature_names = att, class_names=target, filled = True);
    fig.savefig(f'tree_{treeNumber}.png')
    
def train(xTrain , yTrain):
    forest = RandomForestClassifier(n_estimators = 1000, criterion='gini', random_state = 100)
    forest.fit(xTrain , yTrain)
    return forest
def prediction(xTest, forest):
    yPred = forest.predict(xTest)
    return yPred

def calAccuracy(yTest, yPred):
    accuracy = accuracy_score(yTest, yPred) * 100
    return accuracy

def readData():
    data = pd.read_csv('bankloan.csv')
    return data
    
def main_event( window ):
    data = readData()
    print(data.shape)
    data.head()
    x, y, xTrain, xTest, yTrain, yTest = splitData(data)

    forest = train(xTrain, yTrain)
    temp = DoubleVar()
    if education.get() == "Diploma" :
        temp = 1
    elif education.get() == "Bachelor" :
        temp = 2
    elif education.get() == "Master&PHD" :
        temp = 3
    pred = prediction([[age.get() , experience.get() , income.get() , zipcode.get() , family.get() , credit_card_Average.get() , temp , morgage.get() , SecuritiesAccount.get() , CD_Account.get() , Online.get() , Credit_card.get()]] , forest)
    result = StringVar()
    if pred == 1 :
        result = "You will get loan"
    elif pred == 0 :
        result = "You will not get loan"
    else :
        result = "Error"
    
    yPred = prediction(xTest , forest)
    plotDecisionTree(forest, 5, ['Age', 'Experience' , 'Income' , 'ZIPCode' , 'Family' , 'CCAvg' , 'Education', 'Mortgage' , 'SecuritiesAccount' , 'CDAccount' , 'Online' , 'CreditCard'] , ['Not Ok' , 'OK'])
    colList = ['Age', 'Experience' , 'Income' , 'ZIPCode' , 'Family' , 'CCAvg' , 'Education', 'Mortgage' , 'SecuritiesAccount' , 'CDAccount' , 'Online' , 'CreditCard']
    importances = list(forest.feature_importances_)
    window.destroy()
    result_window = Tk()
    result_window.geometry( "%dx%d+%d+%d" % ( 650 , 300 , 300 , 50 ) )
    result_window.title("Result" )
    result_window.resizable(False,False)
    result_window.iconbitmap('icon.ico') 
    result_window.configure(background='white')
    Label(result_window, text = result , font = "Arial 25 bold" ).pack()
    Label(result_window, text = "Accuracy of Forest: {}".format(calAccuracy(yTest , yPred) ) , font = "Arial 25 bold" ).pack()
    i = 0
    for col in colList:
        Label( result_window , text= " Variable: {} : Importance: {}% ".format(colList[i] , round(importances[i] * 100 , 2))).pack()
        i = i + 1
    
window = Tk()
window.geometry( "%dx%d+%d+%d" % ( 850 , 550 , 300 , 50 ) )
window.title("Bank Loan" )
window.resizable(False,False)
window.iconbitmap('icon.ico') 
window.configure(background='white')
l1 = Label( window , text="Age" , justify = LEFT ,  font="tahoma 10 bold" , fg="black" , width=25  )
l1.place( x = 75 , y = 10  )
l2 = Label( window , text="Experience" , justify = LEFT , font="tahoma 10 bold" , fg="black" , width=25  )
l2.place( x = 75 , y = 50 )
l3 = Label( window , text="Income(K $)" , justify = LEFT , font="tahoma 10 bold" , fg="black" , width=25  )
l3.place( x = 75 , y = 95  )
l4 = Label( window , text="ZIPCode" , justify = LEFT , font="tahoma 10 bold" , fg="black" , width=25  )
l4.place( x = 75 , y = 135  )
l5 = Label( window , text="Family" , justify = LEFT , font="tahoma 10 bold" , fg="black" , width=25 )
l5.place( x = 75 , y= 170  )
l6 = Label( window , text="CCAvg" , justify = LEFT ,  font="tahoma 10 bold" , fg="black" , width=25  )
l6.place( x = 75 , y = 210  )
l7 = Label( window , text="Education" , justify = LEFT , font="tahoma 10 bold" , fg="black" , width=25  )
l7.place( x = 75 , y = 250 )
l8 = Label( window , text="Mortgage" , justify = LEFT , font="tahoma 10 bold" , fg="black" , width=25  )
l8.place( x = 75 , y = 290  )
l9 = Label( window , text="SecuritiesAccount" , justify = LEFT , font="tahoma 10 bold" , fg="black" , width=25  )
l9.place( x = 75 , y = 330  )
l10 = Label( window , text="CDAccount" , justify = LEFT , font="tahoma 10 bold" , fg="black" , width=25 )
l10.place( x = 75 , y= 370  )
l11 = Label( window , text="Online" , justify = LEFT , font="tahoma 10 bold" , fg="black" , width=25  )
l11.place( x = 75 , y= 410 )
l12 = Label( window , text="CreditCard" , justify = LEFT , font="tahoma 10 bold" , fg="black" , width=25 )
l12.place( x = 75 , y= 450 )

age = IntVar()
a1 = ttk.Combobox( window , textvariable=age )
var1 = []
for i in range( 1,65) :
    var1.append(i)
a1["value"]=var1
a1.current(18)
a1.place( x = 450 , y = 10 )

experience = IntVar()
experience1 = ttk.Combobox( window , textvariable=experience )
var2 = []
for i in range( 1,46) :
    var2.append(i)
experience1["value"]=var2
experience1.current(8)
experience1.place( x = 450 , y = 50 )

income = IntVar()
income1 = Scale( window , from_= 1 , to=999 , orient="horizontal" , activebackground="black" , cursor="dot" , length=500 , variable=income)
income1.place( x=300 , y = 85 )

zipcode = StringVar()
zipcode1 = Entry( window , textvariable=zipcode , font="tahoma 14 normal " , width=20 )
zipcode1.place( x=450 , y = 130 )

family = IntVar()
family1 = ttk.Combobox( window , textvariable=family )
var3 = []
for i in range( 1,10) :
    var3.append(i)
family1["value"]=var3
family1.current(2)
family1.place( x = 450 , y = 170 )

credit_card_Average = DoubleVar()
cca = Entry( window , textvariable=credit_card_Average , font="tahoma 14 normal" , width=10 )
cca.place( x=450 , y=210 )

education = StringVar()
education1 = ttk.Combobox( window , textvariable=education)
education1["value"] = ("Diploma","Bachelor","Master&PHD")
education1.current(1)
education1.place( x = 450 , y = 250 )
    
    
morgage = IntVar()
mr = Entry( window , textvariable=morgage , font="tahoma 14 normal" , width=10 )
mr.place( x=450 , y=290 )

SecuritiesAccount = IntVar()
r1 = Radiobutton( window , text="Yes" , variable=SecuritiesAccount , value=1 ) 
r2 = Radiobutton( window , text="No" , variable=SecuritiesAccount , value=0 ) 
r1.place( x=450 , y = 330 )
r2.place( x=500 , y = 330 )

CD_Account = IntVar()
r1 = Radiobutton( window , text="Yes" , variable=CD_Account , value=1 ) 
r2 = Radiobutton( window , text="No" , variable=CD_Account , value=0 ) 
r1.place( x=450 , y = 370 )
r2.place( x=500 , y = 370 )

Online = IntVar()
r1 = Radiobutton( window , text="Yes" , variable=Online , value=1 ) 
r2 = Radiobutton( window , text="No"  , variable=Online , value=0 ) 
r1.place( x=450 , y = 410 )
r2.place( x=500 , y = 410 )

Credit_card = IntVar()
r1 = Radiobutton( window , text="Yes" , variable=Credit_card , value=1 ) 
r2 = Radiobutton( window , text="No"  , variable=Credit_card , value=0 ) 
r1.place( x=450 , y = 450)
r2.place( x=500 , y = 450)

b = Button( window , text="Confirm Data" , width=10  , command= lambda : main_event( window )  )
b.pack(side="bottom" , pady=20 )
window.mainloop()