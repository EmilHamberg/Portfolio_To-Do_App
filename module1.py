from random import choice
import datetime
from datetime import calender
import tkinter
from tkinter import *


tasks=[]
tags=[]

def add_task():
    task=input("Enter new task: ")
    tasks.append(task)
    print("Task added")
    
def view_tasks():
    if len(tasks)==0:
        print("To-Do list empty")
    else:
        print("To-Do list: ")
        for i, task in enumerate(tasks):
            print(f'{i+1}, {task}')
            
def delete_task():
    if len(tasks)==0:
        print('No tasks to delete')
    else:
        print('Tasks: ')
        for i, task in enumerate(tasks):
            print(f'{i+1}, {task}')
        choice = int(input('Enter tasknumber to delete: '))
        
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print('Task deleted.')
        else:
            print('Invalid task number.')
            
def prioritizing():
    # Give priority to the tasks, organizing them after priority

    def tags():
    # Allow user to give tasks a tag from premade list
        if len(tags)==0:
         print('No avaialble tags.')
        elif tags <= 0:
         print('Following tags are available')
         print('Choose tag for task.')
    # Allow user to make custom tags 
    # When user assign tags, let them choose 'Custom'
    # Save custom tag in taglist
    #if

def reminder():
    # give the option to set a reminder 

    def main():
     while True:
        print('\n***** To-Do-List application *****')
        print('1: Add task')
        print('2: View tasks')
        print('3: Delete task')
        print('4: Quit')
        
    choice=int(input('Enter choice: '))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        print('Thanks for using the To-Do application')
        #break
    else:
        print('Invalid choice. Please try again')