# 장르를 기준: 장르별 총 재생 횟수로 순서 나열, 그 후에 장르 내에서 재생 횟수가 높은 노래

import operator

def solution(genres, plays):
    # 장르 : [(고유 번호, 재생 횟수), ...]
    genres_types = {genre: [] for genre in set(genres)}
    for i, (g, p) in enumerate(zip(genres, plays)):
        genres_types[g] += [(i, p)]

    # 그 후 정렬을 해서 재생 횟수가 높은 원소 순으로 나열 (재생 횟수가 같다면 고유 번호가 낮은 순으로)
    for g in genres_types:
        genres_types[g] = sorted(genres_types[g], key=lambda x: x[1] , reverse=True)
        # genres_types[g] = sorted(genres_types[g], key=operator.itemgetter(1), reverse=True)

    # 각 장르 별로 재생 횟수를 모두 더한 값을 키로, 재생 횟수가 많은 원소 두 개만 리스트로 추린다.
    # 장르 총 재생 횟수를 키, 값은 [고유 번호, 고유 번호]
    total = {}
    for g in genres_types:
        temp = 0
        for p in genres_types[g]:
            temp = temp + p[1]
        total[temp] = genres_types[g][0:2]

    total = sorted(total.items(), reverse=True)
    answer = []

    for g in total:
        for p in g[1]:
            answer.append(p[0])

    return answer


def solution(genres, plays):
    # 장르 : [(고유 번호, 재생 횟수), ...]
    # genres_types = dict.fromkeys(set(genres), [])
    # dict.fromkeys를 사용하여 초기화할 때, 모든 키에 동일한 빈 리스트 객체가 할당된다. 이로 인해 한 키에 요소를 추가하면, 모든 키에 동일한 요소가 추가되는 문제가 발생한다.
    genres_types = {genre: [] for genre in set(genres)}
    for i, (g, p) in enumerate(zip(genres, plays)):
        genres_types[g] += [(i, p)]

    # 장르별 재생 횟수가 높은 장르순으로 sort
    genres_types = sorted(genres_types.items(), key=lambda x: sum(map(lambda y: y[1], x[1])), reverse=True)

    # 장르 내 재생 횟수가 높은 노래순으로 나열 (재생 횟수가 같다면 고유 번호가 낮은 순으로)
    answer = []
    for g in genres_types:
        sorted_plays = [p[0] for p in sorted(g[1], key=lambda x: (x[1], -x[0]) , reverse=True)]
        answer += sorted_plays[:min(len(sorted_plays), 2)]
        # genres_types[g] = sorted(genres_types[g], key=operator.itemgetter(1), reverse=True)
    return answer


def solution(genres, plays):
    answer = []

    # 장르 : [(재생 횟수, 고유 번호), ...]
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])

    # 장르별 재생 횟수가 높은 장르순으로 sort
    genre_sort = sorted(list(d.keys()), key= lambda x: sum(map(lambda y: y[0], d[x])), reverse = True)

    # 장르별 순서에 맞게 재상 횟수가 높은 노래를 sort해서 answer에 넣는다.
    for g in genre_sort:
        temp = [e[1] for e in sorted(d[g], key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer


def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []

    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)

    # while len(dic) > 0:
    #     play_genre = dic.pop(0)
    for genre, _ in dic:
        cnt = 0;
        for ab in album_list:
            if genre == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))