# 48024 Applications Programming as example
total_assessment_percentage = 100

# Assessments 
assessment_one_weight = 15
one_max = 10

assessment_two_weight = 30
two_max = 30

assessment_three_weight = 20
three_max = 20

assessment_four_weight = 35
four_max = 35

total_weight = assessment_one_weight + assessment_two_weight + assessment_three_weight + assessment_four_weight

result_one = input("Enter assessment 1 score: ")
a1_final = (float(result_one) / float(one_max) * float(assessment_one_weight))
print(round(a1_final, 2))

print('Total Course Percentage: ' + str(a1_final))