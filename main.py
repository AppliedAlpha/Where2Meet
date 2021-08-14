# How to import
# import [Name]  // Local
# from . import [Name]  // Production
import Interface
import Execution

from Interface import Menu, fprint


def run():
    while True:
        try:
            # 메뉴 받아오기
            next_menu = Interface.get_next_menu()
            # print(next_menu)

            if next_menu == Menu.BetweenTime:
                Execution.between_time()

            elif next_menu == Menu.MidPoint:
                Execution.mid_point()

            elif next_menu == Menu.StationRange:
                Execution.station_range()

            elif next_menu == Menu.Exit:
                fprint('프로그램을 종료합니다.')
                return

        except ValueError:
            print('값의 입력이 잘못되었거나, 데이터가 올바르지 않습니다.')

        except Exception as err:
            print(err)  # 추후 errprint로 user-define해서 사용

        finally:
            print()


# 프로그램 실행
if __name__ == '__main__':
    print("프로그램이 실행되었습니다.")

    Execution.read()
    Execution.check_load()
    run()
