
# https://blogattach.naver.com/d045cc7f6d3734e8c4254b7b4eacd1a30c58a7468e/20230310_126_blogfile/offbeat1020_1678410920771_44n7GW_txt/test.txt
from urllib.request import urlopen
import sys # python script실행 시 인자를 받기 위함

def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_items(items):
    for item in items:
        print(item)

def main(url):
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    main(sys.argv[1])