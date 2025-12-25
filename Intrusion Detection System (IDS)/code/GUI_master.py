from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score,roc_curve
root = tk.Tk()
root.title("GUI")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

# image2 = Image.open('img2.jpg')

# image2 = image2.resize((w, h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)


# background_label = tk.Label(root, image=background_image)
# background_label.image = background_image
# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)




#background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Intrusion Detection ", font=('times', 35,' bold '), height=1, width=32,bg="blue",fg="white")
lbl.place(x=300, y=10)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
# data = pd.read_csv("Book1.csv")
# data = data.dropna()

# le = LabelEncoder()
def Data_Preprocessing():
    data = pd.read_csv("D:/final code/100% code Introsion detection/100% code Introsion detection/IDS_ML/training.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    
    #data['destination_Port'] = le.fit_transform(data['destination_Port'])
    data[' Flow_Duration'] = le.fit_transform(data[' Flow_Duration'])
    data[' Total_Fwd_Packets'] = le.fit_transform(data[' Total_Fwd_Packets'])
    data['Total_Backward_Packets'] = le.fit_transform(data['Total_Backward_Packets'])
    data['Total_Length_of_Fwd_Packets'] = le.fit_transform(data['Total_Length_of_Fwd_Packets'])
    data['Total_Length_of_Bwd_Packets'] = le.fit_transform(data['Total_Length_of_Bwd_Packets'])
    data[' Fwd_Packet_Length_Max'] = le.fit_transform(data[' Fwd_Packet_Length_Max'])
    data['Fwd_Packet_Length_Min'] = le.fit_transform(data['Fwd_Packet_Length_Min'])
    data[' Fwd_Packet_Length_Mean'] = le.fit_transform(data[' Fwd_Packet_Length_Mean'])
    data[' Fwd_Packet_Length_Std'] = le.fit_transform(data[' Fwd_Packet_Length_Std'])
    data['Bwd_Packet_Length_Max'] = le.fit_transform(data['Bwd_Packet_Length_Max'])
    data[' Bwd_Packet_Length_Min'] = le.fit_transform(data[' Bwd_Packet_Length_Min'])
    data[' Bwd_Packet_Length_Mean'] = le.fit_transform(data[' Bwd_Packet_Length_Mean'])
    data[' Bwd_Packet_Length_Std'] = le.fit_transform(data[' Bwd_Packet_Length_Std'])
    data['Flow_Bytes'] = le.fit_transform(data['Flow_Bytes'])
    data[' Flow_Packets'] = le.fit_transform(data[' Flow_Packets'])
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
  

    """Feature Selection => Manual"""
    x = data.drop(['Class'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=200, y=80)


def Model_Training():
    data = pd.read_csv("D:/final code/100% code Introsion detection/100% code Introsion detection/IDS_ML/training.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
 
    #data['destination_Port'] = le.fit_transform(data['destination_Port'])
    data[' Flow_Duration'] = le.fit_transform(data[' Flow_Duration'])
    data[' Total_Fwd_Packets'] = le.fit_transform(data[' Total_Fwd_Packets'])
    data['Total_Backward_Packets'] = le.fit_transform(data['Total_Backward_Packets'])
    data['Total_Length_of_Fwd_Packets'] = le.fit_transform(data['Total_Length_of_Fwd_Packets'])
    data['Total_Length_of_Bwd_Packets'] = le.fit_transform(data['Total_Length_of_Bwd_Packets'])
    data[' Fwd_Packet_Length_Max'] = le.fit_transform(data[' Fwd_Packet_Length_Max'])
    data['Fwd_Packet_Length_Min'] = le.fit_transform(data['Fwd_Packet_Length_Min'])
    data[' Fwd_Packet_Length_Mean'] = le.fit_transform(data[' Fwd_Packet_Length_Mean'])
    data[' Fwd_Packet_Length_Std'] = le.fit_transform(data[' Fwd_Packet_Length_Std'])
    data['Bwd_Packet_Length_Max'] = le.fit_transform(data['Bwd_Packet_Length_Max'])
    data[' Bwd_Packet_Length_Min'] = le.fit_transform(data[' Bwd_Packet_Length_Min'])
    data[' Bwd_Packet_Length_Mean'] = le.fit_transform(data[' Bwd_Packet_Length_Mean'])
    data[' Bwd_Packet_Length_Std'] = le.fit_transform(data[' Bwd_Packet_Length_Std'])
    data['Flow_Bytes'] = le.fit_transform(data['Flow_Bytes'])
    data[' Flow_Packets'] = le.fit_transform(data[' Flow_Packets'])
                                                                   
    
  

    """Feature Selection => Manual"""
    x = data.drop(['Class'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Class']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=10)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear',random_state=0)
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
   
    
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
    
    import seaborn as sns
    rf_false_positive_rate,rf_true_positive_rate,rf_threshold = roc_curve(y_test,y_pred)
    
    sns.set_style('whitegrid')
    plt.figure(figsize=(10,5))
    plt.title('Reciver Operating Characterstic Curve')
    
    plt.plot(rf_false_positive_rate,rf_true_positive_rate,label='Support Vector Machine',color='red')  
    plt.plot([0,1],ls='--',color='blue')
    plt.plot([0,0],[1,0],color='green')
    plt.plot([1,1],color='green')
    plt.ylabel('True positive rate')
    plt.xlabel('False positive rate')
    plt.legend()
    plt.show()

    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as svmmodel.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"svmmodel.joblib")
    print("Model saved as svmmodel.joblib")



def call_file():
    import Check_Prediction
    Check_Prediction.Train()
    





def window():
    root.destroy()

button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
button2.place(x=5, y=90)

# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Model Training", command=Model_Training, width=15, height=2)
# button3.place(x=5, y=170)

button4 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text=" detection", command=call_file, width=15, height=2)
button4.place(x=5, y=250)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=5, y=330)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''