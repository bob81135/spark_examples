from pyspark import SparkContext

logFile = "test.txt"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numBs = logData.flatMap(lambda s: s.split(',')).collect()
for i in numBs:
    print(i)


