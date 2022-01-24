import argparse

task = open("task.txt","r+")
completed_task = open("completed.txt", "r+")

task_data = task.readlines()
completed_data = completed_task.readlines()
c=len(completed_data)
t= len(task_data)

parser= argparse.ArgumentParser()


parser.add_argument('input1',
action='store', type=str, nargs='?', default='default')

parser.add_argument('input2', action = 'store',
                    nargs='?',
                    default='-1')

args = parser.parse_args()
        

if(args.input1 == 'default' or args.input1 == 'help'):
    print('''Usage :-
$ ./docket add "hello world"    # Add a new item with priority 2 and text "hello world" to the list
$ ./docket ls                   # Show incomplete list items
$ ./docket del INDEX            # Delete the incomplete item with the given index
$ ./docket done INDEX           # Mark the incomplete item with the given index as complete
$ ./docket help                 # Show usage
$ ./docket report               # Statistics''')
        

# Add a new item

elif(args.input1 == 'add' and args.input2 != '-1'):
    task.write(str(args.input2) +"\n")
    print('Added task: '+ (args.input2))

# List all pending items

elif(args.input1 == 'ls'and t>0):
    for i in range(t,0,-1):
        line = task_data[i-1].strip()
        print(str(i)+'. '+line)
        
elif(args.input1 == 'ls'):
    print("There are no pending tasks!")


# Delete an item

elif(args.input1 == 'del' and args.input2 != '-1' and int(args.input2) <= t and int(args.input2)>0):
    task_data.remove(task_data[int(args.input2)-1])
    task.truncate(0)
    task.seek(0)
    for line in task_data:
        line = line.strip()
        task.write(line+"\n")
    print('Deleted item with index '+(args.input2))

elif(args.input1 == 'del'):
    print("Error: item with index "+str(int(args.input2))+" does not exist. Nothing deleted.")

# Mark a task as complete

elif(args.input1 == 'done' and args.input2 != '-1' and int(args.input2) <= t and int(args.input2)>0):
    line = task_data[int(args.input2)-1]
    completed_task.write(task_data[int(args.input2)-1])
    task_data.remove(task_data[int(args.input2)-1])
    task.truncate(0)
    task.seek(0)
    for line in task_data:
        line = line.strip()
        task.write(line+"\n")
    print('Marked item as done.')

elif(args.input1 == 'done'):
    print("Error: no incomplete item with index "+str(int(args.input2))+" exists.")
 
# Generate a Report 

elif(args.input1 == 'report'):
    print("Pending tasks: "+ str(t))
    for i in range(t,0,-1):
        line = task_data[i-1].strip()
        print(str(i)+'. '+ line )
    print("Completed tasks: "+ str(c))
    for i in range(c,0,-1):
        line = completed_data[i-1].strip()
        print(str(i)+'. '+ line )