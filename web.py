import streamlit as stl
import function as fcn

todos = fcn.get_todos()


def add_todo():
    todo = stl.session_state["new_todo"] + "\n"
    todos.append(todo)
    fcn.write_todos(todos)


stl.title("To do App")
stl.subheader("My Todo App")
stl.write("This app will help to increase productivity")

for index, todo in enumerate(todos):
    checkbox = stl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fcn.write_todos(todos)
        del stl.session_state[todo]
        stl.experimental_rerun()

stl.text_input(label="", placeholder="Add a new todo",
               on_change=add_todo, key="new_todo")

