import pyspark as ps
from pyspark.sql import SQLContext

conf = ps.SparkConf().setMaster("local[4]").setAppName("p3_spark")
sc = ps.SparkContext(conf=conf)


textPath = 'GOOGLE.csv'
sqlContext = SQLContext(sc)
df = sqlContext.read.csv(textPath)

dataDF = df.select("_c0", "_c4")


cabecera = dataDF.rdd.first()
dataRDD = dataDF.rdd.filter(lambda x: x != cabecera)
dataRDD = dataRDD.map(lambda x: (int(x._c0.encode('utf-8').split("-")[0]), float(x._c4.encode('utf-8'))))


datos = dataRDD.groupByKey().map(lambda x: (x[0], list(x[1])))
suma = datos.map(lambda x: (x[0], sum(x[1])))
elementos = datos.map(lambda x: (x[0], len(x[1])))

union = suma.join(elementos)
media = union.map(lambda x: (x[0], x[1][0]/x[1][1]))

print(media.sortByKey().collect())