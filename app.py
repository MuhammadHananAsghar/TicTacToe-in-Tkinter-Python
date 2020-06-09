'''
Muhammad Hanan Asghar
Data Scientist
TicTacToe App Project in Tkinter
Created on Jun 05,2020
Friday
'''
from tkinter import *
import tkinter.ttk as ttk
import time as t
from plyer import notification


bclicks = True



#############################FUNCTIONS########################
def action(buttons):
    global bclicks
    if buttons['text'] == " " and bclicks == True:
        buttons['text'] = "X"
        bclicks = False
    elif buttons['text'] == " " and bclicks == False:
        buttons['text'] = "O"
        bclicks = True
    if (btn_b1['text'] == "X" and btn_b2['text'] == "X" and btn_b3['text'] == "X" or
    btn_b4['text'] == "X" and btn_b5['text'] == "X" and btn_b6['text'] == "X" or
    btn_b7['text'] == "X" and btn_b8['text'] == "X" and btn_b9['text'] == "X" or 
    btn_b1['text'] == "X" and btn_b5['text'] == "X" and btn_b9['text'] == "X" or
    btn_b3['text'] == "X" and btn_b5['text'] == "X" and btn_b7['text'] == "X" or
    btn_b1['text'] == "X" and btn_b4['text'] == "X" and btn_b7['text'] == "X" or
    btn_b2['text'] == "X" and btn_b5['text'] == "X" and btn_b8['text'] == "X" or
    btn_b3['text'] == "X" and btn_b6['text'] == "X" and btn_b9['text'] == "X" ):
        # print("Player X Wins")
        lbl_win['text'] = "Player X Wins"
        notification.notify(
            title="TicTacToe By Muhammad Hanan",
            message="Congratulations Player X Wins",
        )
        return

        


    if (btn_b1['text'] == "O" and btn_b2['text'] == "O" and btn_b3['text'] == "O" or
    btn_b4['text'] == "O" and btn_b5['text'] == "O" and btn_b6['text'] == "O" or
    btn_b7['text'] == "O" and btn_b8['text'] == "O" and btn_b9['text'] == "O" or 
    btn_b1['text'] == "O" and btn_b5['text'] == "O" and btn_b9['text'] == "O" or
    btn_b3['text'] == "O" and btn_b5['text'] == "O" and btn_b7['text'] == "O" or
    btn_b1['text'] == "O" and btn_b4['text'] == "O" and btn_b7['text'] == "O" or
    btn_b2['text'] == "O" and btn_b5['text'] == "O" and btn_b8['text'] == "O" or
    btn_b3['text'] == "O" and btn_b6['text'] == "O" and btn_b9['text'] == "O" ):
        # print("Player X Wins")
        lbl_win['text'] = "Player O Wins"
        notification.notify(
            title="TicTacToe By Muhammad Hanan",
            message="Congratulations Player O Wins",
        )
        return
    
        

'''
Muhammad Hanan Asghar
Data Scientist
TicTacToe App Project in Tkinter
Created on Jun 05,2020
Friday
'''

root = Tk()
root.geometry("408x580")
root.title("TicTacToe By Muhammad Hanan")


########################FIRST FRAME###############################
first_frame = Frame(root,bg = "#8E44AD")
first_frame.place(x=0,y=0,width = 800,height = 160)

btn_b1 = Button(first_frame,text = " ",font=("lucida",15,"bold"),height=5,width = 10,command=lambda :action(btn_b1))
btn_b1.grid(row=0,column=0,padx=5,pady = 10)

btn_b2 = Button(first_frame,text = " ",font=("lucida",15,"bold"),height=5,width = 10,command=lambda:action(btn_b2))
btn_b2.grid(row=0,column=1,pady=5)

btn_b3 = Button(first_frame,text = " ",font=("lucida",15,"bold"),height=5,width = 10,command=lambda:action(btn_b3))
btn_b3.grid(row=0,column=2,padx=5,pady=5)
########################SECOND FRAME##############################
second_frame = Frame(root,bg = "#273746")
second_frame.place(x=0,y=161,width = 800,height = 160)

btn_b4 = Button(second_frame,text = " ",font=("lucida",15,"bold"),height=5,width = 10,command=lambda:action(btn_b4))
btn_b4.grid(row=0,column=0,padx=5,pady=10)

btn_b5 = Button(second_frame,text = " ",font=("lucida",15,"bold"),height=5,width = 10,command=lambda:action(btn_b5))
btn_b5.grid(row=0,column=1,pady=10)

btn_b6 = Button(second_frame,text = " ",font=("lucida",15,"bold"),height=5,width = 10,command=lambda:action(btn_b6))
btn_b6.grid(row=0,column=2,padx=5,pady=10)
########################THIRD FRAME#############################
third_frame = Frame(root,bg="#873600")
third_frame.place(x=0,y=322,width=800,height = 160)

btn_b7 = Button(third_frame,text = " ",font=("lucida",15,"bold"),height=5,width = 10,command=lambda:action(btn_b7))
btn_b7.grid(row=0,column=0,padx=5,pady=5)

btn_b8 = Button(third_frame,text = " ",font=("lucida",15,"bold"),height=5,width = 10,command=lambda:action(btn_b8))
btn_b8.grid(row=0,column=1,pady=10)

btn_b9 = Button(third_frame,text = " ",font=("lucida",15,"bold"),height=5,width = 10,command=lambda :action(btn_b9))
btn_b9.grid(row=0,column=3,padx=5,pady=10)

############################FRAME FOUR######################
fourth_frame = Frame(root,bg="#21618C")
fourth_frame.place(x=0,y=483,width=800,height=190)



lbl_win = Label(fourth_frame,text=" ",font=("lucida",20,"bold"),fg="white",bg="#21618C")
lbl_win.grid(row=0,column=0,padx=115,pady=30)
'''
Muhammad Hanan Asghar
Data Scientist
TicTacToe App Project in Tkinter
Created on Jun 05,2020
Friday
'''

root.mainloop()