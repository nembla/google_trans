#Language translator from English to any target using google translate requests
#Currently supports: Spanish (es), Afrikaans (af), and Norwegian (no), Serbian (sr)
#Support can be expanded in future project for practice. 
from googletrans import Translator


translator = Translator()
run = True

#Language Selection
while run == True:
    print("\n" + "Welcome to my English Language Translator. Select from the following menu:")
    print("1.Spanish\n2.Afrikaans\n3.Norwegian\n4.Serbian Cyrillic\n5.Serbian Latinica")
    menu = int(input("Enter target langauge: "))

    if menu == 1:
        print("Spanish selected.")
        target_language = 'es'

    elif menu == 2:
        print("Afrikaans selected.")
        target_language = 'af'

    elif menu == 3:
        print("Norwegian selected.")
        target_language = 'no'
    
    elif menu == 4:
        print("Serbian (Cyrillic) selected.")
        target_language = 'sr'

    elif menu == 5:
        print("Serbian (Latin) selected.")
        target_language = 'hr'

    else:
        print("Error: no language selected.")
        continue
    run = False

content = input("Enter content to be translated: ")                                         #content to be translated
in_lang = translator.detect(content)                                                        #detect input language
result = translator.translate(text=content, dest=target_language, src=in_lang.lang)         #translate input to target language
print(result.text)                                                                          #output results