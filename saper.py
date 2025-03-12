import tkinter as tk
import tkinter.font as tkFont
import functools
import tkinter.simpledialog as sd
from collections import deque
from random import randint

root = tk.Tk()
rows = sd.askinteger("Ustawienia", "Liczba wierszy:", initialvalue=15, minvalue=1,maxvalue=21)
cols = sd.askinteger("Ustawienia", "Liczba kolumn:", initialvalue=15, minvalue=1,maxvalue=38)
difficulty = sd.askinteger("Ustawienia", "Trudność (% bomb):", initialvalue=20, minvalue=1,maxvalue=99)
reveal = sd.askinteger("Ustawienia", "Odkryj puste pole:", initialvalue=1, minvalue=0,maxvalue=1)


def randTable(v,h,n,bomb = 9) :
    output = [[0 for _ in range(h)] for _ in range(v)]
    i = 0
    while (i < n) :
        x = randint(0,v-1)
        y = randint(0,h-1)

        if output[x][y] != bomb :
            output[x][y] = bomb
            i += 1
    return output

def saper(T,bomb = 9) :
    lx = len(T)
    for x in range(lx) :
        ly = len(T[x])
        for y in range(ly) :
            if T[x][y] == bomb :
                continue
            sum = 0
            for i in range(x-1,x+2) :
                if i < 0 or i > lx - 1 :
                    continue
                for j in range(y-1,y+2) :
                    if j < 0 or j > ly - 1 :
                        continue
                    if T[i][j] == bomb :
                        sum += 1
            T[x][y] = sum
    return T

def generate(vert,hor,dif,rev) :
    bomb = "@"
    number_of_bombs = int((vert * hor * dif) / 100)
    sap = saper(randTable(vert,hor,number_of_bombs))
    buttons = [[None for _ in range(hor)] for _ in range(vert)]
    colors = ["gray","limegreen","green","deepskyblue","steelblue","mediumblue","darkslateblue","darkorchid","darkmagenta","red"]
    uncovered = []
    defused = []
    gamestate = True

    
    root.title("Saper, pozostało " + str(number_of_bombs) + " bomb")
    

    def clear(a,b) :
        first = (a,b)
        Q = deque()
        Q.append(first)
        processed = []
        while Q :
            x,y = Q.popleft()
            t = sap[x][y]
            if t == 0 :
                t = ''
            buttons[x][y].config(text = t, state = "disabled", relief="sunken")
            uncovered.append((x,y))
            if sap[x][y] != 0 :
                continue
            for i in range(x-1,x+2) :
                if i < 0 or i >= vert :
                    continue
                for j in range(y-1,y+2) :
                    if j < 0 or j >= hor :
                        continue
                    if (i,j) not in Q and (i,j) not in processed :
                        processed.append((i,j))
                        Q.append((i,j))
                        
    def show_all() :
        nonlocal gamestate
        for x in range(vert) :
            for y in range(hor) :
                if sap[x][y] != 9 and (x,y) in uncovered :
                    continue
                buttons[x][y].config(state = "disabled", relief = "sunken")
                if sap[x][y] == 9 :
                    buttons[x][y].config(bg = "red")

        label = tk.Label(root, text="Game Over")
        font = tkFont.Font(size=20)
        label.config(font=font)
        label.grid(row=0, column=0, rowspan=vert, columnspan=hor)
        gamestate = False

    def clear_near(x,y) :
        bombs_near = 0
        
        for i in range(x-1,x+2) :
            if i < 0 or i >= vert :
                continue
            for j in range(y-1,y+2) :
                if j < 0 or j >= hor :
                    continue
                if (i,j) in defused :
                    bombs_near += 1
        # if bombs_near != sap[x][y] :
        #     return None
        
        for i in range(x-1,x+2) :
            if i < 0 or i >= vert :
                continue
            for j in range(y-1,y+2) :
                if j < 0 or j >= hor :
                    continue
                
                if (i,j) not in defused and (i,j) not in uncovered :
                    t = sap[i][j]
                    if t == 9 :
                        show_all()
                    if t == 0 :
                        t = ""
                        clear(i,j)
                    buttons[i][j].config(text = t,state = "disabled", relief = "sunken")
                    uncovered.append((i,j))

    def left_click(event,x,y):
        nonlocal gamestate
        if not gamestate or (x,y) in defused :
            return None
        place = sap[x][y]
        if (x,y) in uncovered and place != 0 :
            clear_near(x,y)
        if (x,y) not in uncovered :
            uncovered.append((x,y))
        if place == 9 :
            show_all()
        if event.widget["text"] != bomb :
            event.widget.config(text=place, state="disabled", relief="sunken")
            if place == 0 :
                clear(x,y)
        if ((len(defused) == number_of_bombs)) :
            winning = True
            for i in range(vert) :
                for j in range(hor) :
                    if (i,j) not in defused and sap[i][j] == 9 :
                        buttons[i][j].config(bg = "red")
                        winning = False
            if winning :
                label = tk.Label(root, text="Game Finished")
                font = tkFont.Font(size=20)
                label.config(font=font)
                label.grid(row=0, column=0, rowspan=vert, columnspan=hor)
                gamestate = False
            else :
                show_all()
        
    def right_click(event,x,y):
        nonlocal gamestate,number_of_bombs
        if not gamestate :
            return None
        if (x,y) in defused :
            event.widget.config(text="",disabledforeground = colors[sap[x][y]])
            defused.remove((x,y))
        elif (x,y) not in uncovered :
            event.widget.config(text = bomb, fg = "red",state = "disabled",disabledforeground = "red")
            if (x,y) not in defused :
                defused.append((x,y))
                bombs = number_of_bombs - len(defused)
                root.title("Saper, pozostało " + str(bombs) + " bomb")
        if ((len(defused) == number_of_bombs)) :
            winning = True
            for i in range(vert) :
                for j in range(hor) :
                    if (i,j) not in defused and sap[i][j] == 9 :
                        buttons[i][j].config(bg = "red")
                        winning = False
            if winning :
                label = tk.Label(root, text="Game Finished")
                font = tkFont.Font(size=20)
                label.config(font=font)
                label.grid(row=0, column=0, rowspan=vert, columnspan=hor)
                gamestate = False
            else :
                show_all()
    
    def first_reveal() :
        done = False
        while not done :
            first_x = randint(0,vert-1)
            first_y = randint(0,hor-1)

            if sap[first_x][first_y] == 0 :
                clear(first_x,first_y)
                done = True

    for i in range(vert):
        for j in range(hor):
            button = tk.Button(root, text="", width=2, height=1)
            color = colors[sap[i][j]]
            button.config(disabledforeground=color)
            button.grid(row=i, column=j)
            button.bind("<Button-1>", functools.partial(left_click, x=i, y=j))
            button.bind("<Button-3>",  functools.partial(right_click, x=i, y=j))
            buttons[i][j] = button

    if rev == 1 :
        first_reveal()

    
generate(rows,cols,difficulty,reveal)
root.mainloop()