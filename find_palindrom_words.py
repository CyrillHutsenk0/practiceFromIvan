con = str(input("Enter a sentence: "))

while len(con) <= 0:
    con = str(input("Enter a sentence: "))


def palindrom(sentence):
    structure = sentence.lower().split()
    rezalt = []
    newlist = []
    dublicate = []
    for elem in structure:
        elem_list = list(elem)
        copy_el_ls = elem_list.copy()
        copy_el_ls.reverse()
        if elem_list == copy_el_ls:
            str_elem = elem_list
            convert_el_ls = ''.join(map(str, str_elem))
            rezalt.append(convert_el_ls)
    if bool(rezalt) is False:
        return print("We dont't found polidrom")
    for i in rezalt:
        if i not in newlist:
            newlist.append(i)
        else:
            dublicate.append(i)
    return print(f"We found polindrom: {newlist}")


palindrom(con)
