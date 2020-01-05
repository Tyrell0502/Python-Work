def getCourse():
#creates dictionaries for the room number, instructor, and meeting time of the course
    roomNumbers = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244', 'CM241':'1411'}
    courseInstructor = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
    meetingTimes = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.', 'CS103':'10:00 a.m.', 'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}
    userCourseNumber = input('Enter your course number: ')
#using a try and except statement incase user enters a course that isnt in the dictionary
    try:
        print('Your room number is', roomNumbers[userCourseNumber])
        print('Your instructor is', courseInstructor[userCourseNumber])
        print('Your meeting time for this class is', meetingTimes[userCourseNumber])
    except KeyError:
        print('This is not a valid course, try again.')
        
def main():
    getCourse()
    
main()
