### key_lambda 사용한 정렬
- 오름 차순으로 정렬된다.

정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.

key 값을 기준으로 정렬되고 기본값은 오름차순이다. 
```python
str_list = ['좋은하루','good_morning','굿모닝','niceday']
print(sorted(str_list, key=len))  # 함수
['굿모닝', '좋은하루', 'niceday', 'good_morning']

print(sorted(str_list, key=lambda x : x[1]))  # 람다
['niceday', 'good_morning', '굿모닝', '좋은하루']
``` 

여러 개의 요소를 가진 경우, 튜플로 사용할 수 있다.

```python
>>> tuple_list = [('좋은하루', 0),
    	          ('niceday', 1), 
    	          ('좋은하루', 5), 
    	          ('good_morning', 3), 
    	          ('niceday',5)]
                  
>>> tuple_list.sort(key=lambda x : (x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능
>>> print(tuple_list)
[('good_morning', 3), ('niceday', 1), ('niceday', 5), ('좋은하루', 0), ('좋은하루', 5)]
