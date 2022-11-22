import sys
def whoami():
	print("\n" + " ATTENTION ".center(80, "*") + "\n")
	print("%s/%s%s" %("The function is \n" + sys._getframe(1).f_code.co_filename, sys._getframe(1).f_code.co_name, "\nand the line number is " + str(sys._getframe(1).f_lineno)))
	print ("\n" + "*"*80)

