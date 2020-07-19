#Absenct statistics
import time 
def group(ad):                                        
    with open(ad, encoding='UTF-8') as sf:
        text = sf.read()
    global sign
    for ch in '\n  “”‘’\'"+1234567:890—_-':
        text=text.replace(ch,'')
    for i in sign:
        text=text.replace(i,',')
    return set(text.split(','))
with open("symbol.txt", encoding='UTF-8') as sf:
        sign0 = sf.read()
sign=sign0.split('|')
present=group("present.txt")
leave=group("leave.txt")
total=group("total.txt")
present=present&total
absence=total-present-leave                          
print("Absent list:{}".format(absence))
time.sleep(10000)
