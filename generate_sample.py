import random
from faker import Faker

fake = Faker()

# Generate 12 more sample input files
for i in range(1, 13):
    # Create a filename based on the index
    filename = f"{i}.txt"

    # Randomly generate a URL
    url = f"www.example{i}.com"

    # Randomly generate between 3 to 10 sentences
    num_sentences = random.randint(3, 10)
    sentences = "$".join([fake.sentence() for _ in range(num_sentences)])

    # Combine URL and sentences
    file_content = f"{url}\n{sentences}$"

    # Write content to the file
    with open(filename, "w") as file:
        file.write(file_content)

    print(f"Generated {filename}")
