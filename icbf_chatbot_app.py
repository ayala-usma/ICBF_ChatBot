# Importing required libraries
import time
import streamlit as st
import chatbot_methods

# Title of the Chatbot
st.title("ICBF Chatbot 💬🤖! (Unofficial)")
st.caption("by: Aurelia Ayala Usma 💁🏻‍♀️ @ Factored.ai")
st.markdown(
    "*Este es un ChatBot bilingüe que puede responder tus dudas en Español e Inglés (🇨🇴/🇺🇸) al respecto de los procesos y funciones llevados a cabo por el Instituto Colombiano de Bienestar Familiar (ICBF)  //  This is a bilingual ChatBot in English and Spanish (🇨🇴/🇺🇸) that answers your questions about processes and functions of the Colombian Institute of Family Welfare (ICBF)*"
)
st.divider()

# Initialize chat history to be displayed
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input(
    "Por favor escriba su pregunta / Please write your question"
):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(f"__{prompt}__")

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = chatbot_methods.overall_method(prompt)
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )
