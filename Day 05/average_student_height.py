# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
height = 0
number_of_students = 0

for height in student_heights:
  total_height += height

for students in student_heights:
  number_of_students += 1

average_height = round(total_height / number_of_students)

print(f"total height = {total_height} \nnumber of students = {number_of_students}\naverage height = {average_height}")

