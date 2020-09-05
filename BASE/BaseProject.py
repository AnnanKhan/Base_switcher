from graphics import *
from base10ton import *
from basento10 import *

def answer(number__,number_base__,to_base__):
    ans__ = base10_to_n(base_n_to_base_10(number__,number_base__),to_base__)
    return(ans__)

def main():
    win = GraphWin("BASE PROJECT", 600, 230)

    text1 = Text(Point(100,70),"Number to be converted:")
    text1.draw(win)
    input_number_1 = Entry(Point(100, 100), 10)
    input_number_1.draw(win)



    text2 = Text(Point(300,70),"Base of that number:")
    text2.draw(win)
    input_base_number_1 = Entry(Point(300,100),10)
    input_base_number_1.draw(win)

    text3 = Text(Point(500,70),"In base:")
    text3.draw(win)
    input_base_output  = Entry(Point(500,100),10)
    input_base_output.draw(win)

    win.getMouse()

    x = input_number_1.getText()
    y = input_base_number_1.getText()
    z = input_base_output.getText()

    text4 = Text(Point(100,200),"ANSWER:-"+"  "+answer(str(x),int(y),int(z)))
    text4.setTextColor(color_rgb(0,255,0))
    text4.setSize(20)
    text4.draw(win)

    win.getMouse()
    win.close()

main()

