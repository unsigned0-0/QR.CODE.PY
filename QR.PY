from tkinter import *
from turtle import fillcolor, title, width
from PIL import ImageTk,Image
from click import command
 
import qrcode
code = qrcode.QRCode(
    version=4,
    box_size=20,
    border=2
)


code.make(fit=True)
pop = code.make_image(fill='green',back_color='green')
pop.save('him.png')
def qr_maker():
    com = LINK
    com.config()
    code.add_data(com)
    
    
##########################################################
DNA = Tk()
DNA.title('MR.QR')
DNA.iconbitmap('C:\\Users\\abdul\\Documents')

can = Canvas()

p1 = Label(DNA, text= 'select path down her !!!' ,font=('Arial', 20))
LINK = Entry(DNA, width=50, command=com)
LINK.pack()

img = ImageTk.PhotoImage(Image.open('him.png'))
img1 = Label(image=img)
img1.pack()
label1 = Label(DNA, text='path of qrcode ""him.png""').pack()
DNA.mainloop()