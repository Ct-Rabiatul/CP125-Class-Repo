#SITI RABIATUL ADAWIAH BINTI HUSSAIN


def determine_grade(mark):
    
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

#Student is grade information
def student_grade(mark):
    
    print(f"Mark : {mark:.1f}, Grade: {determine_grade(mark)}")


#Function call and prompt user to input student's mark
result = student_grade(mark= float(input("Enter the student's mark: ")))
