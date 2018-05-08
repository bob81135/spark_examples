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







