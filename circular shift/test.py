

from circularShift import CircularShift


def main():

    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a versatile and powerful programming language.",
        "OpenAI's GPT-3 is an impressive language model.",
        "I love to code and solve interesting problems.",
        "This sentence is just a test for circular shifting."
    ]

    
    c = CircularShift(sentences)
    
    for line in c.get_shifted_lines():
        print(line)


if __name__ == '__main__':
    main()
    