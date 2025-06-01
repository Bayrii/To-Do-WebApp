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


edit_index = st.session_state.get("edit_index")

with st.container(height=400):
    for index, todo in enumerate(todos):
        if edit_index == index:
            edited_todo = st.text_input("Edit todo", value=todo.strip(), key=f"edit-input-{index}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Save", key=f"save-{index}"):
                    todos[index] = edited_todo + "\n"
                    fn.write_todos(todos)
                    del st.session_state["edit_index"]
                    st.rerun()
            with col2:
                if st.button("Cancel", key=f"cancel-{index}"):
                    del st.session_state["edit_index"]
                    st.rerun()
        else:
            col1, col2 = st.columns(2)
            with col1:
                checkbox = st.checkbox(todo, key=f"{todo}-{index}")
                if checkbox:
                    todos.pop(index)
                    fn.write_todos(todos)
                    del st.session_state[f"{todo}-{index}"]
                    st.rerun()
            with col2:
                if st.button("Edit", key=f"edit-{index}"):
                    st.session_state["edit_index"] = index




st.text_input(label='Enter a todo',
              placeholder="Add new todo ...",
              on_change=add_todo, key="new todo")