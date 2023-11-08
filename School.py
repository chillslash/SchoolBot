import os
import ast
import time
import datetime
monday = ['Literature', 'Literature', 'Mother Tongue', 'Mother Tongue', 'English', 'English', 'Recess', 'Science', 'Science', 'Science', 'Geography', 'H-Cube', 'H-Cube']
tuesday = ['AP', 'AP', 'English', 'English', 'Science', 'Science', 'Recess', 'Art', 'Art','Art', 'Math', 'Math', 'History']
wednesday = ['Assembly', 'Math', 'PE', 'PE', 'D&T', 'D&T', 'Recess', 'History', 'History', 'Mother Tongue', 'Mother Tongue', 'Early Dismissal', 'Early Dismissal']
thursday = ['AP', 'AP', 'Geography', 'Geography', 'PE', 'PE', 'Recess', 'Math', 'Math', 'D&T', 'D&T', 'Mother Tongue', 'Mother Tongue']
friday = ['Science', 'Science', 'Speech/Drama', 'Speech/Drama', 'Math', 'Math', 'Recess', 'Literature', 'English', 'Early Dismissal', 'Early Dismissal', 'Early Dismissal', 'Early Dismissal', 'Early Dismissal']
timee = [' 0800-0830', ' 0830-0900', ' 0900-0930', ' 0930-1000', ' 1000-1030', ' 1030-1100', ' 1100-1130', ' 1130-1200', ' 1200-1230', ' 1230-1300', ' 1300-1330', ' 1330-1400', ' 1400-1430']
days = monday, tuesday, wednesday, thursday, friday
def cont(n):
    try:
        x = n[1]
        return True
    except IndexError:
        print("No date input found")
        return False
def reminder():
    remind = str(datetime.datetime.now())
    if (remind[11] == '2' and len(hw) != 0) and (remind[12] == '0' or remind[12] == '1' or remind[12] == '2' or remind[12] == '3') and (len(hw) != 0):print("PLEASE COMPLETE HOMEWORK SOON!!!")
    else:pass
def isdigit(n):
    try:
        int(n)
        return True
    except ValueError: return False
def empty():
    try:
        k = len(input1)
        if k >= 1:return k
    except:return False
def empty2():
    try:
        k = len(i[1])
        if k >= 1:return True
    except:return False
def empty3():
    try:
        k = len(i[2])
        if k >= 1:return False
    except:return True
def hwprint():
    posthw = hw.split("\n")
    length = len(posthw)-1
    j = 0
    if length == 0:
        # Separating if there's no homework
        print("Empty")
    # Getting one homework at a time
    for i in range(length):
        f = 30
        posthw1 = posthw[j].split("| ")
        # If there is no date, an exception will be raised and returned False
        if cont(posthw1):
            # Separating if the homework is more than 30 characters long
            if len(posthw1[0]) > 30:
                posthw2 = posthw1[0]
                # Separating if the number of homework is 2 digits...
                if j>8:
                    print("{}: {}: {}".format((j + 1), posthw2[0:30], posthw1[1]))
                # Or 1 digit
                elif j<9:
                    print("{} : {}: {}".format((j + 1), posthw2[0:30], posthw1[1]))
                # If the homework is divisible by 30, it can be easily looped by the same format
                if (len(posthw2)%30) == 0:
                    for s in range(int((len(posthw2)/30)-1)):
                        print("{}{}{}{}".format("  : ", posthw2[f:f+30], " "*(30-len(posthw2[f:f+30])), ":"))
                        f+=30
                    j+=1
                # Else, it would be looped till the last part
                else:
                    newnumb = ((len(posthw2)-(len(posthw2)%30))/30)
                    for s in range(int(newnumb)):
                        print("{}{}{}{}".format("  : ", posthw2[f:f+30], " "*(30-len(posthw2[f:f+30])), ":"))
                        f += 30
                    j += 1
            # If the homework is less than 30 characters long
            else:
                # Same thing of separating if number of homework is 2 digits...
                if j > 8:
                    print("{}: {}{}: {}".format((j + 1), posthw1[0], " " * (30 - len(posthw1[0])), posthw1[1]))
                # and 1 digit
                elif j < 9:
                    print("{} : {}{}: {}".format((j+1), posthw1[0], " "*(30-len(posthw1[0])), posthw1[1]))
                j += 1
        else:
            return False
