def base_n_to_base_10(number, base):
    abc_ = {
        "a": 10,
        "b": 11, "c": 12,
        "d": 13, "e": 14, "f": 15,
        "g": 16, "h": 17, "i": 18, "j": 19,
        "k": 20, "l": 21, "m": 22, "n": 23, "o": 24,
        "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
        "v": 31, "w": 32, "x": 33, "y": 34, "z": 35,
    }
    errors =["ERROR:The number of base can only be 2 to 36(you can add more support by increasing the symbols/letters in the 'abc_' dictionary)",
             "ERROR:The number can't have a digit/symbol with a value greater than or equal to that of the integer of your base"
        ]
    if base <= 1 or base > (len(abc_) + 10):
        return (errors[0])
    str_num = number
    list_num = []
    for el_num1 in range(len(str_num)):
        list_num.append(str_num[el_num1])
    list_val_num_ = []
    for el_num2 in range(len(list_num)):
        if list_num[el_num2] == "0"  or list_num[el_num2] == "1" or list_num[el_num2] == "2" or list_num[el_num2] == "3" or list_num[el_num2] == "4" or list_num[el_num2] == "5" or list_num[el_num2] == "6" or list_num[el_num2] == "7" or list_num[el_num2] == "8" or list_num[el_num2] == "9":
            list_val_num_.append(list_num[el_num2])
        else:
            list_val_num_.append(str(abc_[list_num[el_num2]]))
    list_val_num_int = []
    for el_num4 in range(len(list_val_num_)):
        list_val_num_int.append(int(list_val_num_[el_num4]))
    if max(list_val_num_int) >=   base:
        return (errors[1])
    else:
        value_10 = 0
        for el_num3 in range(len(list_val_num_int)):
            value_10 = value_10 + int(list_val_num_int[-(el_num3 + 1)]) * (base ** el_num3)
    return (value_10)






















































