Python Scripts
===================
A collection of all the personal python scripts that I have made. 

Learning while making something useful.


----------

These scripts are written in python3.5 and are a bit machine specific i.e. work based on the layout of my folders and files.  

> **N.B.**
	Assumes containing directory of all these scripts have been _**exported to the PATH**_.


----------


[purge.py](https://github.com/robwayne/PythonScripts/tree/master/purge)
-------------
Removes the files on my computer that are located in certain directories. This works with `markForRemoval.py`. Removes all the marked files and folders, symbolic links from the disk. 

 **Usage:**		
 
 > 1. To run ***without*** any warnings or output:
	- `$ purge.py`

 > 2. To run with ***limited*** output, output from purge.py itself only: 
	 - `$ purge.py -v` 
 
> 3. To view ***all*** of the script's activity as well as the verbose output of `markForRemoval.py`: 
	 - `$ purge.py -vv`
> 4. To start purging a specific directory tree provide the absolute path to the root folder of that tree as an optional argument:
		- `$ purge.py -p /path/to/directory`

----------

[markForRemoval.py](https://github.com/robwayne/PythonScripts/tree/master/markForRemoval)
-------------
A complementing script that works with `purge.py`. Renames files and folders that are unnecessary by marking them with a prefix of `delete_`. eg. `temp.txt` --> `delete_temp.txt`

 **Usage:**		
 
 > 1. To run ***without*** any warnings or output:
	- `$ markForRemoval.py`
 
> 2. To view ***all*** of the script's activity:
	 - `$ markForRemoval.py -v`
> 3. To mark only items from a specific directory tree provide the absolute path to the root folder of that tree as an optional argument:
		- `$ markForRemoval.py -p /path/to/directory`


   [checkDiskSpace.py](https://github.com/robwayne/PythonScripts/tree/master/checkDiskSpace)
-------------
A script that is run by the scheduleDiskCheck.sh bash script at 11:59 PM on a daily basis to determine whether or not the disk should be purged.

-	Checks the current remaining free space in GB. 
-	Calls [purge.py](purge.py) if the remaining free space is less than the current threshold (5GB). 
-	Takes no arguments. 

**Usage**:
	
- > `$ checkDiskSpace.py`
   
----------
> Written with [StackEdit](https://stackedit.io/).
