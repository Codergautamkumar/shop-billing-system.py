from ast import Delete
from cgitb import text
from distutils.cmd import Command
from re import search
from tkinter import *
from tkinter import ttk
from tkinter import font
from turtle import bgcolor, width
from PIL import Image,ImageTk #pip install pillow
import random,os
from tkinter import messagebox
import tempfile

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")


        #============Variables=========
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        # Product Categories list
        self.Category=("Select Option","Clothing","LifeStyle","Mobiles")


        # SubCatClothing
        self.SubCatClothing=("Pant","T-Shirt","Shirt")
        self.pant=("Levis","Mufti","Spykar")
        self.price_levis=5000
        self.price_mufti=7000
        self.price_spykar=8000


        self.T_shirt=("Polo","Roadstar","Jack&Jones")
        self.price_polo=1500
        self.price_Roadstar=1800
        self.price_Jackjones=1700


        self.Shirt=("Peter England","Louis Phillips","Park Avenue")
        self.price_Peter=2100
        self.price_Louis=2700
        self.price_Park=1740

        
        # SubCatLifeStyle
        self.SubCatLifeStyle=("Bath Soap","Face Cream","Hair Oil")
        self.Bath_soap=("Lifeboy","Lux","Santoor","Pearl")
        self.price_life=float(25)
        self.price_lux=20
        self.price_santoor=28
        self.price_pearl=30


        self.Face_creame=('Fair&lovely','Ponds','Olay','Garnier')
        self.price_fair=30
        self.price_ponds=65
        self.price_olay=30
        self.price_garnier=70


        self.Hair_oil=('Parachute','Jashmin','Bajaj')
        self.price_para=25
        self.price_jashmin=22
        self.price_bajaj=30


        # SubCatMobiles
        self.SubCatMobiles=("Iphone","Sumsung","Xiome","RealMe","One+")
        self.Iphone=('IphoneX','Iphone_11','Iphone_12')
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=85000


        self.Sumsung=('Sumsung M16','Sumsung M12','Sumsung M21')
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000


        self.Xiome=('Red11','Redme-12','RedmePro')
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000


        self.RealMe=('RealMe 12','RealMe 13','RealMe Pro')
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000


        self.OnePlus=('OnePlus1','OnePlus2','OnePlus3')
        self.price_one1=45000
        self.price_one2=60000
        self.price_one3=45800


        #image-1-----

        img=Image.open("image/img3.jpg")
        img=img.resize((500,300),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)


        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=460,height=130)


        #image-2-----


        img_1=Image.open("image/pic3.1.jpg")
        img_1=img_1.resize((500,300),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)


        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=460,y=0,width=500,height=130)


        #image-3-----

        img_2=Image.open("image/pic3.jpg")
        img_2=img_2.resize((520,300),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)


        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=960,y=0,width=520,height=130)


        lbl_title=Label(self.root,text="SHOAPING BILLING SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1530,height=45)


        Main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_frame.place(x=0,y=175,width=1530,height=620)


        #Customer LabelFrame

        Cust_Frame=LabelFrame(Main_frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)


        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)


        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)


        self.lblCustName=Label(Cust_Frame,font=("arial",10,"bold"),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)


        self.textCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.textCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.lblEmail=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)


        self.textEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.textEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        # Product LabelFrame

        Product_Frame=LabelFrame(Main_frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)


        # Category

        self.lblCategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Select Categories",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)


        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial",10,"bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


        # Subcategory

        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="SubCategory",bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)


        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[" "],state="readonly",font=('arial',10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)


        # Product Name

        self.lblproduct=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)


        self.Comboproduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=("arial",10,"bold"),width=24)
        self.Comboproduct.grid(row=2,column=1,sticky=W,padx=5,pady=5)
        self.Comboproduct.bind("<<ComboboxSelected>>",self.price)


        # price

        self.lblPrice=Label(Product_Frame,font=("arial",12,'bold'),bg="white",text="Price",bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)


        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=("arial",10,"bold"),width=24)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)


        # Qty

        self.lblQty=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)


        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)


        # Middel Frame--

        MiddleFrame=Frame(Main_frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)


        #image-1-----

        img12=Image.open("image/pic4.jpg")
        img12=img12.resize((490,340),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)


        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=490,height=340)

        #image-2-----

        img_13=Image.open("image/pic3.1.jpg")
        img_13=img_13.resize((490,340),Image.ANTIALIAS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)


        lbl_img_13=Label(MiddleFrame,image=self.photoimg_13)
        lbl_img_13.place(x=490,y=0,width=490,height=340)


        # Search

        Search_Frame=Frame(Main_frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=15,width=500,height=40)


        self.lblBill=Label(Search_Frame,font=("arial",10,"bold"),fg="white",bg="red",text="Bill Number")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1,pady=0)


        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial",8,"bold"),width=20)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2,pady=0)


        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",8,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        # right side bill aria Frame

        RightLabelFram=LabelFrame(Main_frame,text="Bill Aria",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFram.place(x=1000,y=45,width=350,height=355)


        scroll_y=Scrollbar(RightLabelFram,orient=VERTICAL)
        self.textarea=Text(RightLabelFram,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)


        # Bill Counter

        Bottom_Frame=LabelFrame(Main_frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=400,width=1520,height=125)


        self.lblSubTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Sub Total",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)


        self.EntySubTotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"), textvariable=self.sub_total,width=24)
        self.EntySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)


        self.lbl_tax=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="GOV. Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)


        self.txt_tax=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"), textvariable=self.tax_input,width=24)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.lblAmountTotal=Label(Bottom_Frame,font=("arial",12,"bold"),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)


        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"), textvariable=self.sub_total,width=24)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        #Button Frame

        Btn_Frame=Frame(Bottom_Frame,bd=2,bg='white')
        Btn_Frame.place(x=320,y=0)


        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,text="Add To Cart",font=("arial",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)


        self.Btngenerate_bill=Button(Btn_Frame,command=self.gen_bill,text="Generate Bill",font=("arial",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,text="Save Bill",font=("arial",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,text="Print",font=("arial",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,text="Clear",font=("arial",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,text="Exit",font=("arial",12,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]


    #======================Function Declaration===================


    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome Gaurav mini Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")


        self.textarea.insert(END,"\n====================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n====================================\n")

    
    def AddItem(self):
        print("Function .... Test @123")
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the product name")
        else:
             self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
             self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
             self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
             self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

            # (((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100))) # Total
            # ((((sum(self.l)) - (self.prices.get()))*Tax)/100) # Tax
            # (sum(self.l)) # Sub Total






    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","please add to cart product")

        else:
              text=self.textarea.get(10.0,(10.0+float(len(self.l))))
              self.welcome()
              self.textarea.insert(END,text)
              self.textarea.insert(END,"\n ============================")
              self.textarea.insert(END,f"\n Sub Ammount:\t\t\t{self.sub_total.get()}")
              self.textarea.insert(END,f"\n Tax Ammount:\t\t\t{self.tax_input.get()}")
              self.textarea.insert(END,f"\n Total Ammount:\t\t\t{self.total.get()}")
              self.textarea.insert(END,"\n==============================")


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved successfully")
            f1.close


    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
              if i.split('.')[0]==self.search_bill.get():
                    f1=open(f'bills/{i}','r')
                    self.textarea.delete(1.0,END)
                    for d in f1:
                          self.textarea.insert(END,d)
                    f1.close()
                    found="yes"
        if found=='no':
              messagebox.showerror("Error","Invalid Bill No.")


    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()



    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)


        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)


        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)


    def Product_add(self,event=""):
        print("Function For Product Adition.....")
        if self.ComboSubCategory.get()=="Pant":
            self.Comboproduct.config(value=self.pant)
            self.Comboproduct.current(0)


        if self.ComboSubCategory.get()=="T-Shirt":
            self.Comboproduct.config(value=self.T_shirt)
            self.Comboproduct.current(0)


        if self.ComboSubCategory.get()=="Shirt":
            self.Comboproduct.config(value=self.Shirt)
            self.Comboproduct.current(0)


        # Lifestyle

        if self.ComboSubCategory.get()=="Bath Soap":
            self.Comboproduct.config(value=self.Bath_soap)
            self.Comboproduct.current(0)


        if self.ComboSubCategory.get()=="Face Cream":
            self.Comboproduct.config(value=self.Face_creame)
            self.Comboproduct.current(0)


        if self.ComboSubCategory.get()=="Hair Oil":
            self.Comboproduct.config(value=self.Hair_oil)
            self.Comboproduct.current(0)


        # Mobile

        if self.ComboSubCategory.get()=="Iphone":
            self.Comboproduct.config(value=self.Iphone)
            self.Comboproduct.current(0)    


        if self.ComboSubCategory.get()=="Sumsung":
            self.Comboproduct.config(value=self.Sumsung)
            self.Comboproduct.current(0)    


        if self.ComboSubCategory.get()=="Xiome":
            self.Comboproduct.config(value=self.Xiome)
            self.Comboproduct.current(0)    

        if self.ComboSubCategory.get()=="RealMe":
            self.Comboproduct.config(value=self.RealMe)
            self.Comboproduct.current(0)    

        if self.ComboSubCategory.get()=="One+":
            self.Comboproduct.config(value=self.OnePlus)
            self.Comboproduct.current(0)    


    def price(self,event=""):
        # Pant

        if self.Comboproduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)    


        if self.Comboproduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        
        # T-Shirt


        if self.Comboproduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_polo)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Roadstar":
            self.ComboPrice.config(value=self.price_Roadstar)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_Jackjones)
            self.ComboPrice.current(0)
            self.qty.set(1)


        # Shirt

        if self.Comboproduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Louis Phillips":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1)
        


        # bath Soap
        
        
        if self.Comboproduct.get()=="Lifeboy":
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0)
            self.qty.set(1) 


        if self.Comboproduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Pearl":
            self.ComboPrice.config(value=self.price_pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Fair&lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_para)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Jashmin":
            self.ComboPrice.config(value=self.price_jashmin)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="IphoneX":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Sumsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Sumsung M12":
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Sumsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Red11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="Redme-12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="RedmePro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="RealMe 12":
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="RealMe 13":
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="RealMe Pro":
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="OnePlus1":
            self.ComboPrice.config(value=self.price_one1)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="OnePlus2":
            self.ComboPrice.config(value=self.price_one2)
            self.ComboPrice.current(0)
            self.qty.set(1)


        if self.Comboproduct.get()=="OnePlus3":
            self.ComboPrice.config(value=self.price_one3)
            self.ComboPrice.current(0)
            self.qty.set(1)


        

        

       





  

        







    








if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
