"טענת כניסה: הפעולה מקבלת מספר שלם וכמות בזיכרון"
"טענת יציאה: הפעולה מחזירה את הייצוג הבינארי של המספר בתור סטרינג"
def ConvertToBinary(Num, Memory):
    Finale = ""
    Index = 2 ** (Memory - 1)
    while Index != 0:
        if Num >= Index:
            Finale += "1"
            Num -= Index
        else:
            Finale += "0"
        Index //= 2
    return Finale

"שיטת המשלים לאחד"
"טענת כניסה: הפעולה מקבלת ייצוג סטרינג של המספר הבינארי"
"טענת יציאה: הפעולה מחזירה את הסטרינג לאחר שכל 0 הומר ל-1 וכל 1 הומר ל-0"
def CompleteToOne(Num):
    length = len(Num)
    string_list = list(Num)
    for i in range(length):
        if string_list[i] == "0":
            string_list[i] = "1"
        else:
            string_list[i] = "0"
    Num = "".join(string_list)
    return Num

"שיטת המשלים לשתיים"
"טענת כניסה: הפעולה מקבלת מספר סטרינג וכמות בזיכרון"
"טענת יציאה: הפעולה מבצעת על המספר סטרינג את שיטת המשלים ל-2"
"ובכך ממירה אותו לייצוג השלילי של המספר המקורי"
def CompleteToTwo(Num, Memory):
    keep_the_one = False
    final_index = 0 - Memory
    starter = -2
    string_list = list(Num)
    if string_list[-1] == "1":
        string_list[-1] = "0"
        keep_the_one = True
    else:
        string_list[-1] = "1"
    while starter >= final_index:
        if string_list[starter] == "0":
            if keep_the_one:
                string_list[starter] = "1"
                keep_the_one = False
        else:
            if keep_the_one:
                string_list[starter] = "0"
        starter += -1
    Num = "".join(string_list)
    return Num

def Main():
    Memory = int(input("enter the space of the memory" ))
    Number = int(input("enter the nunber you want to convert to negative binary"))
    binary = ConvertToBinary(Number, Memory)
    fixed_binary = CompleteToOne(binary)
    negative_binary = CompleteToTwo(fixed_binary, Memory)
    print(negative_binary)

if __name__ == "__main__":
    Main()