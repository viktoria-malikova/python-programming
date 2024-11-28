def count_smalls_4(lst):
    i = 0
    small_items = 0
    while i < len(lst):
        if lst[i] < 30:
            small_items += 1
        else:
            return small_items
        i += 1
    return small_items

def main():

    list = [10,20,25,30,50,90]
    print(count_smalls_4(list))

main()