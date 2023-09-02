#!/usr/bin/python3
""" This Module contient a function that print two new lines.
"""


def text_indentation(text):
    """ Function that print 2 new lines after ".?:" characters.

    Args:
        text: input string.

    Returns:
        No return.

    Raises:
        TypeError: If text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    txt = text[:]

    for d in ".?:":
        list_txt = txt.split(d)
        txt = ""
        for i in list_txt:
            i = i.strip(" ")
            txt = i + d if txt is "" else txt + "\n\n" + i + d

    print(txt[:-3], end="")
