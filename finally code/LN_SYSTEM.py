from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as sc
import os 
import time
import threading
import cv2
from pathlib import Path
import pygame
from PIL import Image, ImageTk
import requests
from cryptography.fernet import Fernet

# Initialize the key
key = Fernet.generate_key()

# Create the Fernet instance
f = Fernet(key)

root = Tk()
root.geometry('1000x800')
root.title(' File protection system ')
root.configure(background='BLACK')
root.iconbitmap('icone.ico')
image = Image.open("security_hacker_names.jpg")
image = image.resize((1600, 1200), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)

# إنشاء عنصر الكانفاس
canvas = Canvas(root, width=1600, height=1200)
canvas.pack()
# إضافة الصورة إلى الكانفاس كخلفية
canvas.create_image(0, 0, image=background_image, anchor=NW)

#============ Functions =========

def openfile ():
    global tf
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/Laith/Desktop/",
        title= 'open file',
        filetypes=(("Text Files ","*.txt"),
                    ("PDF File","*.pdf"),
                    ("Word File","*.docx"),
                    ("PowerPoint File","*.pptx"),
                    ("Excel File","*.xlsx"),
                    ("Access File","*.accdb"))
    )
    en1.insert(END,tf)
    global filesize1
    filesize1= os.path.getsize(tf)
    en2.insert(END,filesize1)

def secu():
    while True:
        new_path = tf
        size = os.path.getsize(new_path)
        if filesize1 == size:
            txt.insert('end','[✔]-','black')
            txt.insert('end','your file is safe ','green')
            txt.insert('end', time.ctime(),'black')
            txt.insert('end','\n\n')
            get_time = int(en3.get())
            time.sleep(get_time)
            continue
        else:
            txt.insert('end','[X]-','black')
            txt.insert('end','your file has been tampered with ' , 'red')
            txt.insert('end',time.ctime(),'black')
            txt.insert('end','\n--------------------\n')
            # التقاط صورة
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            desktop_path = str(Path.home() / "Desktop")
            cv2.imwrite(os.path.join(desktop_path, 'captured_image.jpg'), frame)
            cap.release()
            # تحديد مسار الملف الصوتي
            sound_path = os.path.join(os.path.dirname(__file__), "alarm.wav")

            # تحميل الملف الصوتي
            pygame.mixer.init()
            sound = pygame.mixer.Sound(sound_path)

            # تشغيل الصوت
            sound.play()
            # music - send email -message telegram

            token = '6130115090:AAF2NHJPqms3gaOK9LfQztK3dOSxzcj5VUg'
            groupId = 'programing4us2'
            msg = f'You Are Being Attacked'
            def sendMsg(message):
                url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{groupId}&text={message}'
                res = requests.get(url)
                if res.status_code==200:
                    print('Successfully sent')
                else:
                    print('ERROR: Could not send Message')
            sendMsg(msg)

            break

def go():
    threading.Thread(target=secu).start()

def encrypt_file(file_path):
    # Read the file data
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the file data
    encrypted_data = f.encrypt(file_data)

    # Write the encrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def encrypt_file_gui():
    # Prompt the user for the file to encrypt
    file_path = en1.get()

    # Encrypt the file
    encrypt_file(file_path)
    txt.insert('end', 'File encrypted successfully.\n', 'black')

#-------------------------------------------------------------------------------
def decrypt_file(file_path):
    # Read the encrypted file data
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the file data
    decrypted_data = f.decrypt(encrypted_data)

    # Write the decrypted data back to the file
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def decrypt_file_gui():
    # Prompt the user for the file to decrypt
    file_path = en1.get()

    # Decrypt the file
    decrypt_file(file_path)
    txt.insert('end', 'File decrypted successfully.\n', 'black')


#-------------------------------------------------------------------------------
#============= title top ==============
title = Label( root,
            text=" Welcome To",
            font= ('Courier',36),
            bg='#CDE460',
            fg='black'
            )
title.place(relx=0.001, rely=0.2, relwidth=0.44, height=50)
title2 = Label( root,
            text="LN System",
            font= ('Courier',36),
            bg='#CDE460',
            fg='black'
            )
