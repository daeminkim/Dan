### heapq 라이브러리
- 힙(Heap) 기능 제공

다익스트라 최단 경로 알고리즘을 비롯한 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용       
PriorityQueue 라이브러리도 사용가능하지만, *코딩 테스트 환경에서 보통 heapq가 더 빠르게 동작*     
파이썬의 힙은 최소 힙으로 구성되어 있어서 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간복잡도 O(NlogN)에 오름차순 정렬이 완료된다.          
(보통 최소 힙 자료구조의 최상단 원소는 '가장 작은' 원소이기 때문)          

- 힙에 원소를 삽입 *heap.heappush()* 메서드를 사용         
- 힙에서 원소를 꺼낼때 *heap.heappop()* 메서드를 사용     

### 오름차순 heapq정렬 예시 코드       
```python
improt heapq

def heapsort(iterable):
	h = []
    result = []
    # 모든 우너소를 차례대로 힙에 삽입
    for value in iterable:
    	heapq.push(h, vlaue)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내서 담기
   	for i in range(len(h)):
    	result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 출력
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
파이썬에서는 최대 힙을 제공하지 않기 때문에, heapq 라이브러리를 이용해서 최대 힙을 구현해야 할 때는 '-'를 사용하여 임시로 변경하는 방식을 사용한다.   
힙에 원소를 삽입하기 전에 잠시 부호(-)를 반대로 바꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾸면 된다.

### 내림차순 heapq정렬 예시코드
```python
import heapq

def heapsort(iterable):
	h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입 (부호 반대로)
    for value in iterable:
    	heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기 (부호 다시 뒤집어서)
    for i in range(len(h)):
    	result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 출력
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
