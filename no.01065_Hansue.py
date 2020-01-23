"""
-문제-
어떤 양의 정수 X의 자리수가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때,
1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

-입력-
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

-출력-
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""


# 한자리와 두자리는 모두 한수.
# 계산 상 110까지 한수는 99개 뿐.
# 입력받은 수 까지 존재하는 모든 수를 검증해야함.
# input이 110 이상일 경우만 계산.
# 110 이상일 경우 110 부터 입력 받은 수까지 카운트.
# 카운트를 문자열 -> 슬라이싱 -> 정수 리스트화
# 각 자리수를 a,b,c,d라 할때 a-b = b-c = c-d가 성립하면 한수.
# 리스트로 받을 경우
# if a <= len(list)-2 and list[a] - list[a+1] == list[a+1]-list[a+2]


def com_diff(lists):
    count = 0
    for i in range(1, int(lists) + 1):
        temp = list(map(int, str(i)))
        if i < 100:
            count += 1
        else:
            if temp[0] - temp[1] == temp[1] - temp[2]:
                count += 1

    print(count)


num_list = input()
com_diff(num_list)
