# coding=utf-8
import codecs
import re
import unicodedata
from transliterate import translit, get_available_language_codes
from langdetect import detect

book_notes = {}
bnewbook = False
book_name = ""
log=codecs.open('log.txt','w','utf-8')
notes=codecs.open('My_Clippings.txt','r+','utf-8')
# find all unique book names
for index, line in enumerate(notes, start = 1):
    if index == 2 or bnewbook: 
        book_name = line.upper().strip().replace(" ","_").replace(".","")
#        book_name = book_name.replace("/[\W_]/g", "_");
#        book_name = translit(book_name, reversed = True)
        book_name = book_name.encode("utf-8")
        book_name = book_name.replace("\xef\xbb\xbf", "") 
#        book_name = book_name[0:30]         
        bnewbook = False
    if line.strip() == '==========': 
        bnewbook = True 
        continue
    if book_name != "":
        if book_name in book_notes and book_notes[book_name]: 
            book_notes[book_name] += line + "\n"            
        else:
            book_notes[book_name] = line + "\n"
# for every unique book name create a file in folder books
for book_name in book_notes:
    book_fname = "books/" + book_name + ".txt"
    try:
        book = codecs.open(book_fname,"w",'utf-8')
    except:
        print(book_name)
        log.write(book_name.decode("utf-8")) 
        continue
    book.write(book_notes[book_name])  
    book.close()
