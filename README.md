Python Scripts
===================
A collection of all the personal python scripts that I have made. 

Learning while making something useful.


----------

These scripts are written in python3.5 and are a bit machine specific i.e. work based on the layout of my folders and files.  


----------


[purge.py](https://github.com/robwayne/PythonScripts/tree/master/purge)
-------------
Removes the files on my computer that are located in certain directories. This works with `markForRemoval.py`. Removes all the marked files and folders, symbolic links from the disk. 

 **Usage:**		
 
 > 1. To run ***without*** any warnings or output:
- `$ ./purge.py`

 > 2. To run with ***limited*** output, output from purge.py itself only: 
	 - `$ ./purge.py -v` 
 
> 3. To view ***all*** of the script's activity as well as the verbose output of `markForRemoval.py`: 
	 - `$ ./purge.py -vv`
> 4. To start purging a specific directory tree provide the absolute path to the root folder of that tree as an optional argument:
		- `$ ./purge.py -p /path/to/directory`

----------

[markForRemoval.py](https://github.com/robwayne/PythonScripts/tree/master/markForRemoval)
-------------
A complementing script that works with `purge.py`. Renames files and folders that are unnecessary by marking them with a prefix of `delete_`. eg. `temp.txt` --> `delete_temp.txt`

 **Usage:**		
 
 > 1. To run ***without*** any warnings or output:
- `$ ./markForRemoval.py`
 
> 2. To view ***all*** of the script's activity:
	 - `$ ./markForRemoval.py -v`
> 3. To mark only items from a specific directory tree provide the absolute path to the root folder of that tree as an optional argument:
		- `$ ./markForRemoval.py -p /path/to/directory`
   

> Written with [StackEdit](https://stackedit.io/).
