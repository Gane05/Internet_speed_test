from tkinter import *
import speedtest
sp = Tk()
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    k=sp.download()/1048576
    down = str(round(k,2))+' Mbps'
    up = str(round((sp.upload()/1048576),2))+' Mbps'
    ldt.config(text=down)
    lut.config(text=up)
    if k!=0:
        speedcount1 = '100 MB of a file  can be \n downloaded in ' + str(round(100 / k, 2)) + ' seconds'
    else:
        speedcount1 = 'YOUR INTERNET SPEED IS \n NILL'
    sc.config(text=speedcount1)
sp.title('internet speed test')
sp.geometry('600x650')
sp.config(bg='black')
lab = Label(sp, text='Your internet speed',font=('Times new roman', 30, 'bold'), bg='black', fg='red')
lab.place(x=140, y=40,height=40,width=400)
lab = Label(sp, text='Download speed',font=('Times new roman', 30, 'bold'), bg='black',fg='blue')
lab.place(x=140, y=100,height=40,width=400)
ldt = Label(sp, text='00', font=('Times new roman', 30, 'bold'), bg='black', fg='blue')
ldt.place(x=140, y=160, height=40, width=400)
lab = Label(sp, text='upload speed', font=('Times new roman', 30, 'bold'), bg='black', fg='blue')
lab.place(x=140, y=220, height=40, width=400)
lut = Label(sp, text='00', font=('Times new roman', 30, 'bold'), bg='black', fg='blue')
lut.place(x=140, y=280, height=40, width=400)
button = Button(sp, text='check', font=('Times new roman', 30, 'bold'), relief=RAISED, bg='red', fg='white', command=speedcheck)
button.place(x=140, y=380, height=40, width=400)
sc=Label(sp,text='',font=('Times new roman', 30, 'bold'), bg='black', fg='blue')
sc.place(x=60,y=480,height=80,width=540)


sp.mainloop()


