from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder  \
    .appName("AccidentesTransito")  \
    .master("local[*]")  \
    .config("spark.hadoop.fs.defaultFS", "file:///") \
    .getOrCreate()

df = spark.read.option("header",True) \
    .option("inferSchema", True) \
    .csv("/home/angiegoya28/accidentes_transito.csv")

print ("ESTRUCTURA DE LOS DATOS")
df.printSchema()

print ("PRIMEROS 5 REGISTROS")
df.show(5, truncate=False)

print ("ACCIDENTES POR DEPARTAMENTO")
df.groupBy("departamento_accidente") \
    .count().orderBy(col("count").desc()).show(10, truncate=False)

print ("ACCIDENTES SEGUN GRAVEDAD")
df.groupBy("gravedad_accidente") \
    .count().orderBy(col("count").desc()).show(truncate=False)

spark.stop()
