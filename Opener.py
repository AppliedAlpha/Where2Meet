routes = [
    'SL1.txt'
]


# 노선들 파일 내용 읽어들이기
def read():
    adj = {}
    stations = set()

    for route in routes:
        with open(f'Routes/{route}', encoding='utf-8') as file:
            lines = file.readlines()

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

    return adj, stations
