'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer "e" at position i.
print: Print the list.
remove e: Delete the first occurrence of integer "e".
append e: Insert integer "e" at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of N followed by N lines of commands where each 
command will be of the 7 types listed above. Iterate through each command in order and perform 
the corresponding operation on your list.

'''

N = int(input("Numero de comandos: "))
list = [None]*10000
for i in range(N):
  command = input("Digite o comando: ").split()
  if command[0] == 'insert':
    exec('list' + '.' + command[0] + '(' + command[2] + ',' + command[1] + ')')
  elif command[0] == 'print':
    exec('print' + '(' + 'list' + ')')
  elif command[0] == 'remove':
    exec('list' + '.' + command[0] + '(' + command[1] + ')')
  elif command[0] == 'append':
    exec('list' + '.' + command[0] + '(' + command[1] + ')')
  elif command == 'sort':
    exec('list' + '.' + command[0] + '(' + ')')
  elif command[0] == 'pop':
    exec('list' + '.' + command[0] + '(' + ')')
  else:
    exec('list' + '.' + command[0] + '(' + ')')

pass