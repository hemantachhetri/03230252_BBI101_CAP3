def read_text(txt_file): #reading a text file
    total_sum = 0
    
    with open(txt_file, 'r') as file:
        for line in file:
            line = line.strip()
            # Extract first and last digits  
            first_digit = None
            last_digit = None

            for char in line:
                if char.isdigit():
                    if first_digit is None:
                        first_digit = int(char)
                    else:
                        last_digit = int(char)
                        break

            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break

            if first_digit is not None and last_digit is not None:
            #If first and last digit are found then add them to the total sum.
                two_digit_number = int(str(first_digit) + str(last_digit))
                total_sum += two_digit_number

    return total_sum
# Function to get the real solution
txt_file = '252.txt'
# the last three digits of my student number
# Generate the file based on the last three digits, file = f"{last_three_digits}.txt"
answer = read_text(txt_file)

print(f"The solution for my input file is {answer}")

# REFERENCES
# Lemaster, P. (2021, december 30).Retrieved from how to read from the text.txt file in python.[Video].Youtub video.https://youtu.be/DCaKj3eIrro?si=qKRB-oW8UYlVEbyy
# Aurange, A. (2022, december 8). File Handling in Python.[Video].Yputub video.https://youtube.com/playlist?list=PLVJiPhsW8Gnf5rQCOXoptugEtJneB0ZOd&si=DqUGUWhZo9ZvxzNT


