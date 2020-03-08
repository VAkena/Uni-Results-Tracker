# UTS grade distributions
grade_distributions = {"Fail": range(0, 49), "Pass": range(50, 64), "Credit": range(
    65, 74), "Distinction": range(75, 84), "High Distinction": range(85, 100)}

autumn_courses_2020 = ("31272 Project Management and the Professional", "41025 Introduction to Software Development",
                       "41182 System Security", "31277 Routing and Switching Essentials")

assessment_count = {
    autumn_courses_2020[1]: 3, autumn_courses_2020[2]: 3, autumn_courses_2020[3]: 3}
# Assessment weighting
pmp_assessment_weighting = {"Assessment 1": "{:.0%}".format(0.2), "Assessment 2": "{:.0%}".format(
    0.3), "Assessment 3": "{:.0%}".format(0.1), "Assessment 4": "{:.0%}".format(0.4)}
isd_assessment_weighting = {"Assessment 1": "{:.0%}".format(
    0.3), "Assessment 2": "{:.0%}".format(0.5), "Assessment 3": "{:.0%}".format(0.2)}
rse_assessment_weighting = {"Assessment 1": "{:.0%}".format(
    0.4), "Assessment 2": "{:.0%}".format(0.45), "Assessment 3": "{:.0%}".format(0.15)}
ss_assessment_weighting = {"Assessment 1": "{:.0%}".format(
    0.4), "Assessment 2": "{:.0%}".format(0.4), "Assessment 3": "{:.0%}".format(0.2)}


def update_results():
    pass


def menu_options(i):
    switcher = {
        "v": view_progess(),
        "u": update_results()
    }
    return switcher.get(i, "Please try again!")


user_choice = input("What do you want to do? Choice (v/u/x): ")


def view_progess():
    # Default information view
    print("Autumn 2020 Assessment Overview:\n")
    print(autumn_courses_2020[0] + ": 4")
    for a in pmp_assessment_weighting:
        print(a, pmp_assessment_weighting[a])
    print("Current Percentage:")
    print("Current Grade: \n")

    print(autumn_courses_2020[1] + ": 3")
    for b in isd_assessment_weighting:
        print(b, isd_assessment_weighting[b])
    print("Current Percentage:")
    print("Current Grade: \n")

    print(autumn_courses_2020[2] + ": 3")
    for c in ss_assessment_weighting:
        print(c, ss_assessment_weighting[c])
    print("Current Percentage:")
    print("Current Grade: \n")

    print(autumn_courses_2020[3] + ": 3")
    for d in rse_assessment_weighting:
        print(d, rse_assessment_weighting[d])
    print("Current Percentage:")
    print("Current Grade: \n")

# user_choice = input("What do you want to do? Choice (v/u/x/h): ")
# while user_choice != 'x':
#     if user_choice == 'v':
#         view_progess()
#     else:
#         user_choice()
