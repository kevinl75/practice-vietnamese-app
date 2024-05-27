# Vietnamese to English Translation Quiz

This is a simple quiz application built with Streamlit that helps you practice translating Vietnamese words to English. The app presents a Vietnamese word and provides four possible English translations. Your task is to select the correct translation.

## Features

- Displays a Vietnamese word and four possible English translations.
- Tracks the current score and the best score.
- Randomizes the order of the English translations.
- Provides immediate feedback on whether the selected translation is correct or not.

## Installation

To run this application, you need to have Python installed. It is recommended to use a virtual environment.

```bash
git clone https://github.com/kevinl75/practice-vietnamese-app.git
cd your-repo-directory
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

You can start the application simply by running:
```bash
streamlit run src/app.py
```

Open your web browser and go to `http://localhost:8501` to interact with the application.

## Code Overview

### Load Data

The function `load_data` loads the Vietnamese-English translation dataset from a JSON file.

### Select Quiz Words

The function `select_quizz_words` randomly selects a Vietnamese word and four English translations, ensuring that one of them is the correct translation.

### App Layout and Content

The Streamlit app layout is created using:
- `st.title` and `st.subheader` for headings.
- `st.write` to display the Vietnamese word.
- `st.button` to create buttons for the English translation options.

### Score Management

The score and best score are managed using `st.session_state`. The `check_result` function updates the score based on the user's selection.
