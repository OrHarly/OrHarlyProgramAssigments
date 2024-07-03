def convert_text_file_to_binary_word_list():
    file_name = "unsafe_file.txt"
    with open(file_name, "rb") as binary_file:
        data = binary_file.read()
        text = data.decode('utf-8')  # Decode binary data to text
        words = text.split()  # Split text into words
        binary_word_list = []
        for word in words:
            binary_word = ''.join(format(ord(char), '08b') for char in word)  # Convert word to binary
            binary_word_list.append(binary_word)
    return binary_word_list

def FindVirus(byte_list):
    virus_string = "virus"
    VIRUS = ''.join(format(ord(i), '08b') for i in virus_string)
    for i in range(len(byte_list)):
        if VIRUS in byte_list[i]:
            return True
    return False


def Main():
    L = convert_text_file_to_binary_word_list()
    Contains_Virus = FindVirus(L)
    if Contains_Virus:
        print("this file contains a virus")
    else:
        print("this file is safe")

if __name__ == "__main__":
    Main()
