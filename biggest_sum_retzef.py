def find_biggest_sum(int_list):
    sum = 0
    biggest_sum = 0
    for i in range(len(int_list)):
        j = i
        while (j < len(int_list)):
            sum += int_list[j]
            if sum>biggest_sum:
                biggest_sum = sum
            j += 1
        sum = 0
    return biggest_sum


def Main():
    int_list = [-4, -1, 9, 5, 2, 1]
    print(find_biggest_sum(int_list))

if __name__ == "__main__":
    Main()
