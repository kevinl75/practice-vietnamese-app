import json
import random

import streamlit as st

from options import LanguageOptions
from questions import TranslationQuestion


def load_data() -> dict:

    data = {}
    with open("data/vd_en_words_translations.json") as fd:
        data = json.load(fd)

    return data


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
        st.session_state["bad_answer"] = (
            f':red[Incorrect, the good answer was "*{translation_question.word_options[0]}*"]'
        )


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


st.title("Hello Learners :wave:!")
st.header(
    "Let's make a small game. I give you a word, and you try to give me the english or vietnamese translation. Let's go."
)

change_lang = st.radio(
    "English to Vietnamese or Vietnames to English?",
    [LanguageOptions.VN_TO_EN.value, LanguageOptions.EN_TO_VN.value],
)

translation_question = TranslationQuestion(
    words_dict=st.session_state["words_dict"], vn_to_en=change_lang
)
word_options_shuffled = translation_question.shuffle_word_options()

st.subheader(
    f'What is the english translation of the word "**{translation_question.word_to_guess}**"?'
)

columns = st.columns(4)
for i in range(len(columns)):
    word = word_options_shuffled[i]
    columns[i].button(
        label=f"**{word}**",
        key=word,
        on_click=check_result,
        args=[word],
        use_container_width=True,
    )

st.write(
    st.session_state["good_answer"]
    if st.session_state["good_answer"]
    else st.session_state["bad_answer"]
)

st.write(f"Your current score is: **{st.session_state['score']}**")
st.divider()
st.write(f"Your best score is: **{st.session_state['best_score']}**")
