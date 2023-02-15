from gpiozero import LED, Button
from time import sleep
import requests
import json


key = 'REDACTED'
token = 'REDACTED'

boardid = 'REDACTED'
cardid = 'REDACTED'

listid = 'REDACTED'
finalid = 'REDACTED'

def doit():
    r = requests.put('https://api.trello.com/1/cards/'+cardid+'?idlist='+finalid+'&key='+key+'&token='+token)
    m = r.json
    return(m)

def nogobackpls():

    r = requests.put('https://api.trello.com/1/cards/'+cardid+'?idlist='+listid+'&key='+key+'&token='+token)
    m = r.json
    return(m)

B1 = Button(17)
B2 = Button(27)
ligh = LED(22)

print(('https://api.trello.com/1/cards/'+cardid+'?idlist='+listid+'&key='+key+'&token='+token))

ligh.on()
sleep(1)
ligh.off()
while True:
    if B1.is_pressed:
        print('button 1 was pressed')
        ligh.on()
        sleep(1)
        ligh.off()
        sleep(1)
        print(doit())
    if B2.is_pressed:
        print('button 2 was pressed')
        ligh.on()
        sleep(1)
        ligh.off()
        sleep(1)
        print(nogobackpls())