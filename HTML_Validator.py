#!/bin/python3


import re


def validate_html(html):
    '''
    This function performs a limited version of html validation by
    checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    if len(html) == 0:
        return True
    alltags = _extract_tags(html)
    if not alltags:
        return False
    stack = []
    balanced = True
    index = 0

    while index < len(alltags) and balanced:
        tag = alltags[index]
        if '/' not in tag:
            stack.append(tag)
        else:
            if not stack:
                balanced = False
            else:
                top = stack.pop()
                top1 = top.replace('/', '')
                if not top1 == tag.replace('/', ''):
                    balanced = False
        index += 1
    if balanced and not stack:
        return True
    else:
        return False

    # HINT:
    # use the _extract_tags function below to generate a list of
    # html tags without any extra text;
    # then process these html tags using the balanced parentheses
    # algorithm from the class/book
    # the main difference between your code and the code from class
    # will be that you will have to keep track of not just
    # the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to
    be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    tags = re.findall(r'<[^>]+>', html)
    return tags
