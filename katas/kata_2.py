def repeated_letter_hist(word):
    histogram = {}
    for letter in word:
        if letter not in "abcdefghijklmnopqrstuvwxyz":
            continue
        else:
            histogram[letter] = histogram.get(letter, 0) + 1
    maximum = max(histogram.values())
    return maximum


def LetterCount(a_str):
    split_string = a_str.split()
    max_count_repeats = 1
    word_with_most = ''

    for word in split_string:
        if repeated_letter_hist(word) > max_count_repeats:
            max_count_repeats = repeated_letter_hist(word)
            word_with_most = word

    if max_count_repeats > 1:
        return word_with_most
    return -1