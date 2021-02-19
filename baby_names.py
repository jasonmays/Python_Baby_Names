#Jason Mays
#Programming Assignmnet #6, 10/13/16
#This program asks for a name and gender and then reads two files.
#It pulls out the line that matches the name and gender that is put in.
#It then displays a graph of how popular the name was for each decade.

from DrawingPanel import *

YEAR = 1890
DECADES = 13
HEIGHT = 30
WIDTH = 60

def main():
    intro()
    name_search = get_name()
    gender_search = get_gender()
    file1 = open("names.txt")
    file2 = open("meanings.txt")
    line1 = search (file1, name_search, gender_search)
    #The below lines decide if the words match a line and then prints the two lines.
    #It also calls the graph function. If it doesn't find matches then it prints
    #"name" does not match.
    if(len(line1) > 0):
        num = display(line1, name_search, gender_search)
        number = num.split() 
        number_copy = num.split()
        line2 = search (file2, name_search, gender_search)
        if(len(line2) > 0):
            display(line2, name_search, gender_search)
            p = DrawingPanel (780, 560, background = "white")
            numbers = convert(number)
            graph_title(p, line2)
            graph_bar(p, numbers, gender_search, number_copy)
        else:
            print(end='')
    else:
        print("\"" + name_search + "\"" + " not found")
    
#This function produces the intro to the program.  
def intro ():
    print("This program allows you to search through the")
    print("data from the Social Security Administration")
    print("to see how popular a particular name has been")
    print("since 1890.")
    print()
    
#This function asks for the name and returns it to main.
def get_name():
    name_search = input("Name: ")
    name_search = name_search.lower()
    return name_search

#This program asks for the gender and returns it to main.
def get_gender():
    gender_search = input("Gender: ")
    gender_search = gender_search[0].lower()
    return gender_search
    
#This function seraches for the lines that match the words and returns it to main.
def search (file, name_search, gender_search):
    first_line = ""
    for line in file:
        line_lower = line.lower()
        line_split = line_lower.split()
        if (name_search == line_split[0] and gender_search == line_split[1]):
            if (first_line == ""):
                return line
    return ""

#This function displays the line that the words match for and returns the numbers
#for each decade. 
def display (line, name_search, gender_search):
    parts = line.split()
    name = parts[0]
    gender = parts[1]
    rest = ""
    if (gender_search == gender):
        for i in range(2, len(parts)):
            rest += parts[i] + " "
        print(name + " " + gender + " " + rest)
    return rest

#This function graphs the top and bottom gray part of the graph.
#It displays the name meaning at the top and the decades at the bottom.
def graph_title (p, line2):
    p.canvas.create_rectangle (0, 0, 780, HEIGHT, fill = "light gray")
    p.canvas.create_rectangle (0, 560, 780, 560 - HEIGHT, fill = "light gray")
    p.canvas.create_text(360, 16, text= line2)
    for i in range (0, DECADES):
        p.canvas.create_text(15 + (i*WIDTH), 552, text= int(YEAR + (i*10)))
        
#This function converts the list of numbers for the popularity of the name
#and then converts it to y-axis coordinates.
def convert(number):
    for i in range (0, len(number)):
        if(int(number[i]) > 1):
            number[i] = HEIGHT + (int(number[i])//2)
        if(int(number[i]) == 1):
            number[i] = HEIGHT
        if(int(number[i]) == 0):
            number[i] = 560 - HEIGHT
    return number
            
#This function produces the bars for how popular each name was in that decade.
#It also displays yellow bars for females and green bars for males.
def graph_bar(p, numbers, gender_search, number_copy):
    for i in range(0, DECADES):
        if(gender_search == "f"):
            p.canvas.create_rectangle (i * WIDTH, numbers[i], 30 + (i * WIDTH), 560 - HEIGHT,
                                       fill = "yellow",width = 0)
            p.canvas.create_text (i * WIDTH, numbers[i], text = int(number_copy[i]))
        if(gender_search == "m"):
            p.canvas.create_rectangle (i * WIDTH, numbers[i], 30 + (i * WIDTH), 560 - HEIGHT,
                                       fill = "green",width = 0)
            p.canvas.create_text (i * WIDTH, numbers[i], text = int(number_copy[i]))
        
           

main()
            
