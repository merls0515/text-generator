import random

sample_texts = [
    "The future of AI is incredibly exciting and full of possibilities.",
    "Technology is evolving faster than ever before.",
    "Python is one of the most powerful programming languages.",
    "Streamlit makes it easy to build web apps with Python.",
    "Creativity and coding together can build amazing things."
]

def generate_text(prompt, length=50):
    words = prompt.split()

    for _ in range(length):
        words.append(random.choice(sample_texts).split()[0])

    return " ".join(words)
