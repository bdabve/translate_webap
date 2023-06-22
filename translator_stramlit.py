#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# author        : el3arbi bdabve@gmail.com
# created       : 21-June-2023
#
# description   : this is the same translator but with sreamlit
# ----------------------------------------------------------------------------

import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())
import os
api_key = os.getenv('OPENAI_API_KEY')

from langchain.llms import OpenAI
from langchain import PromptTemplate
import streamlit as st
import templates

llm = OpenAI()


# Translation function
def translate_text(input_text, prompt):
    if input_text:
        prompt_formated = prompt.format(translate_to=option_translate_to, text=input_text)
        translation = llm(prompt_formated)
        return translation


def email_(input_text, prompt):
    if input_text:
        prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=input_text)
        formatted_email = llm(prompt_with_email)
        return formatted_email


# Streamlit configuration
st.set_page_config(page_title='AI Streamlit', page_icon=':robot:')

# ------ Navigation bar ------- #
from streamlit_option_menu import option_menu
selection = option_menu(
    menu_title=None,                                # the menu title
    options=['Translator', 'Email', 'Contacts'],       # options
    icons=['house', 'book', 'envelope'],            # bootstrap icons
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',
    styles={
        'container': {'padding': '5px'},
        'icon': {'color': 'orange', 'font-size': '25px'},
        'nav-link': {'font-family': 'Monaco', 'font-size': '18px;', 'text-align': 'left', '--hover-color': '#eee'},
        'nav-link-selected': {'background-color': '#259658'}
    }
)

selections = {'Translator': 'AI Translator', 'Email': 'Globalize Email', 'Contacts': 'Contacts Page'}
st.title(selections[selection])         # set the title for selections

#
if selection == 'Translator':
    st.subheader('Translate any text to Arabic, English, Frensh')
    st.markdown('This Streamlit app allows users to translate text into English, Arabic, Frensh from any language source using the OpenAI language model.')
    st.markdown('### Enter Text to Translate')

    # Create a layout with two columns to add selectbox and button
    col1, _, col2 = st.columns([2, 2, 1])
    # Language selection
    option_translate_to = col1.selectbox('Language to translate to:', ('Arabic', 'English', 'French'))
    # Translate button
    button = col2.button('Translate', type='secondary', help='Click to translate')

    # Text input
    input_text = st.text_area(label='Enter your text here', label_visibility='collapsed', placeholder='Your text...')
    # setup the prompt
    prompt = PromptTemplate(template=templates.translate_template, input_variables=['translate_to', 'text'])
    # Translation output
    if button:
        st.markdown('### Translation')
        translation = translate_text(input_text, prompt)
        if translation:
            st.markdown(translation)

elif selection == 'Contacts':
    # ------ Header Section ------- #
    with st.container():
        st.subheader('Hi, my name is dabve :wave:')
        st.title('Programming with python')
        st.write('I love programming with Python in Ubuntu')
        st.write('[Github](https://github.com/bdabve)')
        st.write('[Youtube](https://www.youtube.com/channel/UCAXFZVODN0hCgx3yhrsZZuA)')

elif selection == 'Email':
    with st.container():
        st.markdown("Often professionals would like to improve their emails, but don't have the skills to do so. \n\n This tool \
                will help you improve your email skills by converting your emails into a more professional format. This tool \
                is powered by [LangChain](https://langchain.com/) and [OpenAI](https://openai.com) and made by \
                [@Elaarbi](https://twitter.com).")
        col1, col2 = st.columns(2)
        with col1:
            option_tone = st.selectbox('Which tone would you like your email to have?', ('Formal', 'Informal'))
        with col2:
            option_dialect = st.selectbox('Which English Dialect would you like?', ('American', 'British'))

        input_text = st.text_area(
            label="Email Input",
            label_visibility='collapsed',
            placeholder="Your Email...",
            key="email_input")

        button = st.button('Generate', type='secondary', help='Click to translate')
        if button:
            # st.session_state.email_input = "Sally I am starts work at yours monday from dave"
            prompt = PromptTemplate(input_variables=["tone", "dialect", "email"], template=templates.email_template)
            formatted_email = email_(input_text, prompt)
            st.write(formatted_email)
