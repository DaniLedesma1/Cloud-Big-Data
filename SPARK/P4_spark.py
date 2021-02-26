import pyspark as ps
from pyspark.sql import SQLContext

conf = ps.SparkConf().setMaster("local[4]").setAppName("p4_spark")
sc = ps.SparkContext(conf=conf)


textPath = 'ratings.csv'
sqlContext = SQLContext(sc)
df = sqlContext.read.csv(textPath)

dataDF = df.select("_c1", "_c2")


cabecera = dataDF.rdd.first()
dataRDD = dataDF.rdd.filter(lambda x: x != cabecera)
dataRDD = dataRDD.map(lambda x: (int(x._c1.encode('utf-8').split("-")[0]), float(x._c2.encode('utf-8'))))


datos = dataRDD.groupByKey().map(lambda x: (x[0], list(x[1])))
suma = datos.map(lambda x: (x[0], sum(x[1])))
elementos = datos.map(lambda x: (x[0], len(x[1])))

union = suma.join(elementos)
media = union.map(lambda x: (x[0], x[1][0]/x[1][1]))

rddAverage = media.sortByKey().collect()


lista = ["", "", "", "", ""]

for line in rddAverage:
    idPeli = line[0]
    valoracion = line[1]

    if float(valoracion) <= 1:
        lista[0] += str(idPeli) + ", "
    elif 1 < float(valoracion) <= 2:
        lista[1] += str(idPeli) + ", "
    elif 2 < float(valoracion) <= 3:
        lista[2] += str(idPeli) + ", "
    elif 3 < float(valoracion) <= 4:
        lista[3] += str(idPeli) + ", "
    else:
        lista[4] += str(idPeli) + ", "


for i, rang in enumerate(lista):
    print("Rango {}: {}\n\n".format(i + 1, rang[:len(rang) - 2]))