import tkFileDialog
import tkMessageBox
import ttk
from Tkinter import *

from textblob import TextBlob

import keys


class MyTranslator:
    def __init__(self, master):
        self.master = master
        master.title("Tweet Translator")
        master.geometry("375x470")
        master.wm_iconbitmap('icon.ico')

        # THE THREE LABELS
        self.lb1 = Label(master, text="Set your tweet to be translated and posted")
        self.lb2 = Label(master, text="Select language and your image")

        # INPUT TEXTBOX
        self.text1 = Text(master, height=10, width=50, bg='#E3E3E3', insertborderwidth=2)

        # OUTPUT TEXTBOX
        self.text2 = Text(master, height=10, width=50, bg='#E3E3E3', insertborderwidth=2)

        # INPUT COMBOBOX LANGUAGE
        vars = ["English", "French", "Spanish", "German", "Italian", "Arabe", "Japones", "Hebreo"]
        self.cboxl = ttk.Combobox(master, width=8, values=vars)
        self.cboxl.current(0)

        # BUTTON LOAD IMAGE
        self.lfButton = ttk.Button(master, text="Load Image", command=self.cargar)
        self.lblImg = Label(master, width=13, bd=1, relief="solid", bg='#E3E3E3', font='Arial 14')
        self.myfiletypes = [('Python files', '*.png'), ('All files', '*')]
        self.open = tkFileDialog.Open(master, filetypes=self.myfiletypes)

        # ENTRY TEXT
        self.encount = ttk.Entry(master, width=3)
        self.lblcoun = Label(master, text="Characters")

        # BUTTONS
        self.tButton = ttk.Button(master, text="Translate", command=self.traducir)
        self.pButton = ttk.Button(master, text="Post", command=self.post)
        self.cButton = ttk.Button(master, text="Clear", command=self.limpiar)
        self.qButton = ttk.Button(master, text="Quit", command=self.salir)

        ############## POSICIONAMIENTO ##################

        # LABEL TITLE
        self.lb1.grid(row=0, columnspan=3)

        # INPUT TEXTBOX
        self.text1.grid(row=1, padx=8, columnspan=3)

        # LABEL LANGUAGE
        self.lb2.grid(row=2, columnspan=3)

        # COMBOBOXS LANGUAGE
        self.cboxl.grid(row=3, column=0, pady=5)

        # LOAD FILE SECCION
        self.lfButton.grid(row=3, column=1, pady=5)
        self.lblImg.grid(row=3, column=2, pady=5)

        # OUTPUT TEXTBOX
        self.text2.config(state=DISABLED)
        self.text2.grid(row=4, padx=8, columnspan=3)

        # ENTRY COUNT
        self.encount.config(state=DISABLED, justify=CENTER)
        self.encount.grid(row=6, column=1)
        self.lblcoun.grid(row=5, column=1)

        # BUTTONS
        self.tButton.grid(row=5, column=0, pady=5)
        self.pButton.grid(row=5, column=2, pady=5)
        self.cButton.grid(row=6, column=0)
        self.qButton.grid(row=6, column=2)

    @property
    def idioma(self):
        if self.cboxl.get() == "English":
            return "en"
        elif self.cboxl.get() == "French":
            return "fr"
        elif self.cboxl.get() == "Spanish":
            return "es"
        elif self.cboxl.get() == "German":
            return "de"
        elif self.cboxl.get() == "Italian":
            return "it"
        elif self.cboxl.get() == "Arabe":
            return "ar"
        elif self.cboxl.get() == "Japones":
            return "ja"
        elif self.cboxl.get() == "Hebreo":
            return "he"

    # Function load image
    def cargar(self):
        self.lblImg.config(text=self.open.show())

    # function to translate
    def traducir(self):
        try:
            blob = TextBlob(self.text1.get("1.0", "end-1c"))
            text_blob = blob.translate(to=self.idioma)
            self.encount.config(state=NORMAL)
            self.encount.insert(INSERT, len(text_blob))
            self.encount.config(state=DISABLED)
            self.text2.config(state=NORMAL)
            self.text2.insert(INSERT, text_blob)
            self.text2.config(state=DISABLED)
        except Exception as err:
            #self.text2.insert(INSERT, "Error {}".format(err))
            tkMessageBox.showinfo("Translator exception", "You cannot translate to the same language")

    # function Post
    def post(self):
        pt = keys.KeysTweet()
        if not self.lblImg.cget("text"):
            if not self.text2.get("1.0", "end-1c"):
                tkMessageBox.showinfo("Tweet sent", "You cannot send empty Tweet")
            else:
                texto = self.text2.get("1.0", "end-1c")
                self.text2.config(state=NORMAL)
                print ("Esta lleno")
                pt.enviar(texto)
                tkMessageBox.showinfo("Tweet sent", "Your Tweet has been sent")

        if self.lblImg.cget("text"):
            texto = self.text2.get("1.0", "end-1c")
            self.text2.config(state=NORMAL)
            img = self.lblImg.cget("text")
            pt.post_text_img(img, texto)
            tkMessageBox.showinfo("Tweet sent", "Your Tweet has been sent")

    # function to clear boxes
    def limpiar(self):
        self.text1.delete("1.0", 'end-1c')
        self.text2.config(state=NORMAL)
        self.text2.delete("1.0", 'end-1c')
        self.text2.config(state=DISABLED)
        self.encount.config(state=NORMAL)
        self.encount.delete(0, END)
        self.encount.config(state=DISABLED)
        self.cboxl.current(0)

    # function to quit
    def salir(self):
        root.destroy()


if __name__ == '__main__':
    root = Tk()
    my_trans = MyTranslator(root)
    root.mainloop()