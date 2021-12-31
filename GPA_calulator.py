class Student(object):
    name = ""
    schoollevel = ""
    studentID = ""
    currentCreditHours = ""
    currentGPA = ""
    desiredGPA = ""
    remainingCreditHours = ""
    takingClasses = ""
    numOfClasses = ""
    classesName = []
    classesGrade = []
    classesHours = []
    
def letters(numOfClasses, classesGrade,classesHours):
    global qualityPoints
    qualityPoints=0
    listGrades = []
    listCreditHours = []
    for i in range(int(numOfClasses)):
        beValid = False
        while not beValid:
            if classesGrade[i] == "A" or classesGrade[i] == "a" or classesGrade[i] == "4" or classesGrade[i] >= "90":
                beValid = True
                classInput1 = 4
            elif classesGrade[i] == "B" or classesGrade[i] == "b" or classesGrade[i] == "3" or classesGrade[i] >= "80":
                beValid = True
                classInput1 = 3
            elif classesGrade[i] == "C" or classesGrade[i] == "c" or classesGrade[i] == "2" or classesGrade[i] >= "70":
                beValid = True
                classInput1 = 2
            elif classesGrade[i] == "D" or classesGrade[i] == "d" or classesGrade[i] == "1" or classesGrade[i] >= "60":
                beValid = True
                classInput1 = 1
            elif classesGrade[i] == "F" or classesGrade[i] == "f" or classesGrade[i] == "0" or classesGrade[i] < "60":
                beValid = True
                classInput1 = 0

                
        qualityPoints += (classInput1*int(classesHours[i]))
        listGrades.append(classInput1)
        listCreditHours.append(classesHours)
    return qualityPoints,

def create_student():
    newstudent = Student()
    
    #makes the name
    newstudent.name = input("What is your name?: \n")

    #makes the schoollevel
    check1 = False
    while not check1:
        newstudent.schoollevel = input("Are you in High school or College?: \n")
        if newstudent.schoollevel.upper() == "HIGH SCHOOL":
            check1=True
            newstudent.schoollevel = 'HIGH SCHOOL'
            break
        elif newstudent.schoollevel.upper() == "COLLEGE":
            check1=True
            newstudent.schoollevel = "COLLEGE" 
            break     
        else:
            print("Please put 'High School' or 'College'")

    #makes the studentID if user is in college
    if newstudent.schoollevel == "COLLEGE":
        newstudent.studentID = input("What is your studentID? \n")
    else:
        newstudent.studentID = "N/A"
    
    #Sees how many credit hours/GPA a student has already taken
    newstudent.currentCreditHours = int(input("How many credit hours have you taken? (Not including classes you are currently taking):  \n"))
    newstudent.currentGPA = float(input("What is your current GPA? (Not including classes you are currently taking):  \n"))
    newstudent.desiredGPA = float(input("What is your desired GPA:  \n"))
    newstudent.remainingCreditHours = int(input("How many credit hours do you have remaining (Not including classes you are currently taking):  \n"))
    
    #asks if you are currently taking classes
    check2 = 0
    while check2 < 1:
        newstudent.takingClasses = input("Are you currently taking classes? (Yes or No)  \n")
        if newstudent.takingClasses.upper() == "YES" or newstudent.takingClasses.upper() == "NO":
            check2 = 1
            newstudent.takingClasses == newstudent.takingClasses.upper()
        else:
            print("incorrect format")
            
    #Checks to see how many classes a person is taking
    newstudent.numOfClasses = 0
    if newstudent.takingClasses.upper() == "YES":
        newstudent.numOfClasses = int(input("How many classes are you taking?  \n"))    

    #Gets the list of classes
    for i in range(newstudent.numOfClasses):
        newstudent.classesName.append(input("Put the name of a class you are taking. \n"))
        newstudent.classesGrade.append(input("What letter grade do you plan to make? \n"))
        newstudent.classesHours.append(int(input("How many credit hours will you receive for this class? \n")))
    letters(newstudent.numOfClasses, newstudent.classesGrade ,newstudent.classesHours)
    return newstudent.name, newstudent.schoollevel, newstudent.studentID, newstudent.currentCreditHours, \
        newstudent.currentGPA, newstudent.desiredGPA, newstudent.remainingCreditHours, \
            newstudent.takingClasses, newstudent.numOfClasses, newstudent.classesName, newstudent.classesGrade, newstudent.classesHours

name, schoollevel, studentID, currentCreditHours, \
        currentGPA, desiredGPA, remainingCreditHours, \
            takingClasses, numOfClasses, classesName, classesGrade, classesHours = create_student()

#Using the 3 differnt grading scales to determine their GPA from the courses above based off quality hours 
neededGrade = (desiredGPA*(currentCreditHours+sum(classesHours)+remainingCreditHours)-currentGPA*currentCreditHours-qualityPoints)/remainingCreditHours
#desiredGPA = (currentGPA*currentCreditHours + qualityPoints(this is already classInput1*classesHours) + neededGPA*remainingCreditHours) / (currentCreditHours + CurrentlyTakingClassHours + remainingHours)
print("Hi, "+name+" after this semester, you need to get at least",neededGrade," to achieve your desired GPA")
