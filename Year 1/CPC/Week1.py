# n = int(input())
# temperatures = input()
# split_temps = temperatures.split()
# int_temps = [int(temp) for temp in split_temps]

# min_temp = 100
# min_day = -1
# for i in range(len(int_temps) - 3):
#     first = int_temps[i]
#     third = int_temps[i + 2]
#     max_temp = max(first, third)
#     if max_temp < min_temp:
#         min_temp = max_temp
#         min_day = i + 1
        
# print(min_day, min_temp)

# Problem 2
# n = input()
# grading_list = [int(grade) for grade in n.split()]

# grade_recieved = int(input())
# letter_grade = "A"

# for i in range(len(grading_list)):
#     if grade_recieved < grading_list[len(grading_list) - 1]:
#         letter_grade = "F"
#         break
#     elif grade_recieved < grading_list[i] and grade_recieved != grading_list[i]:
#         continue
#     match i:
#         case 0:
#             letter_grade = "A"
#         case 1:
#             letter_grade = "B"
#         case 2:
#             letter_grade = "C"
#         case 3:
#             letter_grade = "D"
#         case 4:
#             letter_grade = "E"
#         case _:
#             letter_grade = "F"
#     break

# print(letter_grade)

# Problem 3
# def eligibilityCheck(contestant_info):
#     date_of_post = contestant_info[1].split("/")
#     date_of_birth = contestant_info[2].split("/")
#     courses = contestant_info[3]

#     if int(date_of_post[0]) >= 2010 or int(date_of_birth[0]) >= 1991:
#         return 0
#     elif int(courses) >= 40:
#         return 1
#     elif (int(date_of_post[0]) < 2010) and int(date_of_birth[0]) < 1991 and int(courses) <= 40:
#         return 2
    
#     return 1

# n = input()
# for i in range(int(n)):
#     contestant_info = input().split()
#     isEligible = eligibilityCheck(contestant_info)

#     match isEligible:
#         case 0:
#             print(contestant_info[0], "eligible")
#         case 1:
#             print(contestant_info[0], "ineligible")
#         case 2:
#             print(contestant_info[0], "coach petitions")

# Problem 4
# n = int(input())

# for i in range(n):
#     calories_needed = input()
#     print(int(int(calories_needed) / 400))

# Problem 5
h = int(input())
k = int(input())
dance = {}

for i in range(h):
    dance[i] = input()
    
def readLine(lineIndex):
    current_line = dance[lineIndex]
    for i in range(k):
        if current_line[i] == "$":
            if lineIndex == len(dance):
                continue
            else:
                readLine(len(dance))
        else:
            read(Line)