
# https://blogattach.naver.com/d045cc7f6d3734e8c4254b7b4eaed0ae0a5aa0418e/20230310_126_blogfile/offbeat1020_1678410920771_44n7GW_txt/test.txt

from urllib.request import urlopen
import sys # python script실행 시 인자를 받기 위함

def fetch_words(url):
    """
    url주소에서 파일을 가져와 단어 리스트를 반환합니다.
    :param url: 불어올 url
    :return:
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words

def print_items(items):
    """
    items를 print
    :param items:
    :return:
    """
    for item in items:
        print(item)

def main(url):
    """
    url을 받아 단어를 print함
    :param url: url
    :return:
    """
    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    print(sys.argv)
    main(sys.argv[1])