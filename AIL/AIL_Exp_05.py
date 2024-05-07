'''
Madhur Jaripatke
Roll No. 48
TE A Computer
RMDSSOE, Warje, Pune
'''
'''
Develop an elementary chatbot for any suitable customer interaction application.
'''
import nltk
from nltk.chat.util import Chat, reflections

pairs=[
    #
    [
        r"My name is (.*)",
        ["Hello %1, How are you"]
    ],
    # Or expression
    [
        r"Hi|Hello|Hey there|Hola|What up",
        ["Hello my name is JackieBot"]
    ],
    [
        r"What is your name ?",
        ["I am a bot created by The Illuminati. you can call me friend!",]
    ],
    [
        r"How are you ?",
        ["I'm doing good How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"I (.*) good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude. Find better things to ask",]
    ],
    [
        r"What (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["The Illuminati created me using Python's NLTK library ","Top secret (The Illuminati created me);)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Area 51, USA',]
    ],
    [
        r"How is weather in (.*)?",
        ["Weather in %1 is awesome like always","It's too hot here in %1","It's freezing cold here in %1","Never even heard about %1"]
    ],
    [
        r"I work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"Who (.*) sportsperson ?",
        ["Messy","Ronaldo","Rooney"]
    ],
    [
        r"Who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"I am looking for online guides and courses to learn data science, can you suggest?",
        ["Madhur has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ["Thank you for using our dumb intelligence services"]
    ],
    

]

def chat():
    print("Hey there! I am JackieBot at your service")
    chat = Chat(pairs)
    chat.converse()

if __name__== "__main__":
    chat()
