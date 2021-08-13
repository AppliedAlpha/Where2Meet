# How to import
# import [Name]  // Local
# from . import [Name]  // Production
import sys
import heapq

import Interface

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


# 실행
if __name__ == '__main__':
    print("프로그램이 실행되었습니다.")

    # 파일 읽어오기
    with open('Routes/SL1.txt', encoding='utf-8') as SL1:
        lines = SL1.readlines()

        # 줄 확인
        for line in lines:
            now = line.strip().split()

            # [출발, 도착, 시간]으로 구성됨
            if len(now) == 3:
                # print(*now)

                st = now[0]
                en = now[1]
                val = int(now[2])

                stations.update([st, en])

                # 무방향 그래프에 간선 추가하기
                try:
                    adj[st][en] = val

                except KeyError:
                    adj[st] = {en: val}

                # 무방향 그래프에 간선 추가하기 (반대 방향)
                try:
                    adj[en][st] = val

                except KeyError:
                    adj[en] = {st: val}

                # print(f'{st}: {adj[st]}, {en}: {adj[en]}')

        # 수도권 전철 1호선 초기 로드 완료
        # 입력받고 프로그램 진행
        print(f'{len(stations)}개의 역을 성공적으로 로드했습니다.')
        print(stations)

        # Interface.init_run()

        depart = input('출발할 역을 입력하세요: ')

        # 에러 핸들링
        # try~ except~ 필요 시 raise로, 바로 종료할 시에는 sys로
        if depart not in stations:
            raise SystemExit('그런 이름의 역이 없습니다!')
            # sys.exit('그런 이름의 역이 없습니다!')

        # 최단시간 계산 후 출력
        print(f'{depart}: {dijkstra(depart)}')
