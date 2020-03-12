# NOTE: Script needs to be rearchitected
# We took the easy way out

# UTS grade distributions
grade_distributions = {"Fail": range(0, 49), "Pass": range(50, 64), "Credit": range(
    65, 74), "Distinction": range(75, 84), "High Distinction": range(85, 100)}

# Courses being taken
autumn_courses_2020 = ("31272 Project Management and the Professional", "41025 Introduction to Software Development",
                       "41182 System Security", "31277 Routing and Switching Essentials")

# Excluding PMP
assessment_count = {
    autumn_courses_2020[1]: 3, autumn_courses_2020[2]: 3, autumn_courses_2020[3]: 3}

# Assessment weighting
pmp_assessment_weighting = {"Assessment 1:": "{:.0%}".format(0.2), "Assessment 2:": "{:.0%}".format(
    0.3), "Assessment 3:": "{:.0%}".format(0.1), "Assessment 4:": "{:.0%}".format(0.4)}
isd_assessment_weighting = {"Assessment 1:": "{:.0%}".format(
    0.3), "Assessment 2:": "{:.0%}".format(0.5), "Assessment 3:": "{:.0%}".format(0.2)}
rse_assessment_weighting = {"Assessment 1:": "{:.0%}".format(
    0.4), "Assessment 2:": "{:.0%}".format(0.45), "Assessment 3:": "{:.0%}".format(0.15)}
ss_assessment_weighting = {"Assessment 1:": "{:.0%}".format(
    0.4), "Assessment 2:": "{:.0%}".format(0.4), "Assessment 3:": "{:.0%}".format(0.2)}

# Default information view
print("Autumn 2020 Assessment Overview:\n")
# Display current percentage
default_percentage = "{:.0%}".format(0.0)

# Project Management and the Professional
a1_max = 20
a1_weight = 20
# Update score here
a1_score = 0
a1_final = ((float(a1_score) / float(a1_max) * float(a1_weight)))

a2_max = 30
a2_weight = 30
# Update score here
a2_score = 0
a2_final = ((float(a2_score) / float(a2_max) * float(a2_weight)))

a3_max = 10
a3_weight = 10
# Update score here
a3_score = 0
a3_final = ((float(a3_score) / float(a3_max) * float(a3_weight)))

a4_max = 40
a4_weight = 40
# Update score here
a4_score = 0
a4_final = ((float(a4_score) / float(a4_max) * float(a4_weight)))

print(autumn_courses_2020[0] + ": 4")
for a in pmp_assessment_weighting:
    print(a, pmp_assessment_weighting[a])
print("Current Percentage: " + str(a1_final + a2_final + a3_final + a4_final) + "%")
print("Current Grade: \n")

# Introduction to Software Development
b1_max = 30
b1_weight = 30
# Update score here
b1_score = 0
b1_final = ((float(b1_score) / float(b1_max) * float(b1_weight)))

b2_max = 50
b2_weight = 50
# Update score here
b2_score = 0
b2_final = ((float(b2_score) / float(b2_max) * float(b2_weight)))

b3_max = 20
b3_weight = 20
# Update score here
b3_score = 0
b3_final = ((float(b3_score) / float(b3_max) * float(b3_weight)))

print(autumn_courses_2020[1] + ": 3")
for b in isd_assessment_weighting:
    print(b, isd_assessment_weighting[b])
print("Current Percentage: " + str(b1_final + b2_final + b3_final) + "%")
print("Current Grade: \n")

# System Security
c1_max = 40
c1_weight = 40
# Update score here
c1_score = 0
c1_final = ((float(c1_score) / float(c1_max) * float(c1_weight)))

c2_max = 40
c2_weight = 40
# Update score here
c2_score = 0
c2_final = ((float(c2_score) / float(c2_max) * float(c2_weight)))

c3_max = 20
c3_weight = 20
# Update score here
c3_score = 0
c3_final = ((float(c3_score) / float(c3_max) * float(c3_weight)))

print(autumn_courses_2020[2] + ": 3")
for c in ss_assessment_weighting:
    print(c, ss_assessment_weighting[c])
print("Current Percentage: " + str(c1_final + c2_final + c3_final) + "%")
print("Current Grade: \n")

# Routing and Switching Essentials
d1_max = 40
d1_weight = 40
# Update score here
d1_score = 0
d1_final = ((float(d1_score) / float(d1_max) * float(d1_weight)))

d2_max = 45
d2_weight = 45
# Update score here
d2_score = 0
d2_final = ((float(d2_score) / float(d2_max) * float(d2_weight)))

d3_max = 15
d3_weight = 15
# Update score here
d3_score = 0
d3_final = ((float(d3_score) / float(d3_max) * float(d3_weight)))

print(autumn_courses_2020[3] + ": 3")
for d in rse_assessment_weighting:
    print(d, rse_assessment_weighting[d])
print("Current Percentage: " + str(d1_final + d2_final + d3_final) + "%")
print("Current Grade: \n")
