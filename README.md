# FLAMES Game

FLAMES is a popular game among teenagers to find out the relationship status between two people. FLAMES stands for Friends, Lovers, Affection, Marriage, Enemies, Siblings.

## How to Play

1. Run the `flames_game.py` script.
2. Enter the names of two individuals when prompted.
3. The script will calculate the FLAMES result based on the names entered.
4. It will then display the result indicating the relationship status between the two individuals.

## Game Logic

1. The script takes two names as input and converts them to lowercase for consistency.
2. It then compares the characters in both names to find the unique characters.
3. After eliminating the common characters between the two names, it randomly selects a character from the remaining characters.
4. Based on the selected character, it determines the FLAMES category.
5. The script returns the FLAMES result along with the names of the individuals entered.

## Example
- Enter the 1st Name : John
- Enter the 2nd Name : Jane
- FLAMES for john and jane is: Marriage
