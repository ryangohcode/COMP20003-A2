import textdistance as td

'''Find the most similar word in a list of words to a given word.
Returns a tuple of (most similar word, similarity score based on Hamming similarity'''
def find_most_similar(target_word, data):
    most_similar = (data[0], 0)
    for other_word in data:
        ham_sim = td.hamming.similarity(target_word, other_word)
        if(ham_sim > most_similar[1]):
            most_similar = (other_word, ham_sim)
    return most_similar