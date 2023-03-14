#!/usr/bin/python3
def multiple_returns(sentence):
    ''' returns a tuple with length of a string and its first character'''
    if len(sentence) == 0:
        first = None
    else:
        first = sentence[0]

    data = []
    data.append(len(sentence))
    data.append(first)
    return tuple(data)
