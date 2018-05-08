from pyspark import SparkContext

logFile = "test.txt"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numBs = logData.flatMap(lambda line: line.split(',')).filter(lambda line:  "123"  in line or "456" in line).collect()
print(numBs)
for i in numBs:
    print(i)




