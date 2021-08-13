# How to import
# import [Name]  // Local
# from . import [Name]  // Production
import sys
import heapq

import Interface
from Interface import Menu, fprint
import Opener

# 노선도(그래프), 역 목록(집합) 선언
adj = {}
stations = set()


# 역간 최단시간 구하기용 다익스트라 알고리즘
def dijkstra(start):
    dist = {node: sys.maxsize for node in adj}
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (dist[start], start))

    while queue:
        now_dist, node = heapq.heappop(queue)
        if dist[node] < now_dist:
            continue

        for adj_node, adj_dist in adj[node].items():
            total_dist = now_dist + adj_dist

            if total_dist < dist[adj_node]:
                dist[adj_node] = total_dist
                heapq.heappush(queue, (total_dist, adj_node))

    return dist


def run():
    # 전역 변수 로딩
    global adj, stations

    while True:
        try:
            # 메뉴 받아오기
            next_menu = Interface.get_next_menu()
            # print(next_menu)

            if next_menu == Menu.BetweenTime:
                pass

            elif next_menu == Menu.MidPoint:
                pass

            elif next_menu == Menu.StationInfo:
                depart = input('□  검색할 역을 입력하세요: ')

                # 최단시간 계산 후 출력
                print(f'{depart}: {dijkstra(depart)}')

            elif next_menu == Menu.Exit:
                fprint('프로그램을 종료합니다.')
                del adj, stations
                return

        except Exception as err:
            print(str(err))  # 추후 errprint로 user-define해서 사용


# 실행
if __name__ == '__main__':
    print("프로그램이 실행되었습니다.")

    # 파일 읽어오기
    adj, stations = Opener.read()

    # 수도권 전철 1호선 초기 로드 완료
    # 입력받고 프로그램 진행
    print(f'{len(stations)}개의 역을 성공적으로 로드했습니다.')
    print(stations)

    run()
