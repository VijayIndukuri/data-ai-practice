import pyspark
from pyspark.sql import SparkSession
#import pandas as pd

#pd.read_csv('heart_attack_indonesia.csv')

spark = SparkSession.builder.appName('Practice').getOrCreate()
df_pyspark = spark.read.option('header','true').csv('heart_attack_indonesia.csv')
#df_pyspark.printSchema()
#df_pyspark.select(['Age', 'HeartAttack']).show()
df_pyspark.describe().show()
#df_pyspark.drop('OccupationType')  # drop()   # fill()   # replace()  .na.drop(how="any/all", thres=2, subset=['OccupationType',]) -< na -> drops when null values exist
