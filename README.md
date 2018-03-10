# Python numpy 연습

##### numpy로 배열을 선언할 때와 그냥 선언할 때 연산을 하면 다르게 나온다.
```python
import numpy as np
if __name__ == '__main__':
    
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(a+b) #[5 7 9]
    
    c = [1, 2, 3]
    d = [4, 5, 6]
    print(c+d) #[1, 2, 3, 4, 5, 6]
    
    pass
```