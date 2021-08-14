# Import
import sys
import heapq

import Opener

from Interface import fprint
from ExecutionError import ExecutionError

# 노선도(그래프), 역 목록(집합) 선언
adj = {}
stations = set()


# Opener 실행용
def read():
    global adj, stations

    try:
        adj, stations = Opener.read()

    except Exception:
        raise SystemExit('역 정보를 로드하는 데에 실패했습니다.')


# 로드 확인용
def check_load():
    print(f'{len(stations)}개의 역을 성공적으로 로드했습니다.')
    print(stations)


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


# 1. 두 역 사이의 시간 구하기
def between_time():
    try:
        # 역 입력받기
        st = input('□  첫 번째 역을 입력하세요: ')
        en = input('□  두 번째 역을 입력하세요: ')

        # 동일 역 처리
        if st == en:
            raise ExecutionError('입력된 두 역이 동일합니다.')

        # 거리 구하고 출력
        dist = dijkstra(st)[en]
        fprint(f'{st}, {en} 사이의 최소 시간은 {dist}분입니다.')

    # 이하 오류 처리
    except ExecutionError as err:
        raise err

    except ValueError:
        raise Exception('입력된 값이 올바르지 않습니다.')

    except Exception:
        raise Exception('역이 유효하지 않거나, 계산에 실패했습니다.')


# 2. 두 역 사이의 중간점 찾기
def mid_point():
    try:
        # 역 입력받기
        st = input('□  첫 번째 역을 입력하세요: ')
        en = input('□  두 번째 역을 입력하세요: ')

        # 최소시간 테이블 생성
        st_table = dijkstra(st)
        en_table = dijkstra(en)

        # 동일 역 처리
        if st == en:
            raise ExecutionError('입력된 두 역이 동일합니다.')

        # 거리 구하기, 오차 입력받기
        dist = st_table[en]
        diff = int(input('□  오차 허용 범위를 정수형으로 입력하세요 (단위: 분): '))

        # 최소시간 예외 처리
        if st_table[en] < diff:
            msg = f'두 역 사이의 최소시간이 오차 범위보다 짧습니다. ' \
                  f'(입력된 허용 범위: {diff}분, 역 사이 최소 시간: {st_table[en]}분)'
            raise ExecutionError(msg)

        # 해당 역 탐색 및 저장
        # - 출발지로부터 시간, 도착지로부터 시간이 입력된 오차 이내일시
        # - 출발지로부터 시간, 도착지로부터 시간의 합이 둘 사이 최소 시간 이내일시
        # (두 역 사이의 최소 경로 안에 존재함을 보장하기 위함)
        result = []

        for item in st_table.items():
            st_dist = item[1]
            en_dist = en_table[item[0]]
            diff_dist = abs(st_dist - en_dist)

            if st_dist + en_dist <= dist and diff_dist <= diff:
                result.append((item[0], st_dist, en_dist, diff_dist))

        # 부합하는 역 없을 시 처리
        if not result:
            raise ExecutionError('해당 오차 시간 내에 존재하는 역이 없습니다.')

        # 탐색 결과를 오차 기준으로 정렬 후 출력
        result.sort(key=lambda x: x[3])

        fprint(f'다음과 같은 역들을 총 {len(result)}개 탐색했습니다.')  # rprint로 변경
        for item in result:
            fprint(f'{item[0]}: 오차 {item[3]}분 (출발지에서 {item[1]}분, 도착지에서 {item[2]}분)')

    # 이하 오류 처리
    except ExecutionError as err:
        raise err

    except ValueError:
        raise Exception('입력된 값이 올바르지 않습니다.')

    except Exception:
        raise Exception('역이 유효하지 않거나, 계산에 실패했습니다.')


# 3. 한 역에서 시간 내 갈 수 있는 역들 찾기
def station_range():
    try:
        # 역 입력, 최소시간 테이블 생성, 범위 입력받기
        station = input('□  검색할 역을 입력하세요: ')
        table = dijkstra(station)
        time_range = int(input('□  시간 허용 범위를 정수형으로 입력하세요 (단위: 분): '))

        # 결과 처리 (list-comprehension)
        result = [item for item in table.items() if item[1] <= time_range and item[1] != 0]

        # 부합하는 역 없을 시 처리
        if not result:
            raise ExecutionError('해당 시간 범위 내에 존재하는 역이 없습니다.')

        # 탐색 결과를 오차 기준으로 정렬 후 출력
        result.sort(key=lambda x: x[1])

        fprint(f'다음과 같은 역들을 총 {len(result)}개 탐색했습니다.')  # rprint로 변경
        for item in result:
            fprint(f'{item[0]}: {item[1]}분 소요')

    # 이하 오류 처리
    except ExecutionError as err:
        raise err

    except Exception:
        raise Exception('역이 유효하지 않거나, 계산에 실패했습니다.')
