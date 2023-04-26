from collections import defaultdict


def default_dic_test():
    default_dic_a: defaultdict = defaultdict(int)

    default_dic_a["A"] += 1
    default_dic_a["B"] = 1

    print(default_dic_a)
    print(default_dic_a["C"])


def normal_dic_test():
    normal_dic_a = {"A": 1, "B": 1}

    # KeyError: 'C'
    # normal_dic_a['C'] += 1

    # KeyError: 'D
    # print(normal_dic_a['D'])

    print(normal_dic_a)


print("\nDefault dict test")
default_dic_test()

print("\nDict test")
normal_dic_test()
