words = "나는 파이썬을 공부하고 있습니다. 파이썬은 무척 심플하고 명료합니다.".split()
words = {len(word) for word in words if len(word) > 3}
print(words)