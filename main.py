def main():
    with open("books/frankenstein.txt") as f: # Opening the file for reading
        file_contents = f.read() # Reading the contents of the file into a string
    
    lower_contents = file_contents.lower() # Converting all the characters in the file_contents string into lowercase and storing them
 

    char_count = char_dict(lower_contents) # Creating a dictionary with charaters and their counts

    char_list = [] # Making a dictionary into a sorted list of dictionaries
    for k, v in char_count.items(): 
        if k.isalpha(): # Checking if the character is an alphabetical character
            sorted_dict = {"character": k, "count": v} # Making a dictionary for each character and it's count
            char_list.append(sorted_dict) # Appending a dictionary to the char_list

    char_list.sort(reverse=True, key=sort) # Sorting the list by count in descending order

    for item in char_list: 
        print(f"The {item['character']} was found {item['count']} times")
    

def char_dict(text):
    frank_dict = {}
    for c in text:
        if c in frank_dict:
            frank_dict[c] += 1
        else:
            frank_dict[c] = 1
    return frank_dict # The dictionary, containing each unique character as a key and it's count as a value

def sort(frank_dict):
    return frank_dict["count"]

# Original unsorted dictionary of all character counts, including special characters
unsorted_dict = {'p': 6121, 'r': 20818, 'o': 25225, 'j': 504, 'e': 46043, 'c': 9243, 't': 30365, ' ': 74144, 'g': 5974, 'u': 10407, 'n': 24367, 'b': 5026, "'": 229, 's': 21155, 'f': 8731, 'a': 26743, 'k': 1755, 'i': 24613, ',': 5097, 'y': 7914, 'm': 10604, 'w': 7638, 'l': 12739, '(': 39, 'd': 16863, ')': 39, 'h': 19725, '\n': 7651, 'v': 3833, '.': 3124, '-': 445, ':': 68, '1': 92, '7': 23, '2': 24, '0': 21, '8': 20, '[': 4, '#': 1, '4': 17, ']': 4, '*': 28, 'z': 243, '?': 220, ';': 970, 'x': 677, 'q': 324, '!': 239, '"': 796, '3': 18, '5': 16, '9': 13, '6': 10, '_': 2, '/': 24, '%': 1, '@': 2, '$': 2}

if __name__ == "__main__": # Checking if the script is being run as the main program and calling the main function
    main()