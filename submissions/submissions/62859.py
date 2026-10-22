def word_frequency(text):
    # Create an empty dictionary to store each word and its frequency
    freq = {}

    # Split the input text into a list of words using whitespace
    x = text.split()

    # Loop through each word in the list
    for i in x:

        # Get the current count of the word (0 if it is not present)
        # Add 1 to the count and update the dictionary
        freq[i] = freq.get(i, 0) + 1

    # Return the dictionary containing each word and its frequency
    return freq
