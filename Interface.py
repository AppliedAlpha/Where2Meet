# Import
from enum import Enum


# Menu Enum
# 열거형: .name, .value로 호출
class Menu(Enum):
    BetweenTime = 1  # 두 역 사이의 시간
    MidPoint = 2  # 두 역 사이의 중간점 찾기
    StationInfo = 3  # 한 역에서의 최소시간표
    Exit = 0  # 종료


menu_text = {
    1: "두 역 사이의 시간 구하기",
    2: "두 역 사이의 중간점 찾기",
    3: "역 시간표 구하기 (최소시간)",
    0: "종료"
}


# Custom Formatted Print
def fprint(item):
    if type(item) == list:
        print(f'■■■■  {item[0]}  ■■■■')
    elif type(item) == str:
        print(f'□  {item}')
    else:
        print()


def print_menu():
    for item in Menu:
        fprint(f'{item.value}. {menu_text[item.value]}')


def get_input():
    return input("□  실행할 메뉴 번호를 입력하세요: ")


def init_run():
    while True:
        print_menu()
        idx = get_input()

        try:
            next = Menu(int(idx))
            print(Menu(int(idx)))

        except ValueError as err:
            print(str(err))
