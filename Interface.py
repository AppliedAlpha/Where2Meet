# Import
from enum import Enum


# Menu Enum
# 열거형: .name, .value 로 호출
class Menu(Enum):
    BetweenTime = 1  # 두 역 사이의 시간
    MidPoint = 2  # 두 역 사이의 중간점 찾기
    StationRange = 3  # 한 역에서 시간 내 갈 수 있는 역들 찾기
    Exit = 0  # 종료


menu_text = {
    1: "두 역 사이의 시간 구하기",
    2: "두 역 사이의 중간점 찾기",
    3: "한 역에서 시간 내에 갈 수 있는 역들 찾기",
    0: "종료",
}

color = {
    'Non': '\033[0m',
    'BrightRed': '\033[91m',
    'BrightYellow': '\033[93m',
    'BrightCyan': '\033[96m',
}


# Custom Formatted Print
def fprint(item):
    if type(item) == list:
        print(f'■■■■  {item[0]}  ■■■■')
    elif type(item) == str:
        print(f'□  {item}')
    else:
        print()


# Result Print
def rprint(item):
    print(f'{color["BrightCyan"]}□  {item}{color["Non"]}')


# Notice Print
def nprint(item):
    print(f'{color["BrightYellow"]}□  {item}{color["Non"]}')


# Error Print
def errprint(item):
    print(f'{color["BrightRed"]}□  {item}{color["Non"]}')


def print_menu():
    fprint(['메뉴'])
    for item in Menu:
        fprint(f'{item.value}. {menu_text[item.value]}')


def get_input():
    return input("□  실행할 메뉴 번호를 입력하세요: ")


def get_next_menu():
    print_menu()
    idx = get_input()

    return Menu(int(idx))
