import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Lyceum Registration')
window.geometry('1520x900')
header = Frame(window, width=2000, height=100, bg='white')
header.place(x=0, y=0)


class design_gui_interface():
    def __int__(self, frame1):
        frame1 = ''

    def frames(self, x, y):
        self.frame1 = Frame(window, width=1100, height=160, border=0, bg='#FBF8EF')
        self.frame1.place(x=x, y=y)

    def heading_design(self, x, y, text_value):
        self.text_value = text_value
        self.heading = Label(text=text_value, fg='black', bg='white', font=('Arial', 30, 'bold'))
        self.heading.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white')
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=31, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='#FBF8EF', font=('Calibre', 10))
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y):
        self.upload_button = Button(width=15, pady=7, text='Choose File', bg='black', fg='white', cursor='hand2',
                                    border=0)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(window, image=self.bck_pic)
        self.lbl.place(x=x, y=y)


# displaying the frames create
# instantiation of the class
my_gui_design = design_gui_interface()

# call frames attribute within the class named as design_gui_interface
# call for frame 1
my_gui_design.heading_design(450, 20, 'LYCEUM REGISTRATION FORM')
my_gui_design.frames(200, 220)

# call for frame 2
my_gui_design.frames(200, 390)

# call for frame 3
my_gui_design.frames(200, 560)

# textbox in first frame
firstnametxt = my_gui_design.textbox_design1(440, 262)
middle_nametxt = my_gui_design.textbox_design1(x=649, y=262)
surnametxt = my_gui_design.textbox_design1(x=858, y=262)
surnametxt = my_gui_design.textbox_design1(1067, 262)
date_of_birthtxt = my_gui_design.textbox_design1(440, 330)
nationalitytxt = my_gui_design.textbox_design1(1067, 330)

# display in second frame
departmentxt = my_gui_design.textbox_design2(232, 500)
designationtxt = my_gui_design.textbox_design2(495, 500)
employee_statustxt = my_gui_design.textbox_design2(760, 500)
employee_numbertxt = my_gui_design.textbox_design2(1025, 500)
contact_numbertxt = my_gui_design.textbox_design2(232, 435)
email_addresstxt = my_gui_design.textbox_design2(495, 435)
other_social_mediatxt = my_gui_design.textbox_design2(760, 435)
socail_media_accounttxt = my_gui_design.textbox_design2(1025, 435)

# display in third frame
address_line1txt = my_gui_design.textbox_design2(232, 600)
address_line2txt = my_gui_design.textbox_design2(495, 600)
barrangaytxt = my_gui_design.textbox_design2(760, 600)
municipalitytxt = my_gui_design.textbox_design2(1025, 600)
pronvincetxt = my_gui_design.textbox_design2(232, 670)
zip_codetxt = my_gui_design.textbox_design2(760, 670)
countrytxt = my_gui_design.textbox_design2(495, 670)
picturepathtxt = my_gui_design.textbox_design2(1025, 670)

# textbox label for first frame
first_name_lbl = my_gui_design.label_design(440, 235, 'Firstname')
middle_namelbl = my_gui_design.label_design(650, 235, 'Middlename')
surnamelbl = my_gui_design.label_design(858, 235, 'Surname')
suffixlbl = my_gui_design.label_design(1067, 235, 'Suffix')
date_of_birthlbl = my_gui_design.label_design(440, 305, 'Date of Birth')
nationalitylbl = my_gui_design.label_design(1067, 305, 'Nationality')
civil_statuslbl = my_gui_design.label_design(858, 305, 'Civil Status')
genderlbl = my_gui_design.label_design(650, 305, 'Gender')

# text label for second frame
departmentlbl = my_gui_design.label_design(232, 410, 'Department')
designationlbl = my_gui_design.label_design(498, 410, 'Designation')
emp_statuslbl = my_gui_design.label_design(764, 410, 'Employee Status')
emp_numberlbl = my_gui_design.label_design(1030, 410, 'Employee Number')
emp_contact_numlbl = my_gui_design.label_design(232, 475, 'Contact Number')
emp_email_addlbl = my_gui_design.label_design(498, 475, 'Email Address')
emp_other_social_media_accountlbl = my_gui_design.label_design(764, 475, 'Other Social Media Account')
emp_social_media_accountlbl = my_gui_design.label_design(1030, 475, 'Social Media Account')

# text label for third frame
address_line1lbl = my_gui_design.label_design(232, 575, 'Address Line 1')
address_line2lbl = my_gui_design.label_design(495, 575, 'Address Line 2')
barrangaylbl = my_gui_design.label_design(760, 575, 'Baranggay')
municipalitylbl = my_gui_design.label_design(1025, 575, 'Municipality')
provincelbl = my_gui_design.label_design(232, 645, 'Province')
zip_codelbl = my_gui_design.label_design(498, 645, 'Zip Code')
countrylbl = my_gui_design.label_design(764, 645, 'Country')
picturepathlbl = my_gui_design.label_design(1024, 645, 'Picture Path of Uploaded Image')

# combobox creation
n = tk.StringVar()
combo_field = ttk.Combobox(window, width=30, textvariable=n)

# adding combobox drop down list
combo_field['values'] = (' Female', ' Male', ' Unidentified')
combo_field.place(x=649, y=330)
combo_field.current()

# adding combobox for civil status
# combobox creation
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width=30, textvariable=n)
combo_field1['values'] = (' Single', ' Married', ' Widow', ' Legally Seperated', ' Annulled')
combo_field1.place(x=858, y=330)
combo_field1.current()

# call image to display
uploaded_image = my_gui_design.image_design('C:\\Users\\admin\\PycharmProjects\\GUI\\lyc.jpg', 222, 110, 200, 180)

# call for the button and place under the image
uploadbutton = my_gui_design.button_design(263, 300)

window.mainloop()