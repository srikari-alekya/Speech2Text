
import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox

def speech2text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        txtSpeech.insert(tk.END, "Listening...\n")
        root.update() 
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            txtSpeech.insert(tk.END, text + "\n")
        except sr.UnknownValueError:
            txtSpeech.insert(tk.END, "Could not understand audio\n")
        except sr.RequestError as e:
            txtSpeech.insert(tk.END, "Error: {0}\n".format(e))
        except Exception as e:
            txtSpeech.insert(tk.END, "An error occurred: {0}\n".format(e))
def reset_txtSpeech():
    txtSpeech.delete("1.0",tk.END)
def exit_system():
    result=messagebox.askquestion("Exit System","Confirm if you want to exit?")
    if result=='yes':
        messagebox.showinfo("Goodbye","Good bye")
        root.destroy()

root = tk.Tk()
root.title("Speech to Text")

MainFrame = tk.Frame(root, bd=20, width=900, height=600)
MainFrame.pack()

lblTitle = tk.Label(MainFrame, font=('arial', 40, 'bold'), text="Speech to Text", width=18)
lblTitle.pack()

txtSpeech = tk.Text(MainFrame, font=('arial', 20, 'bold'), width=68, height=12)
txtSpeech.pack()

btnConvert = tk.Button(MainFrame, font=('arial', 20, 'bold'), text="Convert to Text", width=20, height=2, command=speech2text)
btnConvert.pack(side=tk.LEFT, padx=5)

btnReset = tk.Button(MainFrame, font=('arial', 20, 'bold'), text="Reset", width=18, height=2, command=reset_txtSpeech)
btnReset.pack(side=tk.LEFT, padx=5)

btnExit = tk.Button(MainFrame, font=('arial', 20, 'bold'), text="Exit", width=18, height=2, command=exit_system)
btnExit.pack(side=tk.LEFT, padx=5)

root.mainloop()
