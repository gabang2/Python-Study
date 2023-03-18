sentence = "안녕하세요. 저는 김가영이고 24살입니다. 반갑습니다!"
sentence_split = sentence.split()
sentence_split = [len(word) for word in sentence_split if len(word) > 3]
print(sentence_split)