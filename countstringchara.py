check_string = "MalegaonBaramatiPune"

# Initialize an empty dictionary
char_count = {}

# Count occurrences of each character
for ch in check_string:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

# Print the character counts
for key in char_count:
    print(key, "-", char_count[key])
