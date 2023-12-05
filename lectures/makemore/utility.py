import random


# Function to generate a syllable


def generate_syllable(structure, consonants, vowels):
    syllable = ''
    for char in structure:
        if char == 'C':
            syllable += random.choice(consonants)
        elif char == 'V':
            syllable += random.choice(vowels)
    return syllable
