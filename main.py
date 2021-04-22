#application that translates detected language to a variety of output languages
#python gui with tkinter
#dependant on google translate alpha version
from tkinter import *
import tkinter.ttk as ttk
from googletrans import Translator
import googletrans


#initialize translator and set geometry for window
translator = Translator()
root = Tk()
root.geometry("535x535")
root.title("Language Translator")
root.iconbitmap("images/icontiny.ico")
root.resizable(False, False)

#background image
background_image = PhotoImage(file='images/background.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#google translation
def gtrans():
    #chosen language
    chosen_lang = options.get()

    #sets output text state to enabled
    output_entry.configure(state='normal')

    #gets the content to be translated
    get_text = input_entry.get("1.0", END)
    in_lang = translator.detect(get_text)    

    result = translator.translate(text=get_text, dest=chosen_lang, src=in_lang.lang)
    output_entry.delete("1.0", END)
    output_entry.insert("1.0", result.text)

    output_entry.configure(state='disabled')
 
#Target Language Drop Down Menu
variable = StringVar(root)
options = ttk.Combobox(root, width=27, textvariable=variable, state='readonly')

#sets up dictionary of languages into two lists
dictionary = {}
dictionary = googletrans.LANGUAGES
lang_code = [k for item in [dictionary] for k,v in dictionary.items()]
lang = [v for item in [dictionary] for k,v in dictionary.items()]

#loop to capitalize every item in list lang
lang_upper = [x.capitalize() for x in lang]

#options dropdown values and gridded
options['values'] = lang_upper
options.grid(row=0,column=2)

#image for label background
label_back = PhotoImage(file='images/Label_Back1.png') #background image for result_label
label_back2 = PhotoImage(file='images/Label_Back2.png') #background image for input_label
label_back3 = PhotoImage(file='images/Label_Back3.png') #background image for target_language

#target lang label
target_language = Label(root, text="Select target language: ", font=("Helvetica", 12, 'bold'), fg='white', image=label_back3, compound='center')
target_language.grid(row=0, column=0, padx=(15,0), pady=(15,15))

#input label and entry boxes
input_label = Label(root, text="Input text to be translated\n(in any language)", fg='white', font=("Helvetica", 12, 'bold'), image=label_back2, compound='center')
input_label.grid(row=1, column=0, padx=(20,0))
input_entry = Text(fg="black", bg="white", highlightbackground="black", highlightthickness="1", height="8", width="25", font=("Helvetica"), wrap=WORD)
input_entry.grid(row=1,column=2, pady="10")

#result label and entry boxes
result_label = Label(root, text="Translation:", fg='white', font=("Helvetica", 12, 'bold'), image=label_back, compound='center')
result_label.grid(row=2, column=0, pady=(10,25))
output_entry = Text(fg="black", bg="SystemButtonFace", highlightbackground="black", highlightthickness="1", height="8", width="25", font=("Helvetica"), wrap=WORD)
output_entry.grid(row=2,column=2, pady=(10,25))
output_entry.configure(state='disabled')

#green translate button
translate_button = Button(text="Translate", bg="lightgreen", fg="black", command=gtrans, relief=RAISED)
translate_button.grid(row=3,column=1, pady="8")

#quit button
quit_button = Button(text="Quit", command=root.destroy)
quit_button.grid(row=4, column=1)

##main loop##
root.mainloop()
