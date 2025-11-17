#Importing
import os
from pprint import pprint
from PIL import Image,ImageTk
from googletrans  import Translator ,LANGUAGES
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as tkscrolled
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

#Creating tk window and hiding it
root=tk.Tk()
root.withdraw()

#Defining home page as function for other pages
home=None
def Home():

    #Checking if other windows are open or not
    if (pg1 is not None) and pg1.winfo_exists():
        pg1.withdraw()
    if (pg2 is not None) and pg2.winfo_exists():
        pg2.withdraw()
    
    #Size,icon and title of  home page
    global home
    home=Toplevel()
    home.geometry("500x500")
    home.title('Interpres')
    home.iconbitmap("assets/icon.ico")
    home.resizable(False,False)
    
    #Background of home page
    C = Canvas(home,width=500,height=500,borderwidth=0,bd=0 )
    Pic=PhotoImage(file=r"assets\A1.png")
    C.create_image(0,1,anchor=NW,image=Pic)
    C.pack(expand=YES,fill=BOTH)

    #Heading
    homeName=C.create_text(260,40,text='Interpres....', font=('Dancing Script',40,),fill="white")

    #Buttons
    TexttransBtn=Button(home,text="Translate Text",font=('PTSans-Regular',15),bd=6,command=transtext,relief=FLAT)
    C.create_window(250,220,window= TexttransBtn)
    FiletransBtn=Button(home,text="Translate Files",font=('PTSans-Regular',15),bd=6,command=transfile,relief=FLAT)
    C.create_window(250,330,window=FiletransBtn)

    home.mainloop()

#Defining command for translate text
pg1=None
def transtext():
    
    #Checking if other windows are open or not
    if (pg2 is not None) and pg2.winfo_exists():
        pg2.withdraw()
    if (home is not None) and home.winfo_exists():
        home.withdraw()

    #Size,icon and title of  page 1
    global pg1
    pg1=Toplevel()
    W1, H1= pg1.winfo_screenwidth(), pg1.winfo_screenheight()
    pg1.geometry("%dx%d+0+0" % (W1, H1))
    pg1.title('Interpres')
    pg1.iconbitmap("assets/icon.ico")
    pg1.resizable(True,True)

    #Background of pg1
    C1 = Canvas(pg1,width=W1, height=H1,borderwidth=0,bd=0 )
    Pic1= PhotoImage(file=r"assets/B1.png")
    C1.create_image(0,1,anchor=NW,image=Pic1)
    C1.pack(expand=YES, fill=BOTH)

    #Language Values for pg1
    lang_values = list(LANGUAGES.values())
    langs = [i.capitalize() for i in lang_values]

    #Heading of pg1
    pg1Name=C1.create_text(670,40,text='Interpres....', font=('Dancing Script',50,),fill="white")

    #Labels
    Langtotrans=C1.create_text(180,140,text='Text to be translated:',font=("PTSans-Regular",15),fill="white")
    transLang=C1.create_text(840,140,text='Translated Text:', font=('PTSans-Regular',15),fill="white")

    #Source Language button
    srcLang=ttk.Combobox(pg1,values=langs,font=('PTSans-Regular',10),state="readonly")
    srcLang.current(21)
    C1.create_window(390,140,window=srcLang)

    #Display Language button
    destLang=ttk.Combobox(pg1,values=langs,font=('PTSans-Regular',10),state="readonly")
    destLang.current(38)
    C1.create_window(1050,140,window=destLang)

    #Source Languge text
    sourceText=tkscrolled.ScrolledText(pg1,font=("PTSans-Regular",12),height=20,width=60,wrap=WORD,fg="white",bd=4,bg="#07173D",insertbackground='white')
    sourceText.pack(side=LEFT)
    C1.create_window(350,350,window=sourceText)

    #Translated text
    transText=tkscrolled.ScrolledText(pg1,font=("PTSans-Regular",12),height=20,width=60,wrap=WORD,fg="white",bd=4,bg="#07173D",insertbackground='white')
    transText.pack(side=LEFT)
    C1.create_window(1020,350,window=transText)

    #Defining function for button
    def Transfunc():
        translator = Translator()
        try:
            translated=translator.translate(text= sourceText.get(1.0, END) ,dest = destLang.get().lower(), src = srcLang.get().lower() )
            transText.delete(1.0, tk.END)
            transText.insert(tk.END, translated.text)
        except:
            Msg=messagebox.showinfo("Interpres...", "Enter text and try again.")

    #Translate Button
    TranslateBtn=Button(pg1,text="Translate",font=('PTSans-Regular',15),command=Transfunc,bd=4,bg="#07173D",fg="white")
    C1.create_window(670,600,window=TranslateBtn)

    #Home btn in pg1
    homebtn=Button(pg1,text="  Home  ",font=('PTSans-Regular',15),command=Home,bd=4,bg="#07173D",fg="white")
    C1.create_window(70,650,window=homebtn)

    #Translate file btn in pg1
    transfile_btn=Button(pg1,text="Translate files",font=('PTSans-Regular',15),command=transfile,bd=4,bg="#07173D",fg="white")
    C1.create_window(1270,650,window=transfile_btn)
    
    pg1.mainloop()

