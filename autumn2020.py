# UTS grade distributions
grade_distributions = {"Fail": range(0, 49), "Pass": range(50, 64), "Credit": range(65, 74), "Distinction": range(75, 84), "High Distinction": range(85, 100)}

# Courses being taken
autumn_courses_2020 = ("31272 Project Management and the Professional", "41025 Introduction to Software Development","41182 System Security", "31277 Routing and Switching Essentials")

# Excluding PMP
assessment_count = {autumn_courses_2020[1]: 3, autumn_courses_2020[2]: 3, autumn_courses_2020[3]: 3}

# Assessment weighting
pmp_assessment_weighting = {"Assessment 1": "{:.0%}".format(0.2), "Assessment 2": "{:.0%}".format(0.3), "Assessment 3": "{:.0%}".format(0.1), "Assessment 4": "{:.0%}".format(0.4)}
isd_assessment_weighting = {"Assessment 1": "{:.0%}".format(0.3), "Assessment 2": "{:.0%}".format(0.5), "Assessment 3": "{:.0%}".format(0.2)}
rse_assessment_weighting = {"Assessment 1": "{:.0%}".format(0.4), "Assessment 2": "{:.0%}".format(0.45), "Assessment 3": "{:.0%}".format(0.15)}
ss_assessment_weighting = {"Assessment 1": "{:.0%}".format(0.4), "Assessment 2": "{:.0%}".format(0.4), "Assessment 3": "{:.0%}".format(0.2)}

# Default information view
print("Autumn 2020 Assessment Overview:\n")

# Project Management and the Professional
# Display current percentage
default_percentage = "{:.0%}".format(0.0)
a1_max = 20
a1_weight = 20
a1_score = input("What did you score on Assessment 1? ")
a1_final = ((float(a1_score) / float(a1_max) * float(a1_weight)))

a2_max = 30
a2_weight = 30
a2_score = input("What did you score on Assessment 2? ")
a2_final = ((float(a2_score) / float(a2_max) * float(a2_weight)))

print(autumn_courses_2020[0] + ": 4")
for a in pmp_assessment_weighting:
    print(a, pmp_assessment_weighting[a])
print("Current Percentage: " + str(a1_final + a2_final))
print("Current Grade: \n")

# Introduction to Software Development
print(autumn_courses_2020[1] + ": 3")
for b in isd_assessment_weighting:
    print(b, isd_assessment_weighting[b])
print("Current Percentage: " + default_percentage)
print("Current Grade: \n")

# System Security
print(autumn_courses_2020[2] + ": 3")
for c in ss_assessment_weighting:
    print(c, ss_assessment_weighting[c])
print("Current Percentage: "  + default_percentage)
print("Current Grade: \n")

# Routing and Switching Essentials
print(autumn_courses_2020[3] + ": 3")
for d in rse_assessment_weighting:
    print(d, rse_assessment_weighting[d])
print("Current Percentage: "  + default_percentage)
print("Current Grade: \n")
