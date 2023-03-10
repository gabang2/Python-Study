from urllib.request import urlopen

with urlopen("https://blogattach.naver.com/d045cc7f6d3734e8c4254b764eabd4a80f59a1438b/20230310_126_blogfile/offbeat1020_1678410920771_44n7GW_txt/test.txt") as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

for word in story_words:
    print(word)