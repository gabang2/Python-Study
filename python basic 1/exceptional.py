import sys
from math import log

def convert(s):
    """int로 변환"""
    try:
        print("일단 실행해보기")
        a = int(s)
        print("성공")
    except (ValueError, TypeError) as e:
        a = -1
        print("에러 정보 :", e, file=sys.stderr)
        raise ValueError("Argument에 잘못된 값이 전달되었습니다.") # 일부러 에러를 발생시키고, 에러 메세지를 변경함
    else:
        print("에러가 발생하지 않았어요!")
    finally:
        print("여기는 에러가 발생할 때도, 안할 때도 무조건 실행됩니다.")
    return a

def string_log(s):
    v = convert(s)
    return log(v)

# 만약 파일로 저장하고 싶으면
# python exceptional.py '가나다' 2> c.log
# 를 하면 c.log에 저장된다.