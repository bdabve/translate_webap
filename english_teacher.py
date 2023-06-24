#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import dotenv
import os
import streamlit as st
import openai

dotenv.load_dotenv(dotenv.find_dotenv())

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    """
    Calls the OpenAI API to generate a completion based on the given messages.

    Args:
        messages (list): List of message objects.
        model (str): The model to use for completion (default: "gpt-3.5-turbo").
        temperature (float): The degree of randomness in the model's output (default: 0).

    Returns:
        str: The generated completion response.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


def display_messages(chat_container):
    # Display chat history in reverse order (last message first)
    context = st.session_state.context
    for message in context:
        role = message['role']
        content = message['content']
        if role == 'system':
            pass
        else:
            chat_container.markdown(f"**{role.capitalize()}:** {content}")
        chat_container.divider()   # Add a horizontal rule to separate chat history from current input


def app():
    # Check if context is already stored in session state, if not initialize it
    if "context" not in st.session_state:
        st.session_state.context = []
        system = '''
        As a spoken English teacher and improver, \
        I would like to engage in English conversations with you. \
        Please reply in English to help me practice my spoken English skills. \
        Your responses should be clear and concise, limited to 100 words. \
        It's important that you strictly correct any grammar mistakes, typos, and factual errors in my messages. \
        Additionally, please include a question in your reply to encourage further conversation. Let's begin our practice session.         You can start by asking me a question. \
        Remember, I value accurate corrections and guidance to enhance my English language skills.
        '''
        # system = '''
        # User: Please help me improve my English language skills. \
        # I want to correct any grammar mistakes and spelling errors in my writing. \
        # I would appreciate your assistance in making my English more fluent and natural. \
        # Kindly provide suggestions for improvement and examples to illustrate the corrections. Thank you for your help!
        # Let's begin our practice session. Could you start by asking me a question?
        # '''
        st.session_state.context.append({'role': 'system', 'content': system})

    st.title("English Teacher Chatbot")
    context = st.session_state.context

    if len(context) > 0:
        # send the first message as system
        ai_response = get_completion_from_messages(context)
        st.session_state.context.append({'role': 'assistant', 'content': ai_response})

    chat_container = st.container()

    # Get user input and generate AI response
    user_input = st.text_input(label="You: ", placeholder='Enter you text here', key='user_input')
    if user_input:
        st.session_state.context.append({'role': 'user', 'content': user_input})
        ai_response = get_completion_from_messages(context)
        st.session_state.context.append({'role': 'assistant', 'content': ai_response})
        user_input = ''

    display_messages(chat_container)
    for item in context:
        print(item)
        print('-' * 30)


if __name__ == "__main__":
    app()
