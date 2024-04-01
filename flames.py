import random

def flames_game():
    # Prompt users to input their names
    name1 = input("Enter the 1st Name : ").lower()
    name2 = input("Enter the 2nd Name : ").lower()

    # Initialize an empty list to store unique characters from both names
    chars = []

    # Iterate through characters in name1
    for char in name1:
        # Check if the character is not in name2
        if char not in name2:
            # Add the character to the list
            chars.append(char)

    # Iterate through characters in name2
    for char in name2:
        # Check if the character is not in name1
        if char not in name1:
            # Add the character to the list
            chars.append(char)

    # Define the flames categories
    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]

    # Initialize the index for selecting a flames category
    index = 0

    # If there are characters remaining after elimination
    if len(chars) > 0:
        # Randomly select an index within the range of remaining characters
        index = random.randint(0, len(chars) - 1)

    # If there are no characters remaining or index exceeds the flames categories length
    if len(chars) == 0 or index >= len(flames):
        # Set index to 0 (default)
        index = 0

    # Return the selected flames category and the input names
    return flames[index], name1, name2

# Call the flames_game function to get the result
res, name1, name2 = flames_game()

# Print the result
print(f" FLAMES for {name1} and {name2} is: {res}")
