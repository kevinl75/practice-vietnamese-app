import random
from dataclasses import dataclass

from options import LanguageOptions


@dataclass
class TranslationQuestion:

    word_to_guess: str
    word_options: list[str]

    def __init__(self, words_dict: dict, vn_to_en: str):
        if vn_to_en == LanguageOptions.VN_TO_EN.value:
            word_to_guess_lg = "VN"
            word_options_lg = "EN"
        else:
            word_to_guess_lg = "EN"
            word_options_lg = "VN"

        word_to_guess_index = random.randrange(0, len(words_dict["translations"]))
        self.word_to_guess = words_dict["translations"][word_to_guess_index][
            word_to_guess_lg
        ]

        self.word_options = []
        self.word_options.append(
            words_dict["translations"][word_to_guess_index][word_options_lg]
        )

        find_other_words = True
        while find_other_words:
            word_option_index = random.randrange(0, len(words_dict["translations"]))
            if word_option_index != word_to_guess_index:
                if (
                    words_dict["translations"][word_option_index][word_options_lg]
                    not in self.word_options
                ):
                    self.word_options.append(
                        words_dict["translations"][word_option_index][word_options_lg]
                    )
            if len(self.word_options) == 4:
                find_other_words = False

    def shuffle_word_options(self) -> list[str]:
        copy_word_options = self.word_options.copy()
        random.shuffle(copy_word_options)
        return copy_word_options
