#삽입정렬(insertion sort)
#처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
#선택 정렬에 비해 구현 난이도가 높은편이지만, 일반적으로 더 효율적
#시간복잡도O (n**2)
#최선의 경우:현재 리스트의 데이터가 거의 정렬되어 있는상태 시간복잡도 O(n)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1): # 인덱스 i 부터 1까지 1씩 감소
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
