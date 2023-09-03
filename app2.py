import datetime
import time
import random
from gtts import gTTS
import PyPDF2


today=datetime.date.today()
var = str((today.year))
#print(var)

t = time.localtime()
current_time = str(time.strftime("%H%M",t))
#print (current_time)

name = input("Enter the file-name (*for saving pupose)\n")

counter=0
for c in name:
    counter = counter + 1
#print (counter)



if (counter >=10):
    name = name[0:4]
    
elif (counter ==9):
    name = name[:-5]
    
elif (counter == 8 ):
    name = name[:-4]

elif (counter == 7):
    name = name[:-3]

elif (counter == 6):
    name = name[:-2]

elif (counter == 5):
    name = name [:-1]
    

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0381"
length = 3

password = ""

for a in range (length):
    password = password+random.choice(chars)
#print (password)

final = str(name+var+password+current_time)


language = "hi"

pdf_file_path = r"C:\Users\sanskar\Desktop\for git\instructions.pdf"
pdf_file = open(pdf_file_path, "rb")


pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ""
for page_num in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[page_num].extract_text()
pdf_file.close()
speech = gTTS(text=text, lang=language, slow=False)
file_name_with_extension = final + ".mp3"
speech.save(file_name_with_extension)
print("audio has been saved as :"+final+".mp3.")