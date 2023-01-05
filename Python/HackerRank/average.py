'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

The first line contains the integer n, the number of students' records. 
The next n lines contain the names and marks obtained by a student, 
each value separated by a space. 
The final line contains query_name, the name of a student to query.
'''

if __name__ == '__main__':
  # n = int(input())
  # for _ in range(n):
  #     name, *line = input().split()
  #     scores = list(map(float, line))
  #     student_marks[name] = scores
  # query_name = input()
  
  # create a dictionary with student names as keys and list of their scores as values
  student_marks = {"Krishna": [67, 68, 69],
                   "Arjun":   [70, 98, 63],
                   "Malika":  [52, 56, 60]}

  # get the name of the student whose scores we want to calculate
  query_name = "Malika"

  # calculate the mean of the student scores
  mean = sum(student_marks["Malika"])/len(student_marks["Malika"])

  # print the mean of the student scores
  print(f'{mean:.2f}')
  pass