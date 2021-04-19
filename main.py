#application that translates detected language to a variety of output languages
#python gui with tkinter
#dependant on google translate alpha version
from tkinter import *
from googletrans import Translator


#initialize translator and set geometry for window
translator = Translator()
root = Tk()
root.geometry("500x400")
root.title("Language Translator")

#google translation
def gtrans():
    #gets the content to be translated
    get_text = input_entry.get()
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
    output_entry.delete(0, "end")
    output_entry.insert(0, result.text)
    return
 
#Target Language Drop Down Menu
lang_options = ["Spanish", "Afrikaans", "Norwegian", "Serbian", "Croatian"] #all language options
variable = StringVar(root)
variable.set(lang_options[0])                                               #default value is spanish

target_language = Label(root, text="Select Target Language: ")
target_language.grid(row=0, column=0)

options = OptionMenu(root, variable, *lang_options)
options.grid(row=0,column=1)

#input label and entry boxes
input_label = Label(root, text="Input translation text:")
input_label.grid(row=1, column=0)

input_entry = Entry(fg="black", bg="white", highlightbackground="black", highlightthickness="1")
input_entry.grid(row=1,column=1)

#result label and entry boxes
result_label = Label(root, text="Translated text:")
result_label.grid(row=2, column=0)
output_entry = Entry(fg="black", bg="white", highlightbackground="black", highlightthickness="1" )
output_entry.grid(row=2,column=1)

#green translate button
translate_button = Button(text="Translate", bg="lightgreen", fg="black", command=gtrans)
translate_button.grid(row=3,column=0)

#quit button
quit_button = Button(text="Quit", command=root.destroy)
quit_button.grid(row=4, column=0)

##main loop##
root.mainloop()