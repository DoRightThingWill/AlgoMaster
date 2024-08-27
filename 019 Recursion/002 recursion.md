## 递归三要素

- 定义，名称，输入，输出
- 终止条件
- transition

## 尾递归

尾递归，直接从第一函数，向最后一层要一个值，中间的所有递归函数，都当做 pass thru，相当于透明层，没有创建。这种特殊递归方式，不会引起 stack overlfow

下面这种递归调用，是最常见的模式，可能会引起 stack overflow。妈的，c++, java, python，都不支持尾递归优化，该爆栈，还是会爆，她你吗还优化个毛，不如基础版本，写起来顺手，读起来流畅。

```python
# input and output
def double_factoral(number)-> int:
    # termination
    if nunber <= 2:
        return number
    # transition
    next_factoral = double_factoral(number - 2)
    return number * next_factoral
```

尾递归，是一种特殊的递归调用模式。递归只发生在最后一行的代码中，并且，最后一行代码仅仅只有递归，没有其他操作

下面这个递归，就不是尾递归。因为最后一行，出了有递归，还 🈶️ 一个相乘的操作

```python
def double_factoral(number):
    if number <=2 :
        return number

    return n * double_factoral(number - 2)
```

第三个递归，就是尾递归：

```python
def double_factoral(number, pre_result = 1):
    if number <=2 :
        return number * pre_result

    return double_factoral(number - 2, number * pre_result)
```
