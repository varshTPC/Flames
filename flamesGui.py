from tkinter import *
from pygame import *

#main home window
win = Tk()
win.title('FLAMES') #title
win.geometry('1350x730') #geometry
win.configure(bg = '#FF2442') #background
win.iconbitmap(default = './iconflames.ico') #favicon

#music
mixer.init()
gamesounds = {}
gamesounds['worst'] = mixer.Sound("./worst.wav")
gamesounds['kiss'] = mixer.Sound("./kiss.wav")
gamesounds['worst'].play()

startMusic = Button(win, text = "Music On", font = ('arialblack', 13), fg = 'white', bg = '#5C33F6', activebackground = '#D62AD0', command = lambda : gamesounds['worst'].play())
startMusic.place(x = 350, y = 515)

stopMusic = Button(win, text = "Music Off", font = ('arialblack', 13), fg = 'white', bg = '#5C33F6', activebackground = '#D62AD0', command = lambda : gamesounds['worst'].stop())
stopMusic.place(x = 890, y = 515)

#title
titleLabel = Label(win, text = "WELCOME TO FLAMES", bg = '#FF2442')
titleLabel.config(font = ('chiller', 100))
titleLabel.place(x = 180, y = 10)

#homeimage
homePic = PhotoImage(file = "./homepic.png")
homePicLabel = Label(win, image = homePic)
homePicLabel.place(x = 460, y = 150)

#method for button in Flames window
def FLAMES():
    #input 2 names
    name1 = input1.get()
    name2 = input2.get()

    #working of flames
    for i in range(len(name1)):
        for j in range(len(name2)):
            if name1[i] == name2[j]:
                name1 = name1[:i] + "@" + name1[i+1:]
                name2 = name2[:j] + "@" + name2[j+1:]
                break
    count = 0
    for i in name1:
        if i != "@":
            count = count + 1
    for i in name2:
        if i != "@":
            count = count + 1
    f = "FLAMES"; global ans; ans = "";
    n = 0; i = 0;
    while ("F" in f) or ("L" in f) or ("A" in f) or ("M" in f) or ("E" in f) or\
            ("S" in f):
        if f[i] != "@":
                n = n + 1
        if n == count:
            ans = f[i]
            f = f[:i] + "@" + f[i+1:]
            n = 0
        if i == 5:
            i = 0
        else:
            i = i + 1
    #result window
    result = Tk()
    center(result)
    result.maxsize(width = 700, height = 500)
    result.title('RESULT')

    #result window music
    gamesounds['worst'].stop()
    gamesounds['kiss'].play()

    #canvas for result win
    canvas = Canvas(result, width = 750, height = 600, highlightthickness = 0)
    canvas.pack(fill = 'both', expand = True)

    #bg image for result win
    pic = PhotoImage(file = "./resultpic.png", master = result)
    result.pic = pic
    canvas.create_image(0, 0, image = pic, anchor = 'nw')
    
    #displaying the results
    if ans == "F":
            canvas.create_text(350, 80, text = "* FRIENDS *", font = ('algerian', 60), fill = 'black')
            canvas.create_text(340, 180, text = "  You truly are connected by heart!", font = ('algerian', 25), fill = 'black')
            canvas.create_text(355, 215, text = "I'm sure your friendship", font = ('algerian', 25), fill = 'black')
            canvas.create_text(353, 250, text = "will cherish more and more", font = ('algerian', 25), fill = 'black')
    elif ans == "L":
        canvas.create_text(350, 80, text = "* LOVE *", font = ('algerian', 60), fill = 'black')
        canvas.create_text(340, 180, text = "  Lucky You!!!", font = ('algerian', 25), fill = 'black')
        canvas.create_text(355, 215, text = "Made for each other, huh?", font = ('algerian', 25), fill = 'black')
        canvas.create_text(353, 250, text = "Your 'LOVE' will bloom and blossom!", font = ('algerian', 25), fill = 'black')
    elif ans == "A":
        canvas.create_text(350, 80, text = "* AFFECTION *", font = ('algerian', 60), fill = 'black')
        canvas.create_text(340, 180, text = "  Ooh La La!!!", font = ('algerian', 25), fill = 'black')
        canvas.create_text(355, 215, text = "Woah 'AFFECTION' is the word for your relation", font = ('algerian', 21), fill = 'black')
        canvas.create_text(353, 250, text = "True Affection resides in both of your hearts!", font = ('algerian', 21), fill = 'black')
    elif ans == "M":
        canvas.create_text(350, 80, text = "* MARRIAGE *", font = ('algerian', 60), fill = 'black')
        canvas.create_text(340, 180, text = "  Soulmates, huh?", font = ('algerian', 25), fill = 'black')
        canvas.create_text(355, 215, text = "You both are destined to be married!", font = ('algerian', 25), fill = 'black')
        canvas.create_text(345, 250, text = "Good Luck!!!", font = ('algerian', 25), fill = 'black')
    elif ans == "E":
        canvas.create_text(350, 80, text = "* ENEMIES *", font = ('algerian', 60), fill = 'black')
        canvas.create_text(340, 180, text = "  Oh No!!!", font = ('algerian', 25), fill = 'black')
        canvas.create_text(355, 215, text = "Sadly, you both may not get along very well...", font = ('algerian', 21), fill = 'black')
        canvas.create_text(345, 250, text = "Hope you bury the hatchet!", font = ('algerian', 25), fill = 'black')
    elif ans == "S":
        canvas.create_text(350, 80, text = "* SIBLINGS *", font = ('algerian', 60), fill = 'black')
        canvas.create_text(340, 180, text = "  Oh, Dear!!!", font = ('algerian', 25), fill = 'black')
        canvas.create_text(355, 215, text = "Side by side or miles apart,", font = ('algerian', 25), fill = 'black')
        canvas.create_text(345, 250, text = "You are 'SIBLINGS' connected by heart!", font = ('algerian', 25), fill = 'black')

    #try again method
    def try_again():
        gamesounds['kiss'].stop()
        result.destroy()
        input1.delete(0, END)
        input2.delete(0, END)
        input1.focus_set()
        gamesounds['worst'].play()
    def exit_result():
        gamesounds['kiss'].stop()
        result.destroy()
        play.destroy()
        gamesounds['worst'].play()
    #try again button
    tryagain = Button(result, text = 'TRY AGAIN', font = ('algerian', 20), bg = '#F38BA0', fg = 'black', activebackground = '#D62AD0', padx = 5, command = try_again)
    tryagain.place(x = 180, y = 295)

    #exit button
    exit2 = Button(result, text = 'EXIT', font = ('algerian', 20), bg = '#F38BA0', fg = 'black', activebackground = '#D62AD0', padx = 20, command = exit_result)
    exit2.place(x = 360, y = 295)
    
