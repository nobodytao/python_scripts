#!/usr/bin/env python3

import pyttsx3 
from random import randrange 

try:
    with open('interview_questions.txt','r') as interview_file:

            list_of_questions = interview_file.readlines()

            engine = pyttsx3.init()

            while 1 > 0: 
                random_question_index = randrange(len(list_of_questions))
                engine.say(list_of_questions[random_question_index])
                engine.runAndWait()

                input('Press any key...')

except FileNotFoundError:
    print("Can't find 'interview_questions.txt'. Create it by yourself, pls. One line - one question.")