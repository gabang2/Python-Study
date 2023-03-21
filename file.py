def file_test1():
    try:
        f = open('test1.txt', mode = 'wt', encoding='utf-8')
        f.write('파이썬으로 파일을 작성하고 있습니다.')
        f.write('newline 문자로 개행해봅시다.\n')
        f.write('개행이 잘 되었나요?')
    finally:
        f.close()

def file_test2():
    with open('test2.txt', mode='wt', encoding='utf-8') as f:
        f.write('파이썬으로 파일을 작성하고 있습니다.')
        f.write('newline 문자로 개행해봅시다.\n')
        f.write('개행이 잘 되었나요?')

file_test1()
file_test2()