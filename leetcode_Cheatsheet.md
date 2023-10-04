### leetcode Cheatsheet


##### Two pointers: one input, opposite ends
<details>
  <summary>Two pointers: one input, opposite ends - python3</summary>

```python
def fn(arr):
    left = ans = 0
    right = len(arr) - 1

    while left < right:
        # do some logic here with left and right
        if CONDITION:
            left += 1
        else:
            right -= 1
    
    return ans
```

</details>

##### Two pointers: two inputs, exhaust both
<details>
  <summary>Two pointers: two inputs, exhaust both - python3</summary>
  
```python
def fn(arr1, arr2):
    i = j = ans = 0

    while i < len(arr1) and j < len(arr2):
        # do some logic here
        if CONDITION:
            i += 1
        else:
            j += 1
    
    while i < len(arr1):
        # do logic
        i += 1
    
    while j < len(arr2):
        # do logic
        j += 1
    
    return ans
```
  
</details>


