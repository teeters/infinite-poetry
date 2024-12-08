import random

def ablate_lines(poem, forced, lines_to_remove):
    if lines_to_remove <= 0:
        return poem
    lines = poem.split('\n')
    indices_to_ablate = random.sample(range(len(lines)), lines_to_remove)
    for i in indices_to_ablate:
        if forced in lines[i]:
            continue
        else:
            lines[i] = " "
    return "\n".join(lines)

def start_of_word(s, idx):
    '''Return True if idx is the start of a word in s'''
    if idx <= len(s) - 1:
        if (idx == 0 or s[idx-1].isspace()) and not s[idx].isspace():
            return True
    return False

def word_at_idx(s, idx):
    '''Return word at idx terminated by whitespace or end of s'''
    i = idx
    word = ""
    while i < len(s):
        if not s[i].isspace():
            word += s[i]
        else:
            break
        i += 1
    return word

def word_indices(s):
    indices = []
    for i in range(len(s)):
        if start_of_word(s, i):
            indices.append(i)
    return indices

def ablate_words(poem, forced, words_to_remove):
    indices = word_indices(poem)
    to_ablate = []
    while len(to_ablate) < words_to_remove and len(indices) > 0:
        idx = random.choice(indices)
        if not word_at_idx(poem, idx) in forced:
            to_ablate.append(idx)
            indices.remove(idx)
    for start_idx in to_ablate:
        word = word_at_idx(poem, start_idx)
        end_idx = start_idx+len(word)
        poem = poem[0:start_idx] + ' '*len(word) + poem[end_idx:]
    return poem
