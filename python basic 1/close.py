from contextlib import closing

class OpenClose:
    def open(self):
        print('작업을 시작합니다.')
    
    def do_something(self):
        print('작업을 하는 중입니다.')

    def close(self):
        print("작업을 종료합니다.")

def doOpenClose1():
    d = OpenClose()
    d.open()
    d.do_something()
    d.close()

def doOpenClose():
    with closing(OpenClose()) as d:
        d.open()
        d.do_something()