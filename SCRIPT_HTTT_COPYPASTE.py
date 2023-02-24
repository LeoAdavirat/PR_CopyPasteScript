#Import libraries
import pyperclip

#Input Page name
Page_name = input("Please input page name: ")

#Read the script
with open("SCRIPT_HTTT.txt", encoding='utf-8') as SCRIPT_HTTT_file:
    text_copy = SCRIPT_HTTT_file.read()

#Replace the Page's name
text_copy = text_copy.replace("{}", Page_name)
text_copy = text_copy.replace("(TÊN PAGE)", Page_name)
text_copy = text_copy.replace("(PAGE'S NAME)", Page_name)
text_copy = text_copy.replace("(PAGE's NAME)", Page_name)

#Check and Copy into clipboard
print(text_copy)
pyperclip.copy(text_copy)
spam = pyperclip.paste()