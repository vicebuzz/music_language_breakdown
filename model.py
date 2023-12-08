import json
import pandas as pd
import numpy as np

import sparknlp
import pyspark.sql.functions as F

from pyspark.ml import Pipeline
from pyspark.sql import SparkSession
from sparknlp.annotator import *
from sparknlp.base import *
from sparknlp.pretrained import PretrainedPipeline
from pyspark.sql.types import StringType, IntegerType

spark = sparknlp.start()
print ("Spark NLP Version :", sparknlp.version())
spark

# model_name = 'ld_wiki_cnn_231'
model_name = 'ld_wiki_tatoeba_cnn_43'

# load pandas dataframe
songs_df = pd.read_csv("My Apple Music Library.csv")

text_list = songs_df["Track name"]

documentAssembler = DocumentAssembler()\
            .setInputCol("text")\
            .setOutputCol("document")

sentence_detector = SentenceDetector() \
            .setInputCols(["document"]) \
            .setOutputCol("sentence")

languageDetector = LanguageDetectorDL.pretrained(model_name)\
            .setInputCols("sentence")\
            .setOutputCol("language")\
            .setThreshold(0.5)\
            .setCoalesceSentences(True)

nlpPipeline = Pipeline(
    stages=[ 
        documentAssembler, 
        sentence_detector,
        languageDetector])

df = spark.createDataFrame(text_list, StringType()).toDF("text")
result = nlpPipeline.fit(df).transform(df)


view = result.select(F.explode(F.arrays_zip(result.document.result, 
                                     result.language.result)).alias("cols")) \
      .select(F.expr("cols['0']").alias("Song"),
              F.expr("cols['1']").alias("Language"))

view.write.format("csv").save("result")