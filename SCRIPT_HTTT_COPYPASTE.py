#Import libraries
import pyperclip

#Prepare List
List_replace_Key = ["{}", "(TÊN PAGE)", "(PAGE'S NAME)", "(PAGE's NAME)", "(full name of the club/Project)", "(full name Club/Project)", "(tên đầy đủ của CLB/Dự án)", " (tên đầy đủ CLB/Dự án)"]

while True: 
    #Input Page name
    Page_name = input("Please input page name: ")
    #Read the script
    with open("SCRIPT_HTTT.txt", encoding='utf-8') as SCRIPT_HTTT_file:
        text_copy = SCRIPT_HTTT_file.read()

    #Replace the Page's name
    for replace_key in List_replace_Key:
        text_copy = text_copy.replace(replace_key, Page_name)

    #Check and Copy into clipboard
    print("Text copied into clipboard! Enjoy!")
    pyperclip.copy(text_copy)
    spam = pyperclip.paste()