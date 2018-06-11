from graphics import *      

win = GraphWin("Hangman", 600, 600)
win.setBackground("yellow")
textEntry = Entry(Point(233,200),10)
textEntry.draw(win)
text = textEntry.getText()
testText = Text(Point(150,15), text)
testText.draw(win)

exitText = Text(Point(200,50), 'Click anywhere to quit')
exitText.draw(win)

win.getMouse()
win.close()
