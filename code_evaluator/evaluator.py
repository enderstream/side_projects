from solution import solution
from pathlib import Path
from timeit import default_timer as timer


def read_file_into_integer_list(fileName: Path):
    """
    Read integers in filename into a list and return the list
    This function is used for evaluation
    """
    # Use the location of the current .py file
    filePath = Path(__file__).parent / fileName
    result = []

    with filePath.open("r") as f:
        # 파일의 각 줄을 읽어들여 처리
        for line in f:
            line = line.strip()  # 공백 제거
            if len(line):
                if line.isnumeric():
                    result.append(int(line))
                else:
                    result.append(list(map(int, line.split())))

    return result


if __name__ == "__main__":
    print("소스코드 채점을 시작합니다.")
    max_elapsed_time = 0.0
    for testcase_num in range(1, 3 + 1):  # 테스트케이스 개수
        print(f"{testcase_num}번 테스트케이스:", end=" ")
        inputs = read_file_into_integer_list(f"./input/input{testcase_num}.txt")
        outputs = read_file_into_integer_list(f"./output/output{testcase_num}.txt")

        N = inputs[0]
        result = [inputs[i + 1] for i in range(N)]
        correct_answer = outputs[0]
        try:
            start_time = timer()
            answer = solution(N, result)
            elapsed_time = timer() - start_time

            if answer != correct_answer:
                print("틀렸습니다. 반례가 존재합니다. 로직이 잘못됐습니다.")
                break
            elif elapsed_time > 100.0:
                print("제한시간 초과. 너무 느립니다. 최적화가 필요합니다.")
                break
            else:
                print(f"정답.")
                max_elapsed_time = max(max_elapsed_time, elapsed_time)
        except Exception as e:
            print(f"오류 발생: {e}")
            break
    else:
        print("맞았습니다!")
        print(f"최장 실행 시간 : {max_elapsed_time:.5f}초")