# Defining command for translating files
pg2= None
def transfile():
    
    #Checking if other windows are open or not
    if (pg1 is not None) and pg1.winfo_exists():
        pg1.destroy()
    if (home is not None) and home.winfo_exists():
        home.withdraw()

    #Size,icon and title of page 2
    global pg2
    pg2=Toplevel()
    pg2.geometry("600x600")
    pg2.title('Interpres')
    pg2.iconbitmap("assets/icon.ico")
    pg2.resizable(False,False)
    
    #Background of pg2
    C2 = tk.Canvas(pg2,width=600, height=600,borderwidth=0,bd=0 )
    pic2=PhotoImage(file=r"assets\C1.png")
    C2.create_image(0,1,anchor=NW,image=pic2)
    C2.pack(expand=YES, fill=BOTH)

    #Heading of pg2
    pg2Name=C2.create_text(300,40,text='Interpres....', font=('Dancing Script',35,),fill="white")

    #Language Values for pg2
    langvalues = list(LANGUAGES.values())
    Langs = [i.capitalize() for i in langvalues]

    #Labels of pg 2
    Sourcelang=C2.create_text(90,150,text='Source Language :-', font=('PTSans-Bold',13),fill="white")
    Targetlang=C2.create_text(90,225,text='Target Language :-', font=('PTSans-Regular',13),fill="white")
    filename=C2.create_text(100,300,text='File to be translated :-', font=('PTSans-Regular',13),fill="white")

    #Combo boxes of pg2
    SrcLang=ttk.Combobox(pg2,values=Langs,font=('PTSans-Regular',10),state="readonly")
    SrcLang.current(21)
    C2.create_window(290,150,window=SrcLang)

    DestLang=ttk.Combobox(pg2,values=Langs,font=('PTSans-Regular',10),state="readonly")
    DestLang.current(38)
    C2.create_window(290,225,window=DestLang)
    
    #Function for browsing
    def browse():
        global file_path
        file_path =filedialog.askopenfilename( filetypes =[("Text Files","*.txt")])
        display_filepath=Text(pg2,font=('PTSans-Regular',13),width=50,height=1)
        display_filepath.pack(side=LEFT)
        C2.create_window(250,350,window=display_filepath)
        display_filepath.delete(1.0, tk.END)
        display_filepath.insert(tk.END, file_path)     
        
    #Button for browsing
    BrowseBtn=Button(pg2,text="          Browse          ",font=('PTSans-Regular',10),bd=0,command=browse)
    C2.create_window(290,300,window= BrowseBtn)

    #Button for home page
    home_button=Button(pg2,text="   Home   ",font=('PTSans-Regular',15),bd=0,command=Home)
    C2.create_window(70,560,window= home_button)
    
    #Button for translate text
    translate_text=Button(pg2,text="Translate text",font=('PTSans-Regular',15),bd=0,command=transtext)
    C2.create_window(510,560,window= translate_text)

    #Defining function for translating files
    def transfile_func():
        try:
            reader = open(file_path,"r",encoding='utf-8')
            file_name,file_extension=os.path.splitext(file_path)
            try:
                read=reader.read()
                words = read.split()
                if len(words)<2500:
                    try:
                        translator = Translator()
                        Translated=translator.translate(text=read ,dest = DestLang.get().lower(), src = SrcLang.get().lower())
                        
                        #Creating a message box
                        msgbox=messagebox.showinfo("Interpres...", "The file has been translated.")
                        fileposition=filedialog.asksaveasfilename( filetypes =[("Text Files","*.txt")])
                        try:
                            file = open(fileposition , 'x',encoding="utf-8")
                            file.write(Translated.text)
                            file.close()
                            filecreation=messagebox.showinfo("Interpres...", "The file has been created.")
                        except FileNotFoundError:
                            msginfo=messagebox.showinfo("Interpres...", "Please try again.")
                    except TypeError:
                        msg_info=messagebox.showinfo("Interpres...", "The selected file is empty. Please try again.")
                else:
                    wordlimt=messagebox.showinfo("Interpres...", "Sorry,we can translate upto 15,000 words only.")
            finally:
                reader.close()
        except:
            msg=messagebox.showinfo("Interpres...", "Please select a file and proceed.")
            
    #Button for translation (pg2)
    filetransBtn=Button(pg2,text="Start translating",font=('PTSans-Regular',14),bd=0,command=transfile_func)
    C2.create_window(290,425,window= filetransBtn)

    pg2.mainloop()

#Displaying home screen
Home()

#Looping the entire program
root.mainloop()
