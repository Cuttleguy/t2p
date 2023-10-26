import requests
from urllib import parse
import nltk
from nltk import pos_tag
from tkinter import *
from tkhtmlview import HTMLLabel
import speech_recognition as sr
from nltk.corpus import wordnet
# nltk.download()
# nltk.download('universal_tagset')
# nltk.download('punkt')
nltk.download('wordnet')
# inital=Tk()


def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query
window=Tk()
def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)
def phraseToIcon(phrase):
    try:
        safePhrase=parse.quote_plus(phrase)
        x = requests.get('https://thenounproject.com/search/icons/?q='+safePhrase)
        txt=x.text

        imgList=txt.split("<img src=")
        if phrase.lower()=="jupiter":
            metas=imgList[3].split('"')
        else:
            metas=imgList[1].split('"')

        return (metas[1])
    except:
        return ""
    # print(phraseToIcon(""))
def textToPict(text,tags):

    index = 0
    progress = 0
    txt=""
    ws_ts = pos_tag(text.split(),tagset="universal")
    for word, tag in ws_ts:
        print(f'{word}, {tag}')

        if any(x in tag for x in tags):
            if word=="can't":
                icon=phraseToIcon("not")
            elif word == "are" or word == "is":
                icon = phraseToIcon("equals")

            else:
                index = text.find(word, index, len(text))
                icon = phraseToIcon(word)
            txt+=f'<img width="20px"src="{icon}">'
        progress+=1
    return txt
words=takeCommand().lower()
pictoStr=textToPict(words,["NOUN","VERB","ADJ","ADV","PRON"])
#
# inital.destroy()
print(pictoStr)

window.title('Hello Python')
window.geometry("300x200+10+20")
picto=HTMLLabel(window,html=pictoStr,width=270,height=170)
picto.pack(pady=20, padx=20)
def update():
    picto.set_html(html=pictoStr)
    window.after(1000, update)
update()
window.mainloop()