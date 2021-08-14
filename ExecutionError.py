# 실행 시의 오류를 다루는 custom-Error 클래스
class ExecutionError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
