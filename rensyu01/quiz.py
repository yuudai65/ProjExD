import random 

def shutudai():

    qa = random.choice(qa_list)
    print("問題：",qa["q"])
    return qa["a"]
    
if __name__ == "__main__":
    qa_list = {"q":"サザエさんの旦那の名前は？", "a":["ますお","マスオ"]},
    {"q":"カツオの妹の名前は？","a":["わかめ","ワカメ"]},
    {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"]}
    shutudai()
    #kaito()
    
def kaito(a_lst):
    kai = input("答えを入力してください：")
    print("入力した答えは：",kai)
    if kai in a_lst:
        print("正解です")
    else:
        print("不正解")