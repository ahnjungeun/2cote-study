M = [list(map(int,input().split())) for _ in range(5)]
C = [list(map(int,input().split())) for _ in range(5)]
f = False
c=k=0

for i in C:
    # j = 현재 부른 수
    for j in i:
        k+=1
        # 부른 수 체크하기! 불렀으면 0으로 기록
        for a in range(5):
            for b in range(5):
                if M[a][b] == j:
                    M[a][b] = 0
                    print(k)
                    print(*M,sep='\n')
                    print()

                # 이 부분 인터넷 참고함!
                # 빙고인지 확인하기
                for z in range(5):
                    # if-elif로 하면 안 됨. 그럼 뒷조건 확인 안 하고 넘어감
                    # 가로 합
                    if sum(M[z])==0:
                        c+=1
                    # 세로 합
                    if sum([x[z] for x in M])==0:
                        c+=1
                # 대각선 합
                if M[0][0]+M[1][1]+M[2][2]+M[3][3]+M[4][4] == 0:
                    c+=1
                if M[4][0]+M[3][1]+M[2][2]+M[1][3]+M[0][4] == 0:
                    c+=1
                
                # 3빙고면 멈춤
                if c >= 3:
                    f = True
                    break
                # c 누적되면 안 되니 초기화하기! 그 순간순간마다 체크
                else:
                    c = 0
        # n중 반복문 탈출하기 ^^;
        if f:
            break
    if f:
        break
                
print(k)