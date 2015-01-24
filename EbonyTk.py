from Tkinter import *
class Ebony (Frame):
def say_how (self):
 print "What a beautiful day"
 def createWidgets (self):
 self.Quit = Button(self)
 self.Quit["text"] = "Quit"
 self.Quit["fg"]   = "red"
 self.Quit["command"] = self.quit
 self.Quit.pack({"side": "left"})
 self.what_a = Button(self)
 self.what_a["text"] = 
