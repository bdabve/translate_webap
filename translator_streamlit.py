#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# author        : el3arbi bdabve@gmail.com
# created       : 21-June-2023
#
# description   : this is the same translator but with sreamlit
# ----------------------------------------------------------------------------

import os
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())
api_key = os.getenv('OPENAI_API_KEY')

from langchain.llms import OpenAI
from langchain import PromptTemplate      # , ConversationChain
# import matplotlib.pyplot as plt

import streamlit as st
import templates

llm = OpenAI()


def ai_response(llm, input_text, prompt_formated):
    # this function to get ai response for translation and email pages
    if input_text:
        response = llm(prompt_formated)
        return response


# ===# Streamlit configuration # === #
st.set_page_config(page_title='AI Streamlit', page_icon=':robot', layout='wide')

# ------ Navigation bar ------- #
from streamlit_option_menu import option_menu
selection = option_menu(
    menu_title=None,                                # the menu title
    options=['Translator', 'Email', 'Summarizing text.', 'About'],       # options
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

selections = {
    # this to select pages variable
    'Translator': 'Translation',
    'Email': 'Email Generator',
    'Summarizing text.': 'Summarizing text and translte to Arabic',
    'About': 'About',
}

st.title(selections[selection])         # set the title for selections


#
def translator():
    st.subheader('Translate any text to Arabic, English, Frensh')
    st.markdown('''
This is a simple translation app built with Streamlit, which allows you to translate text to Arabic, English, or French. The app leverages the power of OpenAI's language model to provide accurate translations and can automatically detect the source language.

Features
- Translate text to Arabic, English, or French.
- Automatic language detection for the source text.
- Easy-to-use interface with select box and button.
- Dynamic translation output displayed instantly.
- Handles grammar correction, typos, and factual errors.
            ''')

    st.markdown('### Enter information')

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
        translation_prompt = prompt.format(translate_to=option_translate_to, text=input_text)
        translation = ai_response(llm, input_text, translation_prompt)
        if translation:
            st.markdown(translation)


def email_generator():
    with st.container():
        st.markdown("Often professionals would like to improve their emails, but don't have the skills to do so. \n\n This tool \
                will help you improve your email skills by converting your emails into a more professional format. This tool \
                is powered by [LangChain](https://langchain.com/) and [OpenAI](https://openai.com) and made by \
                [@Elaarbi](https://twitter.com).")
        col1, col2 = st.columns(2)
        with col1:
            option_tone = st.selectbox('Which tone would you like your email to have?', ('Formal', 'Informal'))
        with col2:
            option_dialect = st.selectbox('Which Dialect would you like?', ('American', 'British', 'Frensh', 'Arabic'))

        input_text = st.text_area(label="Email Input", label_visibility='collapsed', placeholder="Your Email...")
        button = st.button('Generate', type='secondary', help='Click to translate')

        prompt = PromptTemplate(input_variables=["tone", "dialect", "email"], template=templates.email_template)
        if button:
            prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=input_text)
            formatted_email = ai_response(llm, input_text, prompt_with_email)
            st.write(formatted_email)


def sum_trans_text():
    with st.container():
        input_text = st.text_area(label="Text to summ", label_visibility='collapsed', placeholder="Text...")
        button = st.button('Generate', type='secondary', help='Click to translate')
        prompt = PromptTemplate(input_variables=["text"], template=templates.summ_text)
        if button:
            prompt_with_text = prompt.format(text=input_text)
            text_summ_translated = ai_response(llm, input_text, prompt_with_text)
            st.markdown(text_summ_translated)


def about():
    with st.container():
        # st.subheader('Hi, my name is Ibrahim')
        st.subheader('السلام عليكم')
        st.title('Programming with python')


if selection == 'Translator':
    translator()
elif selection == 'Email':
    email_generator()
elif selection == 'Summarizing text.':
    sum_trans_text()
elif selection == 'About':
    about()
