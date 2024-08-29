import random, sys

input = lambda: sys.stdin.readline().strip()
sys.stdin = open("./class.txt", "r", encoding="utf-8")


def config_class_dict() -> dict:
    class_dict = {}
    for _ in range(7):
        group_info = input()
        student = group_info[5:].split(", ")
        class_dict[int(group_info[0])] = student * (6 // len(student))
    return class_dict


if __name__ == "__main__":
    class_dict = config_class_dict()
    order = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(order)
    for i in order:
        random.shuffle(class_dict[i])
    publisher = [class_dict[n][0] for n in order]
    print(publisher)
    # print(class_dict)
