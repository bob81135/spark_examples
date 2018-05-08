# spark_examples
# spark簡單語法(Python)

### 測試資料(test.txt)：
a,123,456,789,11344,2142,123
b,1234,124,1234,123,123
c,123,4123,5435,1231,5345
d,123,456,789,113,2142,143
e,123,446,789,14,2142,113
f,123,446,789,14,2142,1113,323

### map練習
找出測試資料所有的英文字母
結果如下：
a
b
c
d
e
f

code：
```python=
from pyspark import SparkContext

logFile = "test.txt"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numBs = logData.map(lambda s: s.split(',')).collect()
for i in numBs:
    print(i[0])
```
結果：
![](https://i.imgur.com/gBG6Mkc.png)
### flatmap練習
找出測試資料所有以","切割的資料
結果如下：
a
123
456
789
11344
2142
123
......

code：
```python=
from pyspark import SparkContext

logFile = "test.txt"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numBs = logData.flatMap(lambda s: s.split(',')).collect()
for i in numBs:
    print(i)

```
結果：
![](https://i.imgur.com/9X4C4FY.png)
### filter練習
找出測試資料所有以123與456的資料
結果如下：
123
456
123
1234
1234
.....
code：
```python=
from pyspark import SparkContext

logFile = "test.txt"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numBs = logData.flatMap(lambda line: line.split(',')).filter(lambda line:  "123"  in line or "456" in line).collect()
print(numBs)
for i in numBs:
    print(i)

```
結果：
![](https://i.imgur.com/TIJgW6u.png)
### mapToPair 練習
將測試資料轉換成(str,1)
結果如下：
(a,1)
(123,1)
(456,1)
(789,1)
.....
code：
```python=
from pyspark import SparkContext

logFile = "test.txt"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()
numBs = logData.flatMap(lambda s : s.split(",")).map(lambda b: (b,1)).collect()
for i in numBs:
    print(i)

```
結果：
![](https://i.imgur.com/PGbRZ0Z.png)
### flatMapToPair 練習
將測試資料轉換成(字母,所有後面數字的sum)
結果如下：
(a,14977)
(b,2838)
(c,16257)
(d,3766)
(e,3627)
(f,4950)

....
code：
```python=
from pyspark import SparkContext

logFile = "test.txt"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()
numBs = logData.map(lambda s : s.split(",")).map(lambda b: (b[0][0], sum(map(int ,b[1:])))).collect()
for i in numBs:
    print(i)


```
結果：
![](https://i.imgur.com/XQ161LE.png)
### reduce 練習
找出測試資料所有英文字母,並用reduce將之append成一個字串
結果如下：
abcdef

code：
```python=
from pyspark import SparkContext
import re
a=[]
logFile = "test.txt"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()
numBs = logData.flatMap(lambda line: line.split(',')).filter(lambda ss: re.sub("[0-9]" ,"", ss)).collect()
for i in numBs:
    a.append(str(i))
print(a)

```
結果：
![](https://i.imgur.com/t9DMeJq.png)
### reduceByKey 練習
找出以","切割的所有wordcount
結果如下：
(d,1)
(1113,1)
(1231,1)
(e,1)
(14,2)
(113,2)
.......
code：
```python=
from pyspark import SparkContext
from operator import add
logFile = "test.txt"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()
numBs = logData.flatMap(lambda s : s.split(",")).map(lambda b: (b,1)).reduceByKey(add).collect()
for i in numBs:
    print(i)

```
結果：
![](https://i.imgur.com/VhAoD3c.png)

