# Insert a chat message container.

import streamlit as st
import replicate


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def model_response(prompt):
    for event in replicate.stream(
        "meta/meta-llama-3.1-405b-instruct",
        input={
            "prompt": prompt,
            "max_tokens": 1024,
            "system_prompt": "Du bist der freundliche und wissensreiche BirdBot. Ein Voll-Experte und leidenschaftlicher Ornithologe.",
        },
    ):
        yield str(event)


def get_history(new_prompt):
    history = ""
    for message in st.session_state.messages:
        if message["role"] == "user":
            history += f"User: {message['content']}\n"
        else:
            history += f"BirdBot: {message['content']}\n"
    return history + new_prompt


# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("ai"):
        response = st.write_stream(model_response(get_history(prompt)))
    st.session_state.messages.append({"role": "ai", "content": response})
