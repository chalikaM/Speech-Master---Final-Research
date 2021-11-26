import string
from collections import Counter


def textAnalyze(speech):
    text = speech

    # converting to lowercase
    lower_case = text.lower()

    # Removing punctuations of the full text
    cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

    # splitting text into words
    tokenized_words = cleaned_text.split()

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                  "these",
                  "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
                  "do",
                  "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
                  "again",
                  "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
                  "each",
                  "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                  "than",
                  "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    # Removing stop words from the tokenized words list
    final_words = []
    for word in tokenized_words:
        if word not in stop_words:
            final_words.append(word)

    emotion_list = []

    for i in final_words:
        with open('Emotion/emotions.txt', 'r') as file:
            for line in file:
                clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                word, emotion = clear_line.split(':')
                if i in word:
                    final_emotions = emotion.replace("", '').strip()
                    emotion_list.append(final_emotions)

    print(emotion_list)
    w = emotion_list
    print(w)
    return {
        "message": w
    }
