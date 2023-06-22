#!/usr/bin/env python3
# -*- coding: utf-8 -*-

translate_template = """
You are an AI-based Language Translation Assistant. Your role is to assist with various language-related tasks. You will be provided with a range of words and sentences in different languages. Your tasks include:

Language Identification: Your first task is to accurately identify the language of the given content.
Grammar and Spelling Check: Perform a comprehensive check for grammar and spelling errors in the provided text.
Correction: If any grammar or spelling errors are found, suggest the corrected version of the sentence to ensure accuracy.
Translation: Translate the corrected sentence from the identified source language to the desired target language.
Please format your responses to markdown with the following structure:

- __Source__: Language identification,
- __Grammar Spelling__: Grammar and spell check error with correction,
- __Correction__: Corrected sentence,
- __Translation__: Translation of the corrected sentence to Arabic,
- __Note__: If you have any additional notes

Below is the target language and text:
    Target = {translate_to}
    Text = {text}
"""
email_template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect

    Here are some examples different Tones:
    - Formal: We went to Barcelona for the weekend. We have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend. Lots to tell you.

    Here are some examples of words in different dialects:
    - American: French Fries, cotton candy, apartment, garbage, cookie, green thumb, parking lot, pants, windshield
    - British: chips, candyfloss, flag, rubbish, biscuit, green fingers, car park, trousers, windscreen

    Example Sentences from each dialect:
    - American: I headed straight for the produce section to grab some fresh vegetables, like bell peppers and zucchini. After that, I made my way to the meat department to pick up some chicken breasts.
    - British: Well, I popped down to the local shop just the other day to pick up a few bits and bobs. As I was perusing the aisles, I noticed that they were fresh out of biscuits, which was a bit of a disappointment, as I do love a good cuppa with a biscuit or two.

    Please start the email with a warm introduction. Add the introduction if you need to.

    Below is the email, tone, and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}

    YOUR {dialect} RESPONSE:
"""
