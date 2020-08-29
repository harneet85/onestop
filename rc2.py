
#from textwrap import fill
#from gtk._gtk import SIDE_LEFT
#from block.dmraidmodule import date
#from duplicity.globals import select
#from duplicity.selection import Select
#from distutils import command
#from GUI.test import CheckVar1
#from modules.mss import mss
#import pyscreenshot as ImageGrab
#import  PIL
#from modules import sudom

from Tkinter import *
import sys,os,datetime
import tkMessageBox
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),'modules'))

#from modules import *

from modules import sudopex
from modules import monitorpex
from modules import httppex
from modules import pre
from modules import healthpex
from modules import pdfpex
from modules import waspex
from modules import cmdbpex

class mypr():
    def __init__(self):
        print("Initiating program")
        root=Tk()
        root.wm_title("OneStop V2.0 by - Harneet Singh")
        root.columnconfigure(0, weight=1,uniform='a')
        root.columnconfigure(1, weight=1,uniform='a')
        
        nb_of_columns = 2
        root.geometry("400x400+500+200") 
        
#### HEADING       
        Label1=Label(root,text="""Welcome to program , created by Harneet, 
to fetch evidence for IBM DPS WAS Team""",bg="white",borderwidth=4,font=("Arial", 11))
        Label1.grid(row=1, column=0,sticky='news',columnspan=nb_of_columns)
        
        Label2=Label(root,text="Enviornment",bg="red",font=("Arial", 11))
        Label2.grid(row=3,column=0,sticky='news',)
        
        Label3=Label(root,text="Test",bg="blue",font=("Arial", 11))
        Label3.grid(row=3,column=1,sticky='news')

        variable = "some"

##### FUNCTION TO SET TEST
                
        def select_all():
            print(datetime.datetime.now())
            print("calling slect_all command")
            c1.select()
            c2.select()
            c3.select()
            c4.select()
            c5.select()
            c6.select()
            c7.select()
            
        def scod():
            print(datetime.datetime.now())
            print("calling scod command")
            c1.deselect()
            c2.deselect()
            c3.select()
            c4.deselect()
            c7.deselect()
            c6.deselect()
            c5.select()

        def b6():
            print(datetime.datetime.now())
            print("calling b6 command")
            c1.select()
            c2.select()
            c3.select()
            c4.select()
            c7.select()
            c6.select()
            c5.deselect()
            
        def checkRun():
            ee= v.get()
            if ( ee == 1 ):
                env="PR"
            elif ( ee == 2 ):
                env="ET"
            elif ( ee == 3 ):
                env="ST"
            elif ( ee == 4 ):
                env="DEV"
            
            b= var1.get()
            c=var2.get()
            d=var3.get()
            e=var4.get()
            f=var5.get()
            g=var6.get()            
            h=var7.get()
            print("host is :"+self.a.get())
            print("User is :"+self.e.get())
            print("PASS is :"+self.f.get())


            if (v.get() == 0 ):
                tkMessageBox.showinfo (title='inputs for S3', message="Please select ENV")
            else:
                print("running checkrun")
                print("Env is :"+env)
                pre.exe(self.a.get(),self.e.get(),self.f.get(),env)
                a1="value of ENV is  ",env
                a2="value of button1 is  ",b
 #               tkMessageBox.showinfo(message=a1+a2)
                print("variable V value : ", v.get())
                print("variable var1 value : ", var1.get())
                print("variable var2 value : ", var2.get())
                print("variable var3 value : ", var3.get())
                print("variable var4 value : ", var4.get())
                print("variable var5 value : ", var5.get())
                print("variable var6 value : ", var6.get())            
                print("variable var7 value : ", var7.get())  
                if(b==1):
                    print("Inside 1") ##sudo
                    sudopex.exe(self.a.get(),self.e.get(),self.f.get(),env)
  #                  sudom.sudo(self.a.get(),self.e.get(),self.f.get())
#                 print(self.e.get())
               #     print(self.f.get())
#                  im.show()
                if(c==1):
					print("Inside 2")
					if (env == "ST") or (env == "DEV"):
						print("Env is "+env+" hence not executing monitoring")
					else:
						monitorpex.exe()                    
                if(d==1):
					print("Inside 3")
					healthpex.exe()
                if(e==1):
					print("Inside 4")    
					httppex.exe()
                if(f==1):
					print("Inside 5")  
					pdfpex.exe()
                if(g==1):
                    print("Inside 6")
                    waspex.exe()					
                if(h==1):
					print("Inside 7")
					cmdbpex.exe()
			    
                exit()
                
