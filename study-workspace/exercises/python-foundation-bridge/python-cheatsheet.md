# Python 写法对照表

目标：把中文思路翻译成 Python 写法。

## 基础数据结构

| 中文思路 | Python 写法 | 例子 |
|---|---|---|
| 创建列表 | `items = []` | `scores = [80, 90, 75]` |
| 添加元素 | `items.append(x)` | `scores.append(88)` |
| 遍历列表 | `for item in items:` | `for score in scores:` |
| 创建字典 | `data = {}` | `counts = {}` |
| 读取字典值 | `data[key]` 或 `data.get(key, default)` | `counts.get("a", 0)` |
| 更新计数 | `counts[key] = counts.get(key, 0) + 1` | 统计字符、单词最常用 |
| 创建集合 | `seen = set()` | 用来去重 |
| 判断是否出现过 | `if x in seen:` | 去重、查找 |

## 常见流程

### 逐个处理

```python
result = []
for item in items:
    result.append(item * 2)
```

### 条件筛选

```python
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
```

### 计数

```python
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
```

### 封装成函数

```python
def count_characters(text):
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts
```

## 最常用内置函数

| 函数 | 用途 | 例子 |
|---|---|---|
| `len(x)` | 长度 | `len(items)` |
| `sum(x)` | 求和 | `sum(scores)` |
| `max(x)` | 最大值 | `max(scores)` |
| `min(x)` | 最小值 | `min(scores)` |
| `sorted(x)` | 排序并返回新列表 | `sorted(scores)` |
| `range(n)` | 生成 0 到 n-1 | `for i in range(5):` |
| `enumerate(x)` | 同时拿索引和值 | `for i, item in enumerate(items):` |
| `zip(a, b)` | 同时遍历两个列表 | `for x, y in zip(xs, ys):` |

## 先记住的调试方法

```python
print(type(value))
print(value)
print(len(value))
```

不会写时，不要空想，先打印对象是什么。
