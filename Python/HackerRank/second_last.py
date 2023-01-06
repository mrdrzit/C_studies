'''
Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''

if __name__ == '__main__':
    students = [['Prashant',32], ['Pallavi',36], ['Dheeraj',39], ['Shivam',40]]
    sortd = sorted(students, key=lambda x: x[1], reverse=True)
    same = []
    [sortd.remove(item) for item in sortd[:] if item[1] == sortd[-1][1]]
    [same.append(item[0]) for item in sortd if item[1] == sortd[-1][1]]
    same = sorted(same)
    for name in same:
      print(name)
