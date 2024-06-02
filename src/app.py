import json
import random

import streamlit as st

from questions import TranslationQuestion


def load_data() -> dict:

    data = {}
    with open("data/vd_en_words_translations.json") as fd:
        data = json.load(fd)
    
    return data


def select_question_dataset(words_dict: dict, vn_to_en: bool=True) -> dict:
    if vn_to_en:
        word_to_guess_lg = "VN"
        word_options_lg  = "EN"
    else:
        word_to_guess_lg = "EN"
        word_options_lg  = "VN"

    word_to_guess_index = random.randrange(0, len(words_dict["translations"]))
    word_to_guess = words_dict["translations"][word_to_guess_index][word_to_guess_lg]

    word_options = []
    word_options.append(words_dict["translations"][word_to_guess_index][word_options_lg])

    find_other_words = True
    while find_other_words:
        word_option_index = random.randrange(0, len(words_dict["translations"]))
        if word_option_index != word_to_guess_index:
            if words_dict["translations"][word_option_index][word_options_lg] not in word_options:
                word_options.append(words_dict["translations"][word_option_index][word_options_lg])
        if len(word_options) == 4:
            find_other_words = False

    return TranslationQuestion(word_to_guess=word_to_guess, word_options=word_options)


def check_result(choice):
    if choice == translation_question.word_options[0]:
        st.session_state["score"] += 1
        st.session_state["bad_answer"] = ""
        st.session_state["good_answer"] = f":green[That's right :wink:!]" 
    else:
        if st.session_state["score"] > st.session_state["best_score"]:
            st.session_state["best_score"] = st.session_state["score"]
        st.session_state["score"] = 0
        st.session_state["good_answer"] = ""
        st.session_state["bad_answer"] = f':red[Incorrect, the good answer was "*{translation_question.word_options[0]}*"]'


if "words_dict" not in st.session_state:
    st.session_state["words_dict"] = load_data()

if "score" not in st.session_state:
    st.session_state["score"] = 0

if "best_score" not in st.session_state:
    st.session_state["best_score"] = 0

if "good_answer" not in st.session_state:
    st.session_state["good_answer"] = ""

if "bad_answer" not in st.session_state:
    st.session_state["bad_answer"] = ""

if "vn_to_en" not in st.session_state:
    st.session_state["vn_to_en"] = False

st.session_state["vn_to_en"] = st.toggle("Vietnamese to English" if st.session_state["vn_to_en"] else "English to Vietnamese")

translation_question = select_question_dataset(words_dict=st.session_state["words_dict"], vn_to_en=st.session_state["vn_to_en"])

st.title("Hello Learners :wave:!")

st.subheader("Let's make a small game. I give you vietnamese word, and you try to give me the english translation. Let's go.")
st.write(f"What is the english translation of the word *{translation_question.word_to_guess}*?")

word_options_shuffled = translation_question.word_options.copy()
random.shuffle(word_options_shuffled)
col1, col2, col3, col4 = st.columns(4)

with col1:
    word = word_options_shuffled[0]
    st.button(label=word, key=word, on_click=check_result, args=[word], use_container_width=True)

with col2:
    word = word_options_shuffled[1]
    st.button(label=word, key=word, on_click=check_result, args=[word], use_container_width=True)

with col3:
    word = word_options_shuffled[2]
    st.button(label=word, key=word, on_click=check_result, args=[word], use_container_width=True)

with col4:
    word = word_options_shuffled[3]
    st.button(label=word, key=word, on_click=check_result, args=[word], use_container_width=True)

st.write(st.session_state["good_answer"] if st.session_state["good_answer"] else st.session_state["bad_answer"])

st.write(f"Your current score is: **{st.session_state['score']}**")
st.divider()
st.write(f"Your best score is: **{st.session_state['best_score']}**")
