import sys
from termcolor import colored
def whoami():
	print("\n" + colored(" ATTENTION ", "green").center(80, "*") + "\n")
	print("%s/%s%s" %("The function is \n" + sys._getframe(1).f_code.co_filename, sys._getframe(1).f_code.co_name, "\nand the line number is " + str(sys._getframe(1).f_lineno)))
	print ("\n" + "*"*80)
	exit()