try:
    print("Starting up...")
    print("Homework loading...")
    hw = open("hw.txt").read()
    print("Homework loaded")
    print("Startup completed!")
    reminder()
    while True:
        input2 = input("\nEnter: ")
        input1 = str(input2)
        p = 0
        if empty():
            print()
            i = input1.split(" ")
            if i[0].lower() != "add":
                input1 = input1.lower()
                i = input1.split(" ")
            if i[0] == 'hi' or i[0] == 'hey' or i[0] == 'yo' or i[0] == 'hello' or i[0] == 'sup':
                print("Heyo")
                reminder()
            elif input1 == 'saturday' or input1 == 'sunday':
                print("Um, there's no school on the weekend\n")
                reminder()
            elif i[0] == 'hw':
                hwprint()
                reminder()
            elif input1 == 'del':
                print("What do you want to delete?")
                reminder()
            elif i[0] == 'del' and isdigit(i[1]):
                posthw = hw.split("\n")
                num1 = int(i[1])
                num = num1 - 1
                try:
                    new = posthw[num] + "\n"
                    if new != "\n":
                        hw = hw.replace(new, "")
                        hwprint()
                        reminder()
                    else:
                        print("There is no", num1, "homework")
                        reminder()
                except:
                    print("There is no", num1, "homework")
                    reminder()
            elif i[0] == 'del' and i[1] == 'all':
                hw = ""
                hwprint()
                reminder()
            elif input1 == 'add' or input1 == "aDd" or input1 == "Add" or input1 == "adD" or input1 == "ADd" or input1 == "aDD" or input1 == "AdD" or input1 == "ADD":
                print("What do you want to add?")
                reminder()
            elif i[0] == 'add' or i[0] == "aDd" or i[0] == "Add" or i[0] == "adD" or i[0] == "ADd" or i[0] == "aDD" or i[0] == "AdD" or i[0] == "ADD":
                testinp = i[0] + " "
                inp = input1.replace(testinp, "")
                inp+="\n"
                hw = hw + inp
                if hwprint() == False:
                    hw = hw.replace(inp, "")
                reminder()
            elif input1 == 'end':
                print("Thank You for using")
                print("\nSaving Homwork")
                with open("Hw.txt", "w") as MyFile:
                    MyFile.write(str(hw))
                print("Homework saved\n\nHomework:\n")
                hwprint()
                reminder()
                print("\nShutting down...")
                time.sleep(5)
                break
            elif input1 == 'stop':
                break
            elif input1 == 'help':
                print("Commands:\n")
                print("[(monday-friday)] - Shows timetable")
                print("[add (Work)| (Due date)] - Adds homework to hw list")
                print("[del (Number of homework)] - Deletes homework")
                print("[del all] - Delete all homework")
                print("[hw] - Shows the homework")
                print("[end] - Shuts down the program and auto saves homework")
                print("[stop] - Stops the program immediately without saving")
                reminder()
                print()
            elif input1 == 'about':
                print("School\nCreated By Ryan\nVersion: 3.7")
                reminder()
            else:
                for day in days:
                    try:
                        if eval(input1) == day:
                            print(str.capitalize(input1), "\b:")
                            for p in range(13):
                                print(timee[p], ":", day[p])
                            reminder()
                            break
                    except:
                        pass

except ValueError:
    print("\nValue Error Occurred\nForce Shutdown")
except IndentationError:
    print("\nIndentation Error Occurred\nForce Shutdown")
except FileNotFoundError:
    print("\nFileNotFound Error Occurred\nForce Shutdown")
