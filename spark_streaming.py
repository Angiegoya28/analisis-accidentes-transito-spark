from pyspark.sql import SparkSession
from pyspark.sql.functions import col,from_json
from pyspark.sql.types import StructType,StructField, IntegerType, DoubleType, LongType


spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()


df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers",
"localhost:9092") \
    .option("subscribe", "sensor_data") \
    .load()


datos = df.selectExpr("CAST(value AS STRING)")

esquema = StructType([
    StructField("sensor_id", IntegerType()),
    StructField("temperature", DoubleType()),
    StructField("humidity", DoubleType()),
    StructField("timestamp", LongType()),
])

datos = datos.select(
    from_json(col("value"),
esquema).alias("data")
).select("data.*")

datos.writeStream \
    .format("console") \
    .outputMode("append") \
    .option("truncate","false") \
    .start() \
    .awaitTermination() 
