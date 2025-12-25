from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from tkinter import ttk
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Intrusion Detection ")
    root.configure(background="LightSkyBlue")
    
    #Destination_Port= tk.IntVar()
    Flow_Duration = tk.IntVar()
    Total_Fwd_Packets= tk.IntVar()
    Total_Backward_Packets =  tk.IntVar()
    Total_Length_of_Fwd_Packets =  tk.IntVar() 
    Total_Length_of_Bwd_Packets =  tk.IntVar()
    Fwd_Packet_Length_Max =  tk.IntVar()
    Fwd_Packet_Length_Min =  tk.IntVar()
    Fwd_Packet_Length_Mean =  tk.IntVar()
    Fwd_Packet_Length_Std =  tk.IntVar()
    Bwd_Packet_Length_Max =  tk.IntVar()
    Bwd_Packet_Length_Min =  tk.IntVar()
    Bwd_Packet_Length_Mean =  tk.IntVar()
    Bwd_Packet_Length_Std=  tk.IntVar()
    Flow_Bytes =  tk.IntVar()
    Flow_Packets =  tk.IntVar()
      
    
    #===================================================================================================================


    def Detect():
        
       
       
        e1=Flow_Duration.get()
        print(e1)
        
        e2=Total_Fwd_Packets.get()
        print(e2)
        
        
        e3=Total_Backward_Packets.get()
        print(e3)
        
       
        e4=Total_Length_of_Fwd_Packets.get()
        print(e4)
        
        e5=Total_Length_of_Bwd_Packets.get()
        print(e5)
        
       
        e6=Fwd_Packet_Length_Max.get()
        print(e6)
        
        e7= Fwd_Packet_Length_Min.get()
        print(e7)
        
        e8=Fwd_Packet_Length_Mean.get()
        print(e8)
        
        e9= Fwd_Packet_Length_Std.get()
        print(e9)
        
        e10= Bwd_Packet_Length_Max.get()
        print(e10)
        
        e11=Bwd_Packet_Length_Min.get()
        print(e11)
        
        e12= Bwd_Packet_Length_Mean.get()
        print(e12)
        
        
        e13=Bwd_Packet_Length_Std.get()
        print(e13)
        
        e14=Flow_Bytes.get()
        print(e14)
        
        e15= Flow_Packets.get()
        print(e15)
        
      
      #########################################################################################
        
        from joblib import dump , load
        a1=load('introsion.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15]])
        print(v)
    
        if v[0]=='DDoS':
           print("DDoS ")
           yes = tk.Label(root,text="DDoS ",background="green",foreground="white",font=('times', 20, ' bold '),width=20)
           yes.place(x=600,y=600)
           
           
        if v[0]=='BENIGN':
           print("BENIGN ")
           yes = tk.Label(root,text="BENIGN",background="red",foreground="white",font=('times', 20, ' bold '),width=20)
           yes.place(x=600,y=600)

      
    
    l2=tk.Label(root,text="Flow_Duration",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l2.place(x=5,y=200)
    Flow_Duration=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Flow_Duration)
    Flow_Duration.place(x=500,y=200)
    
    
   
    
    l3=tk.Label(root,text="Total_Fwd_Packets",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l3.place(x=5,y=300)
    Total_Fwd_Packets=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Total_Fwd_Packets)
    Total_Fwd_Packets.place(x=500,y=300)
    
    l4=tk.Label(root,text="Total_Backward_Packets",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l4.place(x=5,y=350)
    Total_Backward_Packets=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Total_Backward_Packets)
    Total_Backward_Packets.place(x=500,y=350)


    
    l5=tk.Label(root,text="Total_Length_of_Fwd_Packets",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l5.place(x=5,y=400)
    Total_Length_of_Fwd_Packets=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Total_Length_of_Fwd_Packets)
    Total_Length_of_Fwd_Packets.place(x=500,y=400)

    
    
    l6=tk.Label(root,text="Total_Length_of_Bwd_Packets",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l6.place(x=5,y=450)
    Total_Length_of_Bwd_Packets=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Total_Length_of_Bwd_Packets)
    Total_Length_of_Bwd_Packets.place(x=500,y=450)
    
    l7=tk.Label(root,text="Fwd_Packet_Length_Max",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l7.place(x=5,y=500)
    Fwd_Packet_Length_Max=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Fwd_Packet_Length_Max)
    Fwd_Packet_Length_Max.place(x=500,y=500)
    
    
    l8=tk.Label(root,text="Fwd_Packet_Length_Min",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l8.place(x=700,y=50)
    Fwd_Packet_Length_Min=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Fwd_Packet_Length_Min)
    Fwd_Packet_Length_Min.place(x=1200,y=50)
    
   
    
    l9=tk.Label(root,text="Fwd_Packet_Length_Mean",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l9.place(x=700,y=100)
    Fwd_Packet_Length_Mean=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Fwd_Packet_Length_Mean)
    Fwd_Packet_Length_Mean.place(x=1200,y=100)
    
    l10=tk.Label(root,text="Fwd_Packet_Length_Std",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l10.place(x=700,y=150)
    Fwd_Packet_Length_Std=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Fwd_Packet_Length_Std)
    Fwd_Packet_Length_Std.place(x=1200,y=150)
    
    l11=tk.Label(root,text="Bwd_Packet_Length_Max",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l11.place(x=700,y=200)
    Bwd_Packet_Length_Max=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Bwd_Packet_Length_Max)
    Bwd_Packet_Length_Max.place(x=1200,y=200)
    
    l12=tk.Label(root,text="Bwd_Packet_Length_Min",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l12.place(x=700,y=250)
    Bwd_Packet_Length_Min=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Bwd_Packet_Length_Min)
    Bwd_Packet_Length_Min.place(x=1200,y=250)
    
    l13=tk.Label(root,text="Bwd_Packet_Length_Mean",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l13.place(x=700,y=300)
    Bwd_Packet_Length_Mean=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Bwd_Packet_Length_Mean)
    Bwd_Packet_Length_Mean.place(x=1200,y=300)
    
    l14=tk.Label(root,text="Bwd_Packet_Length_Std",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l14.place(x=700,y=350)
    Bwd_Packet_Length_Std=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Bwd_Packet_Length_Std)
    Bwd_Packet_Length_Std.place(x=1200,y=350)
    
    l15=tk.Label(root,text="Flow_Bytes",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l15.place(x=700,y=400)
    Flow_Bytes=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Flow_Bytes)
    Flow_Bytes.place(x=1200,y=400)
    
    l16=tk.Label(root,text="Flow_Packets",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l16.place(x=700,y=450)
    Flow_Packets=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Flow_Packets)
    Flow_Packets.place(x=1200,y=450)
   
    
    button1 = tk.Button(root, foreground="white", background="red",text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=600,y=650)


    root.mainloop()

Train()