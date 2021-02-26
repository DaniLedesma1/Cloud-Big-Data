import pyspark as ps

conf = ps.SparkConf().setMaster("local[4]").setAppName("p2_spark")
sc = ps.SparkContext(conf=conf)


textPath = 'access_log'

textRDD = sc.textFile(textPath)

rows = textRDD.map(lambda line: (line.split(" ")[0], 1))

urlfrecuency = rows.reduceByKey(lambda x, y: x + y)

print(urlfrecuency.collect())
