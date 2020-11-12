# coding=utf-8
import codecs
import re
import unicodedata

book_notes = {}
bnewbook = False
book_name = ""
with codecs.open('My_Clippings.txt','r+','utf-8') as notes:
# find all unique book names
    for index, line in enumerate(notes, start=1):
        if index == 2 or bnewbook: 
            book_name = line.upper().strip().replace(" ","_").replace(".","")
#            book_name = re.sub('[^А-Я0-9]+', ' ', book_name)
            book_name = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', book_name)
            book_name = book_name[:30].encode("utf-8")            
            bnewbook = False
        if line.strip() == '==========': 
            bnewbook = True 
            continue
        if book_name!="":
            if book_name in book_notes and book_notes[book_name]: 
                book_notes[book_name]+=line+"\n"
            else:
                book_notes[book_name]=line+"\n"
# for every unique book name create a file in folder books
for book_name in book_notes:
    if "59_СКАЗАТЬ_ЖИЗНИ_ДА!_ВИКТОР" in book_name:
        print(str(len(book_name))+" 1"+book_name+"2")
    book = codecs.open("books/"+book_name+".txt","w",'utf-8')
    book.write(book_notes[book_name])  
    book.close()
