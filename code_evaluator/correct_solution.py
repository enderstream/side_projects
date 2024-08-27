from itertools import permutations

# 일일이 변수로 분리하고 if-else문으로 구현 -> 실행시간 1.3초 : 통과

def baseball_simulator(game: list, player_perm: list, N: int) -> int:
    score = 0
    innings = 0
    hit_order = 0
    while innings < N:
        # base = [0, 0, 0, 1]  # 0:3루 / 1:2루 / 2:1루
        # base = [0] * 3
        base_3 = 0 # 3루
        base_2 = 0 # 2루
        base_1 = 0 # 1루
        out = 0
        while out < 3:
            hitter = player_perm[hit_order]  # 큐 보다 리스트 인덱싱이 더 빠른가?
            hit_order = (hit_order + 1) % 9
            ball_hit = game[innings][hitter]
            if not ball_hit:
                out += 1
            elif ball_hit == 1:
                score += base_3
                base_1, base_2, base_3 = 1, base_1, base_2
            elif ball_hit == 2:
                score += (base_3 + base_2)
                base_1, base_2, base_3 = 0, 1, base_1
            # else:
            elif ball_hit == 3:
                score += (base_3 + base_2 + base_1)
                base_1, base_2, base_3 = 0, 0, 1
            else: # ball_hit == 4:
                score += (base_3 + base_2 + base_1 + 1)
                base_1, base_2, base_3 = 0, 0, 0
                
            # else:
                # score += sum(base[:ball_hit])
                # for j in range(4 - ball_hit):
                #     base[j] = base[j + ball_hit]
                # for j in range(4 - ball_hit, 4):
                #     base[j] = 0
                # base[3] = 1

                # score += base_3
                # base_3, base_2, base_1 = base_2, base_1, 1
                # for _ in range(1, game[innings][hitter]):
                #     score += base_3
                #     base_3, base_2, base_1 = base_2, base_1, 0
        innings += 1
    return score


def correct_solution(N, result):
    max_score = 0
    player_perm_t = permutations(range(1, 9), 8)
    for perm in player_perm_t:
        players = list(perm[:3]) + [0] + list(perm[3:])
        max_score = max(max_score, baseball_simulator(result, players, N))

    return max_score
