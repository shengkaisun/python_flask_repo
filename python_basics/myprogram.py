from mymodule import my_func

my_func()

#from MyFirstPackage import main_script
from MyFirstPackage.SubPackage import subscript

#main_script.report_name()

subscript.sub_report()

# Directly import a function
from MyFirstPackage.main_script import report_name
report_name()

