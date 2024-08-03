import streamlit as st
import functions

todos = functions.get_todo()


def add_todo():
    add_todo  = st.session_state['new_todo'] + "\n"
    todos.append(add_todo)
    functions.write_todo(todos)
    st.session_state['new_todo'] = ''


st.title("My TODO App")
st.header("This is my daily todo app")
st.write("Use this todo app")
for index, mytodo in enumerate(todos):
    checkbox = st.checkbox(mytodo, key=mytodo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[mytodo]
        # st.experimental_rerun()
        st.write('<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)
st.text_input(label="", placeholder="Add a Todo", key="new_todo", on_change=add_todo)

