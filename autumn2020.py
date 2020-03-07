# UTS grade distributions
grade_distributions = {"Fail": range(0,50), "Pass": range(50,64), "Credit": range(65,74), "Distinction": range(75, 84), "High Distinction": range(85,100)}

autumn_courses_2020 = ("31272 Project Management and the Professional", "41025 Introduction to Software Development", "41182 System Security", "31277 Routing and Switching Essentials")

assessment_count = {autumn_courses_2020[1]: 3, autumn_courses_2020[2]: 3, autumn_courses_2020[3]: 3}
print("Assessment Count: \n")
print(autumn_courses_2020[0] + ": 4")
for subject in assessment_count:
    print(subject + ": 3") 

# Final grade calculation
def calculate_grade():
    pass

# Output results
# for subject in autumn_courses_2020:
#     print(subject[0:] + ":") 
#     print("Current Percentage: \n")
#     print("Total Course Percentage: \n")
#     print("Current Grade: \n")