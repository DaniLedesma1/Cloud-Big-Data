import pyspark as ps
from pyspark.sql import SQLContext

conf = ps.SparkConf().setMaster("local[4]").setAppName("p5_spark")
sc = ps.SparkContext(conf=conf)


textPath = 'Meteorite_Landings.csv'
sqlContext = SQLContext(sc)
df = sqlContext.read.csv(textPath)

dataDF = df.select("_c2", "_c4")

NoneType = type(None)
dataRDD = dataDF.rdd.filter(lambda x: type(x._c2) != NoneType and type(x._c4) != NoneType)
dataRDD = dataRDD.map(lambda x: (x._c2.encode('utf-8').split("-")[0], float(x._c4.encode('utf-8'))))

datos = dataRDD.groupByKey().map(lambda x: (x[0], list(x[1])))
suma = datos.map(lambda x: (x[0], sum(x[1])))
elementos = datos.map(lambda x: (x[0], len(x[1])))

union = suma.join(elementos)
media = union.map(lambda x: (x[0], x[1][0]/x[1][1]))

print(media.sortByKey().collect())
