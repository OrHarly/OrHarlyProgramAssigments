def xor_on_string(bit):
    int_bit = int(bit)
    xor_bit = int_bit^1
    xord_str_bit = str(xor_bit)
    return xord_str_bit

def convertlisttostring(list):
    final_s = ""
    for i in range(len(list)):
        final_s += str(list[i])
    return final_s

def main():
    x = int(input("enter either 5 or 6 "))
    bin_x = bin(x)[2:]
    list_bin_x = list(bin_x)
    list_bin_x[1] = xor_on_string(list_bin_x[1])
    list_bin_x[2] = xor_on_string(list_bin_x[2])
    str_bin_x = convertlisttostring(list_bin_x)
    finale = int(str_bin_x, 2)
    print(finale)

if __name__ == "__main__":
    main()