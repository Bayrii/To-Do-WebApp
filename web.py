import streamlit as st
import functions as fn

todos = fn.get_todos()

def add_todo():
    todo_local = st.session_state["new todo"] + "\n"
    todos.append(todo_local)
    fn.write_todos(todos)
    st.session_state["new todo"] = ""


st.title("🚀 Launch Your Day with Purpose")
st.subheader("Your tasks, tracked and tackled.")
st.write("This app helps you break big goals "
         "into small wins — one task at a time.")

with st.container(height=400):
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=f"{todo}-{index}")
        if checkbox:
            todos.pop(index)
            fn.write_todos(todos)
            del st.session_state[f"{todo}-{index}"]
            st.rerun()


st.text_input(label='Enter a todo',
              placeholder="Add new todo ...",
              on_change=add_todo, key="new todo")