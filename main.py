import pyttsx3
from tkinter import *

# engine = pyttsx3.init()
# engine.setProperty("rate", 160)
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)
# engine.say("Hi My Name Is SIRI")
# engine.runAndWait()

def sendCommand():
    awnserEntry.delete(0, END)
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    userCommand = askQuestionEntry.get()
    
    if "hi" in userCommand.lower():
        awnserEntry.insert(END," Hi How Are You?")
        engine.say("Hello There")
    if "how are you" in userCommand.lower():
        awnserEntry.insert(END," I'm Good Thanks")
        engine.say("I'm Good Thanks")
     
        
        
    engine.runAndWait()
        
    
def volumeUp():
    pass
def volumeDown():
    pass


root = Tk()
root.geometry("400x150")
root.config(bg='#121212')
root.resizable(0,0)

askQuestionEntry = Entry(root, bg='#121212', fg='white', width=30)
askQuestionButton = Button(root, bg='#121212', fg='white', command=sendCommand, text='Ask Question', width=15)
awnserEntry = Entry(root, bg='#121212', fg='white', width=30)
volumeUpButton = Button(root, bg='#121212', fg='white', command=volumeUp, text='Turn Volume Up', width=15)
volumeDownButton = Button(root, bg='#121212', fg='white', command=volumeDown, text='Turn Volume Down', width=15)

askQuestionEntry.grid(row=0, column=0, padx=20, pady=(20,0))
askQuestionButton.grid(row=0, column=1, padx=20, pady=(20,0))
awnserEntry.grid(row=1, column=0, padx=20, pady=(20,0))
volumeUpButton.grid(row=1, column=1, padx=20, pady=(10,0))
volumeDownButton.grid(row=2, column=1, padx=20, pady=(10,0))

root.mainloop()