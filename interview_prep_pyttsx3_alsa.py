#!/usr/bin/env python3

import pyttsx3 
from random import randrange 


list_of_questions=[
    "Tell me a little about yourself",
    "Why do you want to work here?",
    "Tell me about a time when you overcame a challenge at work.",
    "Do you have any questions for me?",
    "How did ypu hear about the position?",
    "What do you consider your strengths and weaknesses?",
    "What are your career goals?",
    "Why are you interested in this position?",
    "Where do you see yourself in 5 years?",
    "Why should we hire you?"
    ]

engine = pyttsx3.init()

while 1 > 0: 
    random_question_index = randrange(len(list_of_questions)-1)
    engine.say(list_of_questions[random_question_index])
    engine.runAndWait()

    input('Press any key...')
