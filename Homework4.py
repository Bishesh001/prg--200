# ======================================================
# Question 4 - Word Frequency Counter
# ======================================================

def word_frequency(text):
    # Remove punctuation
    punctuation = ".,!?;:\"'()"
    translator = str.maketrans("", "", punctuation)

    # Convert to lowercase, remove punctuation, and split into words
    words = text.lower().translate(translator).split()

    # Count word frequencies
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Sort by frequency (highest first)
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

    return sorted_words[:3]


# ==========================
# Main Program
# ==========================

print("QUESTION 4 - WORD FREQUENCY COUNTER")

user_text = input("Enter a paragraph: ")

if user_text.strip():
    top_words = word_frequency(user_text)

    print("\nTop 3 Most Frequent Words:")
    for word, count in top_words:
        print(f"{word} - {count} times")
else:
    print("No text entered.")