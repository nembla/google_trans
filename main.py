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
root.geometry("500x500")
root.title("Language Translator")
root.iconbitmap("icontiny.ico") 

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


#target lang label
target_language = Label(root, text="Select Target Language: ")
target_language.grid(row=0, column=0, padx="20", pady="25")

#input label and entry boxes
input_label = Label(root, text="Input translation text:\n(in any language)", pady="25")
input_label.grid(row=1, column=0, pady="20")

input_entry = Text(fg="black", bg="white", highlightbackground="black", highlightthickness="1", height="8", width="27") 
input_entry.grid(row=1,column=2, pady="20")

#result label and entry boxes
result_label = Label(root, text="Translated text:", pady="25")
result_label.grid(row=2, column=0, pady="20")
output_entry = Text(fg="black", bg="white", highlightbackground="black", highlightthickness="1", height="8", width="27") 
output_entry.grid(row=2,column=2, pady="20")

#green translate button
translate_button = Button(text="Translate", bg="lightgreen", fg="black", command=gtrans)
translate_button.grid(row=3,column=1, pady="8", padx="10")

#quit button
quit_button = Button(text="Quit", command=root.destroy)
quit_button.grid(row=4, column=1)

##main loop##
root.mainloop()
