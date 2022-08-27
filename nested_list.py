# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# Input Format

# The first line contains an integer,N , the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.

for _ in range(int(input("enter the number of student:--"))):
    name = input("name of the student:--")
    score = float(input("grade of the student:--"))
    new_list = set(score)
    new_list.remove(min(new_list))
print(min(new_list))
