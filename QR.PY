from cgitb import text
from struct import pack
from tkinter import *
from turtle import fillcolor, title, width
from PIL import ImageTk,Image
import qrcode

code = qrcode.QRCode(
    version=4,
    box_size=9,
    border=2
)
 
def qr_maker():
    com = domain.get()
    DNA.title('on it..')
    code.add_data(com)
    code.make(fit=True)
    pop = code.make_image(fill='green',back_color='yellow')
    pop.save('him.png')
    img = ImageTk.PhotoImage(Image.open("him.png"))
    panel = Label(DNA, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    DNA.title('DONE..')
    DNA.mainloop()
 
##########################################################

DNA = Tk()
DNA.title('MR.QR')
DNA.iconbitmap('C:\\Users\\abdul\\Documents')

can = Canvas(DNA,width=150, height=150)
can.pack()
can.create_window(50, 50 )

p1 = Label(DNA,text= 'ENTER DOMAIN', font=('Arial', 15)) 
p1.pack() 

domain = Entry(DNA, text = ' ENTER DOMAIN ', width=50)
domain.pack()

b1 = Button(DNA, text = ' hit me ', command=qr_maker)
b1.pack()

label1 = Label(DNA, text='path of qrcode ""him.png""').pack()
DNA.mainloop()