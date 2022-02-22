## Docket

Docket is a command-line (CLI) application that lets you manage your tasks. Generally, docket means a list of cases/tasks for trial. 

## Project Structure
```
root
|
|
Docket___completed.txt
     |___docket.bat
     |___docket.py
     |___docket.sh
     |___task.txt
     |___package-lock.json
|
|___README.md
```
## Prerequisite

1. Install python (python3 recommanded)
--> you can install python using following link https://installpython3.com/

2. Terminal / command prompt/ Windows PowerShell

## How to use?

-> Fork this repository 

-> Open your git bash in an empty folder.
-> Clone this repository or run the following command in git bash

```
git clone https://github.com/DiyaVj/Docket.git 
```

-> On your machine, you should notice a folder called "Docket."

-> Once the repository has been cloned in your system, open the command prompt/window powershell and navigate to the folder where you cloned this repo. To open the desired location in command prompt/window powershell, type the following command.

``` 
cd \Loation\Docket\
```

-> Cheers! You can now use docket, run the programme, and have fun!!

## Specification

1. Docket app should be execute by running the following command from the terminal.

   **On Windows:**

   ```
   .\docket.bat
   ```

   **On linux:**

   ```
   ./docket.sh
   ```

2. The app should read from and write to a task.txt text file.

3. Completed task are writted to a completed.txt file. 

## Commands

**1. Use ```add``` command to add a task.**

```
./docket add "Hello World!" 
```
OUTPUT:
``` Added task: Hello World!```

**2. Use ```ls``` command to get list of pending items.**
``` 
./docket ls 
```
OUTPUT:
``` 1. Hello World! ```

**3. Use ```del INDEX``` command to delete incomplete item using its index.**
``` 
./docket del 1 
```
OUTPUT:
``` Deleted item with index 1 ```

**4. Use ```done INDEX``` command to mark pending item as completed.**
```
./docket done 1 
```
OUTPUT:
``` Marked item as done. ```

**5. Use ```help``` command for help. This command will show you all the commands and their uses.**
```
./docket help
```

**6. Use ```report``` command to display full report/status of your docket.**
``` 
./docket report 
```
OUTPUT:
``` Pending tasks:0 \n Completed tasks:1 ```

<hr>

Create your own docket. Read more information about project on [my dev post](https://dev.to/diyavj/docket-a-cli-application-1o2a) or [Tealfeed](https://tealfeed.com/diya_345977).