#### BUTTONS TO CHOOSE MAIN TEST
        v = IntVar()

#        CHECKBUTTON11=Checkbutton(root,text="ALL",variable="var1",command=select_all,activebackground="red")
 #       CHECKBUTTON11.grid(row=4,column=1,sticky=W)
  #      CHECKBUTTON22=Checkbutton(root,text="SCOD", variable="var2", command=scod,activebackground="yellow").grid(row=5,column=1,sticky=W)
   #     CHECKBUTTON33=Checkbutton(root,text="B6", variable="var3", command=b6,activebackground="green").grid(row=6,column=1,sticky=W)
                
        b=Radiobutton(root, text="ALL", variable="var1",command=select_all,activebackground="red").grid(row=4,column=1)
        b=Radiobutton(root, text="SCOD", variable="var2", command=scod,activebackground="red").grid(row=5,column=1)       
        b=Radiobutton(root, text="B6", variable="var3", command=b6,activebackground="red").grid(row=6,column=1)                
               
                
#### BUTTON TO CHOOSE SUB TEST
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
      
                            
            
        c1=Checkbutton(root,text="SUDO", variable=var1)
        c1.grid(row=7,column=1,sticky=W)
        c2=Checkbutton(root,text="Monitor", variable=var2)
        c2.grid(row=8,column=1,sticky=W)
        c3=Checkbutton(root,text="HealthCheck", variable=var3)
        c3.grid(row=9,column=1,sticky=W)
        c4=Checkbutton(root,text="HTTP", variable=var4)
        c4.grid(row=10,column=1,sticky=W)
        c5=Checkbutton(root,text="PostInstallVersion", variable=var5)
        c5.grid(row=11,column=1,sticky=W)
        c6=Checkbutton(root,text="Sync", variable=var6)
        c6.grid(row=12,column=1,sticky=W)
        c7=Checkbutton(root,text="CMDB", variable=var7)
        c7.grid(row=13,column=1,sticky=W)

        
        

##### RADIO BUTTON TO CHOOSE ENV

        b=Radiobutton(root, text="PR", variable=v, value=1).grid(row=4,column=0)
        b=Radiobutton(root, text="ET", variable=v, value=2).grid(row=5,column=0)       
        b=Radiobutton(root, text="ST", variable=v, value=3).grid(row=6,column=0)
        b=Radiobutton(root, text="UT", variable=v, value=4).grid(row=7,column=0)
        
        Label4=Label(root,text="VM Name:",bg="purple",font=("Arial", 11))
        Label4.grid(row=8,column=0,sticky='ew')
        self.a=Entry()
        self.a.grid(row=9,column=0)

        
#### OTHER BUTTONS FOR USERNAME, VM NAME, PASS
        
        Label5=Label(root,text="UserName:",bg="yellow",font=("Arial", 11))
        Label5.grid(row=10,column=0,sticky='ew')
        self.e=Entry()
        self.e.grid(row=11,column=0)

        Label6=Label(root,text="Password:",bg="yellow",font=("Arial", 11))
        Label6.grid(row=12,column=0,sticky='ew')
        self.f=Entry()
        self.f.grid(row=13,column=0)
        
        Button1=Button(root,text="Submit",bg="pink",command=checkRun,font=("Arial", 15))
        Button1.grid(row=16,column=0,columnspan=nb_of_columns)
        
#        Frame1=Frame(root,bg="white",border=1,relief=GROOVE)
#        Frame1.grid(row=17,column=0,columnspan=2,rowspan=6,sticky=N+S)
#        Label7=Label(Frame1,text="Output",border=1)
#        Label7.grid()
        
#        w = Message(root, text="this is a message dsaf f dsf sdf dsa fsa fdsa ",bg="yellow", width=600)
#        w.grid(row=20, column=0,sticky='news',columnspan=nb_of_columns)
        
        root.mainloop()

        
        
### CALLING MAIN CLASS 

try:
    a=mypr()
except (RuntimeError, TypeError, NameError,UnboundLocalError):
    pass
else:
	pass