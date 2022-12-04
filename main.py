from flask import Flask, render_template,request,redirect,url_for
# from flask_migrate import migrate
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
import sqlite3
from enum import Enum
db=sqlite3.connect("Todo_list.db",check_same_thread=False)
db.execute("create table if not exists tasks (title text,discription text,status text,deadline date,important bool)")
cr=db.cursor()


todo_list_app=Flask(__name__)


db=sqlite3.connect("Todo_list.db",check_same_thread=False)
db.execute("create table if not exists tasks (title text,discription text,status text,deadline date,important bool)")


@todo_list_app.route("/")
def homepage():
    return render_template("index.html",title="Todo List")

@todo_list_app.route("/add task")
def add_task():
    return render_template("add_task.html",
                           title="Add Task",
                           custom_css="add_task")
    


@todo_list_app.route("/save_task", methods=("GET","POST"))
def save_task():

    title=request.form.get("title")
    discription=request.form.get("discription")
    status=request.form.get("status")
    deadline=request.form.get("deadline")
    important=request.form.get("important")
    with sqlite3.connect("Todo_list.db",check_same_thread=False) as con:
        cur=con.cursor()
        cur.execute("insert into tasks (title,discription,status,deadline,important) values (?,?,?,?,?)",(title,discription,status,deadline,important) )
        con.commit()
    msg="Added"    
            
    return render_template("add_task.html",title="Add Task",
                           custom_css="add_task",msg=msg)
                
@todo_list_app.route("/all tasks")
def all_tasks():
    row=[]
    cr.execute("select * from tasks")
    row=cr.fetchall() 
    return render_template("all_tasks.html",
                            title="All Tasks",
                            custom_css="all_tasks",
                            row=row)   

@todo_list_app.route("/todo")
def todo_tasks():
    return render_template("todo_tasks.html")  

@todo_list_app.route("/progress")
def progress_tasks():
    return render_template("progress_tasks.html")  

@todo_list_app.route("/done")
def done_tasks():
    return render_template("done_tasks.html")  

@todo_list_app.route("/important")
def important_tasks():
    return render_template("important_tasks.html")  

if  __name__== "__main__":
    todo_list_app.run(debug=True)
    
    

# db=sqlite3.connect("Todo_list.db")
# db.execute("create table if not exists tasks (title text,discription text,status text,deadline date,important bool)")
# cr=db.cursor()




# class Status(Enum):
#     todo=1
#     progress=2
#     done=3   

# class Tasks_manager:
#     def __init__(self,title:str,discription:str,Status:Enum,deadline:date,important:bool):
#         self.title=title
#         self.discription=discription
#         self.Status=Status
#         self.deadline=deadline
#         self.important=important

#     def add_task(self):
#         cr.execute(f"insert into tasks (title,discription,status,deadline,important) values('{self.title}','{self.discription}','{self.Status}','{self.deadline}','{self.important}')")
#         db.commit()
#         print(f"Add Task:{self.title}")
         
    
#     def delete_task(task_title):
#         cr.execute(f"delete from tasks where title='{task_title}'")
#         db.commit()
#         print(f"----Deleted Task:{task_title}----")  
        
    
#     def show_alltasks():
#         print("----All Tasks:----")
#         cr.execute("select title from tasks")
#         db.commit()  
#         for task in cr.fetchall():
#             task[0] 

#     def update_task(task_title,new_Status): #update status
#         cr.execute(f"update tasks set status='{new_Status}' where title='{task_title}'")
#         db.commit() 
#         print(f"Update Task: {task_title} ==> New Status: {new_Status}")
    
    
#     def show_important_tasks():
#         print("----Important Tasks:----")
#         cr.execute("select title from tasks where important='True'")
#         db.commit()  
#         for task in cr.fetchall():
#             print(task[0])
      
    
#     def show_done_tasks():
#         print("----Done Tasks:----")
#         cr.execute("select title from tasks where status='done'")
#         db.commit()  
#         for task in cr.fetchall():
#             print(task[0])
        
          
#     def show_todo_tasks():
#         print("----Todo Tasks:----")
#         cr.execute("select title from tasks where status='todo'")
#         db.commit()  
#         for task in cr.fetchall():
#             print(task[0])
       
        
#     def show_progress_tasks():
#         print("----Progress Tasks:----")
#         cr.execute("select title from tasks where status='progress'")
#         db.commit()  
#         for task in cr.fetchall():
#             print(task[0])
       
        

# task1=Tasks_manager("training","python training",str(Status(3).name),date(2022,12,22),"False")
# # task2=Tasks_manager("learn python","ww",str(Status(2).name),"2022,12,22","True")
# # task3=Tasks_manager("reading","ww",str(Status(1).name),"2022,12,22","True")
# # task4=Tasks_manager("runing","ww",str(Status(1).name),"2022,12,22","False")
# # Tasks_manager.add_task(task1)
# # Tasks_manager.add_task(task2)
# # Tasks_manager.add_task(task3)
# # Tasks_manager.add_task(task4)
# Tasks_manager.update_task("training",Status(3).name)
# Tasks_manager.show_todo_tasks()
# Tasks_manager.show_progress_tasks()
# Tasks_manager.show_alltasks()
# Tasks_manager.show_important_tasks()
# Tasks_manager.show_done_tasks()
# # Tasks_manager.delete_task("reading")















   
