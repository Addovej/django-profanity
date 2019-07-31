import re

__all__ = ['translate']


def translate(text, trans):
    """
    This function designed for replace a matched character sequence by trans dictionary.

    """

    return re.sub(
        f'({"|".join(map(re.escape, trans.keys()))})',
        lambda m: trans[m.group()],
        text
    )
