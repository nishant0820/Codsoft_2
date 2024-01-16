from tkinter import *
from tkinter import ttk,messagebox
import time

class Calculator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Calculator | Nishant Gupta")
        self.root.config(bg="black")
        
        #-------- title ----------------
        title=Label(self.root,text="Calculator",font=("times new roman",40,"bold"),bg="#010c48",fg="white",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #----------- clock -------------
        self.lbl_clock=Label(self.root,text="Date: DD-MM-YYYY\t\t\t\t\t\t\t\t\t\t\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #------------ calculator frame -----------------
        self.var_cal_input=StringVar()
        
        Cal_Frame=Frame(self.root,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=550,y=250,width=268,height=300)
        
        self.txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        self.txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(Cal_Frame,text="7",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input(7)).grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text="8",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input(8)).grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text="9",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input(9)).grid(row=1,column=2)
        btn_add=Button(Cal_Frame,text="+",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input('+')).grid(row=1,column=3)
        
        btn_4=Button(Cal_Frame,text="4",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input(4)).grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text="5",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input(5)).grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text="6",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input(6)).grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text="-",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input('-')).grid(row=2,column=3)
        
        btn_1=Button(Cal_Frame,text="1",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input(1)).grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text="2",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input(2)).grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text="3",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input(3)).grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text="*",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input('*')).grid(row=3,column=3)
        
        btn_0=Button(Cal_Frame,text="0",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input(0)).grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text="C",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=self.clear).grid(row=4,column=1)
        btn_div=Button(Cal_Frame,text="/",font=("arial",14,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=lambda:self.get_input('/')).grid(row=4,column=2)
        btn_eq=Button(Cal_Frame,text="=",font=("arial",15,"bold"),bd=1,width=4,pady=10,cursor="hand2",command=self.perform).grid(row=4,column=3)
        
        
        self.update_date_time()
        
    #------------------ functions -------------------------
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Date: {str(date_)}\t\t\t\t\t\t\t\t\t\t\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)
        
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear(self):
        self.var_cal_input.set('')
        
    def perform(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
        
if __name__=="__main__":
    root=Tk()
    obj=Calculator(root)
    root.mainloop()