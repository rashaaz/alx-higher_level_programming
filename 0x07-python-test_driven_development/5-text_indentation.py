#!/usr/bin/python3
"""Module to perform text indentation."""


def text_indentation(text):
    """Perform text indentation based on specific delimiters.

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the provided text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
