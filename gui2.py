import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Assessment Form')
window.geometry('1900x960')


class design_gui_interface():
    def __int__(self, frame1):
        frame1 = ''

    def frames(self, x, y):
        self.frame1 = Frame(window, width=1100, height=900, border=0, bg='white')
        self.frame1.place(x=x, y=y)

    def header_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='white', font=('Algerian', 30, 'bold'))
        self.lbl.place(x=x, y=y)

    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='white', font=('Calibre', 12, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='white', font=('Calibre', 10))
        self.lbl.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='white')
        self.textbox.place(x=x, y=y)

    def button_design(self, x, y):
        self.upload_button = Button(width=15, pady=4, text='SEARCH', bg='red', fg='white', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)


# frames
my_gui_design = design_gui_interface()
my_gui_design.frames(250, 50)

# headers
heading = my_gui_design.header_design(550, 100, "SE-RI'S CHOICE PAYROLL")
employeebasicinfotxt = my_gui_design.heading_design(415, 180, 'EMPLOYEE BASIC INFO:')
employee_image = my_gui_design.image_design('C:\\Users\\admin\\PycharmProjects\\GUI\\user.jpg', 420, 210, 200, 200)

# labels
employeenumlbl = my_gui_design.label_design(420, 430, "Employee Number:")
searchlbl = my_gui_design.label_design(420, 470, "Search Employee:")
departmentlbl = my_gui_design.label_design(420, 510, "Department:")

firstnamelbl = my_gui_design.label_design(820, 210, 'Firstname:')
middlenamelbl = my_gui_design.label_design(820, 250, 'Middle Name:')
surnamelbl = my_gui_design.label_design(820, 290, 'Surname:')
civilstatuslbl = my_gui_design.label_design(820, 330, 'Civil Status:')
statuslbl = my_gui_design.label_design(820, 380, 'Qualified Dependents')
status2lbl = my_gui_design.label_design(820, 400, 'Status:')
paydatelbl = my_gui_design.label_design(820, 440, 'Paydate:')
empstatuslbl = my_gui_design.label_design(820, 490, 'Employee Status:')
designationlbl = my_gui_design.label_design(820, 540, 'Designation:')

# text boxes
employeenumtxt = my_gui_design.textbox_design1(565, 432)
buttontxt = my_gui_design.button_design(565, 468)
employeenumtxt = my_gui_design.textbox_design1(565, 512)

firstnametxt = my_gui_design.textbox_design1(965, 210)
middlenametxt = my_gui_design.textbox_design1(965, 254)
surnametxt = my_gui_design.textbox_design1(965, 290)
civilstatustxt = my_gui_design.textbox_design1(965, 330)
statustxt = my_gui_design.textbox_design1(965, 380)
paydatetxt = my_gui_design.textbox_design1(965, 440)
empstatustxt = my_gui_design.textbox_design1(965, 490)
designationtxt = my_gui_design.textbox_design1(965, 540)

window.mainloop()