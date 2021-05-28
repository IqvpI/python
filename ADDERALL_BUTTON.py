#IMPORT PACKAGES
from tkinter import *
from tkinter import messagebox
from FUNCTIONS import *
import time
from BUTTONS_ALERT import *
import types


#PROCESS TIMER START
start_time = time.time()


def get_input():
    ddata=int(e_1.get())
    ddata_test = ddata

    # if val_user_input(ddata) == 'false':
    #     w_msg = 'PLEASE ENTER NUMERIC VALUES ONLY!!!'
    #     wrng_msg(w_msg)

    #CHECK IF INPUT NUMERIC
    if ddata == 0:
        w_msg = 'PLEASE ENTER NUMERIC VALUES ONLY!!!'
        wrng_msg(w_msg)

    #EMPTY ENTRY FORM ERROR MSG
    elif ddata is None:
        # IMPROPER ENTRY WARNING
        w_msg = 'PLEASE ENTER NUMERIC VALUES ONLY!!!'
        wrng_msg(w_msg)

    elif isinstance(ddata, str):
        #IMPROPER ENTRY WARNING
        w_msg = 'PLEASE ENTER NUMERIC VALUES ONLY!!!'
        wrng_msg(w_msg)

    else:
        # VALID INPUT
        print(ddata)
        root.quit()

#DOSE ENTRY FORM
root = Tk()
root.title('DOSE DOCUMENTATION')
#CENTER MSGBOX ON TOPLEVEL
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())


#EXIT & END PROCESS (CANCEL BUTTON)
def exitt():
    print('PROCESS CANCELLED!')
    #CANCEL BUTTON MSGBOX
    cancel_msg()

#LABEL_1
label_1=Label(root, text='ENTER DOSE (eg .5, 1, etc):').grid(row=0,column=0)

#ENTRY BUTTON & AUTO POPULATE ENTRY BOX
e_1=Entry(root)
e_1.insert(0, 1)
e_1.grid(row=2, column=2)

#ENTER BUTTON
button_enter = Button(root, text="ENTER", command=get_input).grid(row=3, column=2)


#QUIT BUTTON
button_quit = Button(root, text="EXIT", command=exitt).grid(row=3, column=0)


root.mainloop()


#USER DOSE QUANTITY ENTRY
ddata=e_1.get()
print("DOSE : " + ddata)


#COUNT LINES IN FILES
from FILE_LINE_COUNT import *
numlines = FILE_LINE_COUNT1('testfile.txt')
print("RECORDED ENTRIES : " + str(numlines))

#ADD DATA 2 FILE
from ADOSE_DOC import *
done=ADOSE_DOC1(ddata)

#PROCESS END TIME
end_time = time.time()
p_time = int(end_time - start_time)

#PROCESS COMPLETED MSGBOX
p_complete(p_time)
print('PROCESS COMPLETED! PROCESSING TIME : ' + str(p_time) + ' SECONDS!')