#methods for the home page buttons
#what is flames button
def center(root, w = 700, h = 500):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = int((ws/2) - (w/2))
    y = int((hs/2) - (h/2))
    root.geometry(f'{w}x{h}+{x}+{y}')
def whatIsFlames():
    global root
    global bg
    global bglabel
    root = Tk()
    root.title('WHAT IS FLAMES')
    center(root) #geometry
    root.configure(bg = '#000000') #background
    root.iconbitmap(default = 'iconflames.ico')
    root.maxsize(width = 700, height = 500)

    info = Label(root, justify = 'left', text = "Hi I'm V!!! Welcome to FLAMES !\n\nTake FLAMES test to know what kind of relationship you will fall with the other person!!!\
\n\nFLAMES stands for :- \n\n'F' - Friends\n\n'L' - Love\n\n'A' - Affection\n\n'M' - Marriage\
\n\n'E' - Enemies\n\n'S' - Siblings.\n\nLet's get started, Check your luck !!!\n", width = 700, height = 500, font = ('cooperblack', 13), fg = 'white', bg = 'black')
    info.pack()

#try your luck button
def playFlames():
    global play
    global name1
    global name2
    global input1
    global input2
    play = Tk()
    play.title('FLAMES') #title
    play.geometry('1350x730') #geometry
    play.configure(bg = '#FF2442') #background
    play.iconbitmap(default = 'iconflames.ico') #favicon

    #first name label
    l1 = Label(play, text = 'ENTER YOUR NAME', bg = '#5C33F6', fg = 'black')
    l1.configure(width = 30, height = 2, font = ('algerian', 18))
    l1.place(x = 455, y = 130)

    #second entry
    input2 = Entry(play, width = 20, font = ('timesnewroman', 20), relief = 'groove')
    input2.place(x = 525, y = 370)
            
    #second name label
    l2 = Label(play, text = 'ENTER THE OTHER NAME', bg = '#5C33F6', fg = 'black')
    l2.configure(width = 30, height = 2, font = ('algerian', 18))
    l2.place(x = 455, y = 290)

    #first entry
    input1 = Entry(play, width = 20, font = ('timesnewroman', 20), relief = 'groove')
    input1.focus_set()
    input1.bind('<Return>', lambda event: input2.focus_set())
    input1.place(x = 525, y = 210)

    #flames button
    flames = Button(play, text = 'FLAMES', font = ('algerian', 30), bg = '#5C33F6', activebackground = '#D62AD0', command = FLAMES)
    flames.place(x = 580, y = 450)

#3 buttons
#what is flames
flamesinfo = Button(text = 'What is FLAMES', fg = 'white', bg = '#5C33F6', activebackground = '#D62AD0', command = whatIsFlames)
flamesinfo.configure(width = 30, height = 1, font = ('stencil', 15))
flamesinfo.place(x = 461, y = 450)
 
#try your luck
playbut = Button(text = 'Try Your Luck', fg = 'white', bg = '#5C33F6', activebackground = '#D62AD0', command = playFlames)
playbut.configure(width = 30, height = 1, font = ('stencil', 15))
playbut.place(x = 461, y = 510)

#exit
def destroy():
    win.destroy()
    gamesounds['worst'].stop()
exitbut = Button(text = 'EXIT', fg = 'white', bg = '#5C33F6', activebackground = '#D62AD0', command = destroy)
exitbut.configure(width = 30, height = 1, font = ('stencil', 15))
exitbut.place(x = 461, y = 570)

win.mainloop()

