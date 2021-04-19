#application that translates detected language to a variety of output languages
#python gui with tkinter
#dependant on google translate alpha version
from tkinter import *
from googletrans import Translator


#initialize translator and set geometry for window
translator = Translator()
root = Tk()
root.geometry("500x500")
root.title("Language Translator")

#google translation
def gtrans():
    #sets output text state to enabled
    output_entry.configure(state='normal')

    #gets the content to be translated
    get_text = input_entry.get("1.0", END)
    in_lang = translator.detect(get_text)    

    #gets the target language and swaps string to google translate keyphrase for lang selection  
    target_language = variable.get()      
    if target_language == "Spanish":            #find a more efficient way to do this
        dest = 'es'
    elif target_language == "Afrikaans":
        dest = 'af'
    elif target_language == "Norwegian":
        dest = 'no'
    elif target_language == "Serbian":
        dest = 'sr'
    elif target_language == "Croatian":
        dest = 'hr'

    #translates and inserts result into output_entry      
    result = translator.translate(text=get_text, dest=dest, src=in_lang.lang)
    output_entry.delete("1.0", END)
    output_entry.insert("1.0", result.text)

    #sets output text state to disabled to avoid editing
    output_entry.configure(state='disabled')

    return
 
#Target Language Drop Down Menu
lang_options = ["Spanish", "Afrikaans", "Norwegian", "Serbian", "Croatian"] #all language options
variable = StringVar(root)
variable.set(lang_options[0])                                               #default value is spanish

target_language = Label(root, text="Select Target Language: ")
target_language.grid(row=0, column=0, padx="20", pady="25")

options = OptionMenu(root, variable, *lang_options)
options.grid(row=0,column=2)

#input label and entry boxes
input_label = Label(root, text="Input translation text:\n(in any language)", pady="25")
input_label.grid(row=1, column=0, pady="20")

input_entry = Text(fg="black", bg="white", highlightbackground="black", highlightthickness="1", height="8", width="22") #swapped from entry to Text
input_entry.grid(row=1,column=2, pady="20")

#result label and entry boxes
result_label = Label(root, text="Translated text:", pady="25")
result_label.grid(row=2, column=0, pady="20")
output_entry = Text(fg="black", bg="white", highlightbackground="black", highlightthickness="1", height="8", width="22") #swapped from entry to text
output_entry.grid(row=2,column=2, pady="20")

#green translate button
translate_button = Button(text="Translate", bg="lightgreen", fg="black", command=gtrans)
translate_button.grid(row=3,column=1, pady="8", padx="10")

#quit button
quit_button = Button(text="Quit", command=root.destroy)
quit_button.grid(row=4, column=1)

##main loop##
root.mainloop()