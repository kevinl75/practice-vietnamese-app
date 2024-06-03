from dataclasses import dataclass


@dataclass
class TranslationQuestion:

    word_to_guess: str
    word_options: list[str]
