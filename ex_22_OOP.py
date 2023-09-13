from random import randint
import getpass 

class congrats:
    #Variables to work with through the class will be here
    def __init__(self):
        self.congrlist = ["Bravo",
                    "Cheers",
                    "Felicitations",
                    "Hip, hip, hooray",
                    "Hooray",
                    "Many happy returns of the day",
                    "Best wishes on your special day",
                    "Have a fantastic birthday",
                    "Wishing you a day filled with joy",
                    "May your day be filled with laughter and love",
                    "Here's to another year of fabulous you",
                    "Celebrate in style",
                    "Enjoy your special day to the fullest",
                    "Another year, another adventure",
                    "Happy birthday to an amazing person",
                    "May all your birthday wishes come true",
                    "Cheers to another year of life",
                    "Sending you warm birthday wishes",
                    "Have a blast on your birthday",
                    "It's your day, make it unforgettable",
                    "Wishing you health, happiness, and success",
                    "Another year older, wiser, and more fabulous",
                    "Make a wish and blow out the candles",
                    "Let the birthday festivities begin",
                    "Here's to a year filled with blessings",
                    ]
        self.symbollist = ['\u2042','\u22C6','\u2606','\u2655','\u272E','\u2735','\u2740','\u2743']

    #Iter
    def __iter__(self):
        return self
    
    #Creating next iteration of object
    def __next__(self):
        cong = self.congrlist[randint(0, len(self.congrlist)-1)]
        return cong

#Child class "Cogratulations with your username from OS"
class congratswithname(congrats):
    def __init__(self):
        self.username = getpass.getuser()
        super().__init__()

    def __next__(self):
        picsymbols = (self.symbollist[randint(0, len(self.symbollist)-1)]+" ") * 30
        cong = picsymbols + "\n" + self.username + "! " + self.congrlist[randint(0, len(self.congrlist)-1)] + "\n" + picsymbols + "\n"
        return cong


'''
MAIN
'''        
congr = congratswithname()

while 1 > 0:
    print(next(congr))
    key = input('For one more congratulation press Enter! For exit press "n"\n')
    if key == 'n':
        break
   





