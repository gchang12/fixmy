from fixmy.imports import *
from fixmy.prefixes import *
from fixmy.init_files import *

#	For use in fixing import statements for user-defined modules within parent module

#	Usual use of module as follows:

#	from fixmy.imports import fix_imports
#	fix_imports(replace=bool)

#	Replace 'from' import statements with bool = True and just copy the .py files with bool = False
#	Note: No functionality for 'import [module]' statements; created for personal use, and never imported this way.