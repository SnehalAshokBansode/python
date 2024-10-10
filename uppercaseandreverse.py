class MyClass:

    def get_string(self):
        self.my_str = input("Enter any String: ")

    def print_string(self):
        s = self.my_str
        
        # Print the string in upper case
        print("String in Upper Case:", s.upper())
        
        # Reverse the string and convert it to lower case
        rev_str = s[::-1]  # Using slicing to reverse the string
        print("String in Reverse & Lower Case:", rev_str.lower())

# Main body
if __name__ == '__main__':
    obj = MyClass()
    obj.get_string()
    obj.print_string()