title2.place(relx=0.58, rely=0.2, relwidth=0.45, height=50)
title3 = Label( root,
            text="xxxxxxxxxxxxxxxxxxxxxxxxxxx",
            font= ('Courier',20),
            bg='#CDE460',
            fg='black'
            )
title3.place(relx=0, rely=0.15, relwidth=0.4, height=2)

title4 = Label( root,
            text="xxxxxxxxxxxxxxxxxxxxxxxxxxx",
            font= ('Courier',20),
            bg='#CDE460',
            fg='black'
            )
title4.place(relx=0.7, rely=0.3, relwidth=0.4, height=2)

#================ image logo =========
# img = Image.open('py.png')
# img = img.resize((800, 300), Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(img)
# panel= Label(root, image=photo)
# panel.place(relx=0.25, rely=0.04, relwidth=0.5, relheight=0.3)

#================ Button load file =========

button= Button(root,
                text='Select File  ',
                width=37,
                height=2,
                cursor='hand2',
                fg='white',
                bg='black',
                bd=10,relief=RIDGE ,
                font=('Courier',18),
                command=openfile
                
                ) 
button.place(relx=0.01, rely=0.4, relwidth=0.3, height=50)

#================ Entry to path =========
en1= Entry(root,font=('Courier',15),bd=2,bg="black",fg="white")
en1.place(relx=0.35, rely=0.4, relwidth=0.3, height=40)
#================ Frame :label with entry =========
f2 =Frame(root,width=800,height=800,bg='white',bd=0,relief=GROOVE)
f2.place(relx=0.01, rely=0.6, relwidth=0.3, relheight=0.6)

L1 = Label (f2,text='    File Options :                          ',bg='#CDE460',fg='black',font=('Courier',15))
L1.place(relx=0, rely=0, relwidth=1, height=50)

L2 = Label (f2,text='File Size :',bg='#CDE460',fg='black',font=('Courier',14))
L2.place(relx=0.02, rely=0.15, relwidth=0.3, height=50)
en2 = Entry(f2,font=('Courier',13),justify=CENTER,bd=2)
en2.place(relx=0.35, rely=0.15, relwidth=0.3, height=50)

L3 = Label (f2,text='Set Time :',bg='#CDE460',fg='black',font=('courier',14))
L3.place(relx=0.02, rely=0.3, relwidth=0.3, height=50)
en3 = Entry(f2,font=('courier',13),justify=CENTER,bd=2)
en3.place(relx=0.35, rely=0.3, relwidth=0.3, height=50)


L4 = Label (f2,text='Start To Security Your File:',bg='white',fg='black',font=('courier',15))
L4.place(relx=0.1, rely=0.42, relwidth=0.8, height=50)

imgframe = PhotoImage(file='scan.png',width=2,height=2)

B1 =Button(f2, text= 'Start Scan ',
            cursor="hand2",image=imgframe,compound=LEFT,
            width=240,bd=10,relief=RIDGE,bg='black',fg='white',
            font=('Courier',18),
            command=go
            )
B1.place(relx=0.02, rely=0.5, relwidth=0.95, height=50)


button_encrypt= Button(root,
                text='Encrypt File  ',
                width=37,
                height=2,
                cursor='hand2',
                fg='white',
                bg='black',
                bd=10,relief=RIDGE ,
                font=('Courier',18),
                command=encrypt_file_gui)
                
button_encrypt.place(relx=0.01, rely=0.5, relwidth=0.3, height=50)


button_decrypt= Button(root,
                text='Decrypt File  ',
                width=37,
                height=2,
                cursor='hand2',
                fg='white',
                bg='black',
                bd=10,relief=RIDGE ,
                font=('Courier',18),
                command=decrypt_file_gui)
                
button_decrypt.place(relx=0.35, rely=0.5, relwidth=0.3, height=50)

#=============== text and scroll for results =======

txt = sc.ScrolledText (root,bg='whitesmoke')
txt['font']=('Courier','20')
txt.place(relx=0.35, rely=0.6, relwidth=0.6, relheight=0.396)
txt.tag_config('green',background='green',foreground='white')
txt.tag_config('black',background='white',foreground='black')
txt.tag_config('red',background='red',foreground='white')

root.mainloop()

