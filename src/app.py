import json
import random

import streamlit as st

def load_data() -> dict:

    data = {}
    with open("data/vd_en_words_translations.json") as fd:
        data = json.load(fd)
    
    return data


def select_quizz_words(words_dict: dict) -> dict:
    selected_words = {
        "VN": [],
        "EN": []
    }
    selected_word_index = random.randrange(0, len(words_dict["translations"]))

    selected_words["VN"].append(words_dict["translations"][selected_word_index]["VN"])
    selected_words["EN"].append(words_dict["translations"][selected_word_index]["EN"])

    find_other_words = True
    while find_other_words:
        selected_en_word_index = random.randrange(0, len(words_dict["translations"]))
        if selected_en_word_index != selected_word_index:
            if words_dict["translations"][selected_en_word_index]["EN"] not in selected_words["EN"]:
                selected_words["EN"].append(words_dict["translations"][selected_en_word_index]["EN"])
        if len(selected_words["EN"]) == 4:
            find_other_words = False

    return selected_words

def check_result(choice):
    if choice == selected_words_dict["EN"][0]:
        st.session_state["score"] += 1
    else:
        if st.session_state["score"] > st.session_state["best_score"]:
            st.session_state["best_score"] = st.session_state["score"]
        st.session_state["score"] = 0
        

if "score" not in st.session_state:
    st.session_state["score"] = 0

if "words_dict" not in st.session_state:
    st.session_state["words_dict"] = load_data()

if "best_score" not in st.session_state:
    st.session_state["best_score"] = 0

# vn_to_en = True        
selected_words_dict = select_quizz_words(words_dict=st.session_state["words_dict"])

st.title("Hello Learners :wave:!")
st.subheader("Let's make a small game. I give you vietnamese word, and you try to give me the english translation. Let's go.")
st.write(f"What is the english translation of the word *{selected_words_dict['VN'][0]}*?")

selected_en_words_dict_shuffled = selected_words_dict["EN"].copy()
random.shuffle(selected_en_words_dict_shuffled)
col1, col2, col3, col4 = st.columns(4)

with col1:
    word = selected_en_words_dict_shuffled[0]
    st.button(label=word, key=word, on_click=check_result, args=[word], use_container_width=True)

with col2:
    word = selected_en_words_dict_shuffled[1]
    st.button(label=word, key=word, on_click=check_result, args=[word], use_container_width=True)

with col3:
    word = selected_en_words_dict_shuffled[2]
    st.button(label=word, key=word, on_click=check_result, args=[word], use_container_width=True)

with col4:
    word = selected_en_words_dict_shuffled[3]
    st.button(label=word, key=word, on_click=check_result, args=[word], use_container_width=True)

st.subheader(body=f"Your current score is: {st.session_state['score']}")
st.subheader(body=f"Your best score is: {st.session_state['best_score']}")
