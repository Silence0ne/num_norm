PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
ENGLISH_DIGITS = "0123456789"

DIGIT_TRANSLATION_TABLE = str.maketrans(
    PERSIAN_DIGITS,
    ENGLISH_DIGITS,
)


def convert_digits(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("value must be a string.")

    return value.translate(DIGIT_TRANSLATION_TABLE)
