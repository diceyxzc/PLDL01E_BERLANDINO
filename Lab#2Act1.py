#Start.

#Intialize final grade and equivalent grading remark.
finalGrade = 0
equivalentGrading = 0

#Input the student's name, final quizzes, research/assignment, project, and exam ratings.
studentName = str(input("Student's Name:"))
finalQuizzes = float(input("Final Quizzes Rating:"))
finalResearchAssignment = float(input("Final Research/Assignment Rating:"))
finalProject = float(input("Final Project Rating:"))
finalExam = float(input("Final Exam Rating:"))

#Compute final grade.
finalGrade = finalQuizzes * 0.30 + finalResearchAssignment * 0.10 + finalExam * 0.40 + finalProject * 0.20
finalGradeDecimal = "{:.2f}".format(finalGrade)

#Convert final grade to equivalent grading remark.
if 98 <= finalGrade <= 100:
    equivalentGrading = 4.00
elif 95 <= finalGrade <= 97:
    equivalentGrading = 3.75
elif 92 <= finalGrade <= 94:
    equivalentGrading = 3.50
elif 89 <= finalGrade <= 91:
    equivalentGrading = 3.25
elif 86 <= finalGrade <= 88:
    equivalentGrading = 3.00
elif 83 <= finalGrade <= 85:
    equivalentGrading = 2.75
elif 80 <= finalGrade <= 82:
    equivalentGrading = 2.50
elif 77 <= finalGrade <= 79:
    equivalentGrading = 2.25
elif 74 <= finalGrade <= 76:
    equivalentGrading = 2.00
elif 71 <= finalGrade <= 73:
    equivalentGrading = 1.75
elif 68 <= finalGrade <= 70:
    equivalentGrading = 1.50
elif 64 <= finalGrade <= 67:
    equivalentGrading = 1.25
elif 60 <= finalGrade <= 63:
    equivalentGrading = 1.00
elif finalGrade < 60:
    equivalentGrading = 0.00
elif finalGrade > 100:
    equivalentGrading = str("Invalid Grading Remark")

#Display student's evaluation.
print("---Student's Evaluation---")
print("Student's Name:", studentName)
print("Final Quizzes Rating:", finalQuizzes)
print("Final Research/Assignment Rating:", finalResearchAssignment)
print("Final Projects Rating:", finalProject)
print("Final Exam Rating:", finalExam)
print("Final Semestral Grade:", finalGradeDecimal)
print("Equivalent Grading Remark:", equivalentGrading)

#End.