def base10_to_n(number_10, to_base):
    abc_inv = {
        10: 'a',
        11: 'b', 12: 'c',
        13: 'd', 14: 'e', 15: 'f',
        16: 'g', 17: 'h', 18: 'i', 19: 'j',
        20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o',
        25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u',
        31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'
    }
    errors_ = ["ERROR:The base you want your number converted to should be more than 1",
               "ERROR:THE base you want your number converted can't be more than 36(you can add more support by increasing the symbols/letters in the 'abc_inv' dictionary)"
    ]
    if to_base < 2:
        return(errors_[0])
    if to_base > (len(abc_inv)+10):
        return(errors_[1])
    carry = number_10
    list_num_val = []
    while carry != 0:
        remainder = carry % to_base
        carry = (carry - remainder) / to_base
        list_num_val.append(int(remainder))
    list_num_val_inv = []
    for ele_num_ in range(len(list_num_val)):
        list_num_val_inv.append(list_num_val[-(ele_num_+1)])

    list_num_f = []
    for ele_num_2 in range(len(list_num_val_inv)):
        if list_num_val_inv[ele_num_2] > 9:
            list_num_f.append(abc_inv[list_num_val_inv[ele_num_2]])
        else:
            list_num_f.append(list_num_val_inv[ele_num_2])
    str_num_ = ""
    for ele_num_3 in list_num_f:
        str_num_ = str_num_ + str(ele_num_3)
    return(str_num_)















