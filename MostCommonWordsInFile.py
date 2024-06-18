def ConvertFileToList():
    my_file = open('file_for_mission', "r")
    data = my_file.read()
    list = data.replace("  ", " ").split(" ")
    return list

def CounterDictionary(list):
    d = {}
    count = 1
    word = ""
    for i in range(len(list)):
        if not list[i] == word:
            if not word == "":
                d[word] = count
            count = 1
            word = list[i]
        else:
            count = count + 1
    d[word] = count
    return d

def main():
    list = ConvertFileToList()
    list.sort()
    d = CounterDictionary(list)
    print(d)
    sort_dictionary = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    print(sort_dictionary)
    N = int(input("enter a number"))
    list_from_dict = [(key, value) for key, value in sort_dictionary.items()]
    if (N > len(list_from_dict)):
        print("sorry there aren't that number of words in the list")
    else:    
        for i in range(N):
            print(list_from_dict[i])

if __name__ == "__main__":
    main()

