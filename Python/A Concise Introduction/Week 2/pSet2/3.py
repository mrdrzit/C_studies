ne = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]
def problem2_3(ne):
    for state in range(len(ne)):
        print(ne[state]," has ",len(ne[state])," letters.",sep='')