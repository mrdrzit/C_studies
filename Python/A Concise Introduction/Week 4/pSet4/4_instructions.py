"""
Problem 4_4:
This problem is to build on phones.py.  You add a new menu item
  r) Reorder
This will reorder the names/numbers in the phone list alphabetically by name. 
This may sound difficult at first thought, but it really is straight forward.  
You need to add two lines to the main_loop and one line to menu_choice to print 
out the new menu option (and add 'r' to the list of acceptable choices).  In 
addition you need to add a new function to do the reordering: I called mine
reorder_phones(). Here is a start for this very short function:

def reorder_phones():
    global phones       # this insures that we use the one at the top
    pass # replace this pass (a do-nothing) statement with your code


Note: The auto-grader will run your program, choose menu items s, r, s, and q
in that order.  It will provide an unsorted CSV file and see if your program
reorders it appropriately. The grader will provide a version of myphones.csv
that has a different set of names in it from the ones we used in the lesson. 
This difference in data will, of course, not matter with a well coded program.
Below the result of this added function is shown using the names used in class.
Note that name is a single field.  Reorder by that field, don't try to separate
first and last name and reorder by one or the other --- just treat name as a 
single field that you re-order by.  Also, in this case upper/lower case won't
matter.

TIP: phones[] is a list of lists (each sublist is a [name, phone].  It looks 
complicated to sort.  Just pretend that each sublist is a single name item and
code it accordingly.  It will work.  This is a beginner course and this sort
function requires only one line and no fancy outside material to make it work.)
The main thrust of this problem is to add in the various pieces to make a new
menu entry.

Before:
Choice: s
     Name                     Phone Number 
  1  Jerry Seinfeld          (212) 842-2527
  2  George Costanza         (212) 452-8145
  3  Elaine Benes            (212) 452-8723
After:
Choice: s
     Name                     Phone Number 
  1  Elaine Benes            (212) 452-8723
  2  George Costanza         (212) 452-8145
  3  Jerry Seinfeld          (212) 842-2527

"""