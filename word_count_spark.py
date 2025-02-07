from pyspark import SparkConf, SparkContext
import json

if __name__ == "__main__":
    conf = SparkConf().setAppName("WordCount")
    sc = SparkContext(conf=conf)

    # Load dataset from HDFS (Make sure this path is correct)
    text_file = sc.textFile("hdfs:///input/*.txt")

    # Perform word count
    counts = text_file.flatMap(lambda line: line.lower().split()) \
                      .map(lambda word: (word, 1)) \
                      .reduceByKey(lambda a, b: a + b)

    # Save results to JSON
    results = counts.collect()
    with open("/home/shiza/wordcount_project/wordcount_spark.json", "w") as file:
        json.dump(dict(results), file, indent=4)

