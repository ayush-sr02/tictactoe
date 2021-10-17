from tkinter import *
import random
global img_o,img_x,canvas
main = Tk()
main.geometry('720x480')
main.resizable(0,0)
main.title('Tic Tac Toe')
img_o = PhotoImage(file='OO.gif')
img_x = PhotoImage(file='X.gif')
canvas = Canvas(main,height=100,width=100)
canvas = Canvas(main)
canvas.create_line(250,0,250,480,dash=(4,2),fill ='gray')
canvas.pack()
canvas1 = Canvas(main)
canvas1.create_line(250,1,250,300,dash=(4,2),fill ='gray')
canvas1.pack()

box = []
canvas_img = []

misc = []

identify = [[0,0,0],[0,0,0],[0,0,0]]
#print(*identify,sep='\n')

done = [1,2,3,4,5,6,7,8,9]

def bot(img=''):
    try:
        move = random.choice(done)
        coord = {1:[105,105],
                2:[195,105],
                3:[285,105],
                4:[105,195],
                5:[195,195],
                6:[285,195],
                7:[105,285],
                8:[195,285],
                9:[285,285]}
                
        '''for i in range(1000):
            move = random.randint(1,9)
            if move not in done:
                break'''
        
        if move==1:
            identify[0][0]=2
        elif move==2:
            identify[0][1]=2
        elif move==3:
            identify[0][2]=2
        elif move==4:
            identify[1][0]=2
        elif move==5:
            identify[1][1]=2
        elif move==6:
            identify[1][2]=2
        elif move==7:
            identify[2][0]=2
        elif move==8:
            identify[2][1]=2
        elif move==9:
            identify[2][2]=2
        
        main.update()
        box[move-1].destroy()

        done.remove(move)
        canvas = Canvas(main,height=90,width=90)
        canvas.create_image(0,0,image=img,anchor=NW)
        canvas.place(x=coord[move][0],y=coord[move][1])
        canvas_img.append(canvas)

    except:
        pass 

def status(stat='You Won',color='orange'):
    main.update()
    win = Label(main,text=stat,font=("",30),foreground=color)
    win.place(x =470 ,y = 200,height = 100,width =200)
    misc.append(win)
    
def check():
    global identify
    #print(*identify,sep='\n') 
    if (len(set(identify[0]))==1 and 1 in identify[0]) or (len(set(identify[1]))==1 and 1 in identify[1]) or (len(set(identify[2]))==1 and 1 in identify[2]) or (identify[0][0]==identify[1][0]==identify[2][0]==1) or (identify[0][1]==identify[1][1]==identify[2][1]==1) or (identify[0][2]==identify[1][2]==identify[2][2]==1) or (identify[0][0]==identify[1][1]==identify[2][2]==1) or (identify[0][2]==identify[1][1]==identify[2][0]==1):
        identify = [[0,0,0],[0,0,0],[0,0,0]]
        status('You Won','orange')

    elif (len(set(identify[0]))==1 and 2 in identify[0]) or (len(set(identify[1]))==1 and 2 in identify[1]) or (len(set(identify[2]))==1 and 2 in identify[2]) or (identify[0][0]==identify[1][0]==identify[2][0]==2) or (identify[0][1]==identify[1][1]==identify[2][1]==2) or (identify[0][2]==identify[1][2]==identify[2][2]==2) or (identify[0][0]==identify[1][1]==identify[2][2]==2) or (identify[0][2]==identify[1][1]==identify[2][0]==2):
        identify = [[0,0,0],[0,0,0],[0,0,0]]
        status('You Lost','red')
    elif len(done)==0:
        status('Draw','gray')

def xyz():
    global done

    try:
        for i in box:
            main.update()
            i.destroy()
        for i in canvas_img:
            main.update()
            i.destroy()
        for i in misc:
            i.destroy()
        done.clear()
        done = [1,2,3,4,5,6,7,8,9]
        
    
    except:
        pass

    def boxes(img):
        global img_o,img_x,canvas
        if img == img_o:
            bmg = img_x
        else:
            bmg = img_o
        main.update()
        choiceo.destroy()
        choicex.destroy()
        
        
        xx=105
        yy=105

        def f():
            canvas = Canvas(main,height=90,width=90)
            canvas.create_image(0,0,image=img,anchor=NW)
            canvas_img.append(canvas)
            check()
            return canvas

        def x1():
            box[0].destroy()
            identify[0][0]=1
            done.remove(1)
            canvas = f()
            canvas.place(x=105,y=105,height=90,width=90)
            bot(bmg)
        
        def x2():
            box[1].destroy()
            identify[0][1]=1
            done.remove(2)
            canvas = f()
            canvas.place(x=195,y=105,height=90,width=90)
            bot(bmg)
        def x3():
            box[2].destroy()
            identify[0][2]=1
            done.remove(3)
            canvas = f()
            canvas.place(x=285,y=105,height=90,width=90)
            bot(bmg)
        def y1():
            box[3].destroy()
            identify[1][0]=1
            done.remove(4)
            canvas = f()
            canvas.place(x=105,y=195,height=90,width=90)
            bot(bmg)
        def y2():
            box[4].destroy()
            identify[1][1]=1
            done.remove(5)
            canvas = f()
            canvas.place(x=195,y=195,height=90,width=90)
            bot(bmg)
        def y3():
            box[5].destroy()
            identify[1][2]=1
            done.remove(6)
            canvas = f()
            canvas.place(x=285,y=195,height=90,width=90)
            bot(bmg)
        def z1():
            box[6].destroy()
            identify[2][0]=1
            done.remove(7)
            canvas = f()
            canvas.place(x=105,y=285,height=90,width=90)
            bot(bmg)
        def z2():
            box[7].destroy()
            identify[2][1]=1
            done.remove(8)
            canvas = f()
            canvas.place(x=195,y=285,height=90,width=90)
            bot(bmg)
        def z3():
            box[8].destroy()
            identify[2][2]=1
            done.remove(9)
            canvas = f()
            canvas.place(x=285,y=285,height=90,width=90)
            bot(bmg)
            
        func = [[x1,x2,x3],[y1,y2,y3],[z1,z2,z3]]

        for i in range(3):
            for j in range(3):
                but = Button(main,command = func[i][j])
                but.place(x=xx,y=yy,height=90,width=90)
                #print(f'canvas.place(x={xx},y={yy},height=90,width=90)')
                xx+=90
                box.append(but)
                
            yy+=90
            xx=105

    def user_x():
        img = img_x
        boxes(img)

    def user_o():
        img = img_o
        boxes(img)

    choicex = Button(main,image=img_x,command = user_x)
    choicex.place(x=150,y=150,height=90,width=90)
    choiceo = Button(main,image=img_o,command = user_o)
    choiceo.place(x=250,y=150,height=90,width=90)

xyz()

again = Button(main,text='Again',command=xyz,font="Times 20 italic bold")
again.place(x =520 ,y = 400,height = 50,width =100 )

main.mainloop()
