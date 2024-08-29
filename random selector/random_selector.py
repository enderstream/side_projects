import random

if __name__ == "__main__":
    class_dict = {
        1: ["정효원", "권동환"],
        2: ["전혜준", "김경환", "정유진"],
        3: ["김범주", "이동언", "최현정"],
        4: ["임종관", "이지은", "오한나"],
        5: ["김선명", "김진실", "김윤하"],
        6: ["이길호", "김재혁", "김근휘"],
        7: ["김순도", "장인영", "이재욱"],
    }
    order = [1, 2, 3, 4, 5, 6, 7]
    random.shuffle(order)
    for i in order:
        random.shuffle(class_dict[i])
        
    publisher = [[o, class_dict[o][0]] for o in order]
    for p in publisher:
        print(f"{p[0]}조: {p[1]}")
