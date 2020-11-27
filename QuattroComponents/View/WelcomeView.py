from pyfiglet import Figlet

def WelcomeView():
    f = Figlet(font="nancyj").renderText("Welcome To Quattro")
    enter = Figlet(font="small").renderText("Press Enter To start!")

    print(f, enter, sep='\n')
    __import__('sys').stdin.readline()


