import streamlit as st
import function

todos = function.get_todos()

st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("My Todo App")
st.subheader("this is a todo app")
st.write("this will help you to increase your <b>productivity</b>",
         unsafe_allow_html=True)

st.text_input(label="ADD TODO HERE",placeholder="Add new todo...",
                      on_change=add_todo, key="new_todo")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)


