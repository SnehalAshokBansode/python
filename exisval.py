# Initial dictionary
my_dict = {'Mon': 3, 'Tue': 5, 'Wed': 6, 'Thu': 9}

print("The given dictionary:", my_dict)

# Get user input for key and value
check_key = input("Enter Key to check: ")
check_value = input("Enter Value: ")

# Check if the key is in the dictionary
if check_key in my_dict:
    print(f"{check_key} is present.")
    # Update the value for the existing key
    my_dict[check_key] = check_value
else:
    print(f"{check_key} is not present.")
    # Add the new key-value pair
    my_dict[check_key] = check_value

# Print the updated dictionary
print("Updated dictionary:", my_dict)
