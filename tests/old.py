from alphabeticShift import AlphabeticShift

if __name__ == "__main__":
    lines = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a versatile and powerful programming language.",
        "OpenAI's GPT-3 is an impressive language model.",
        "I love to code and solve interesting problems.",
        "This sentence is just a test for circular shifting."
    ]

    circular_shifter = CircularShift(lines)
    alphabetic_shifter = AlphabeticShift(circular_shifter)

    alphabetic_shifter.alpha_sort()

    sorted_lines = alphabetic_shifter.get_sorted_lines()

    print("Alphabetically Sorted Lines:")
    for line in sorted_lines:
        print(line)
      
