import json

# Input and output paths
input_path = "/home/hadoop/wordcount_project/output/part-00000"
output_path = "/home/hadoop/wordcount_project/wordcount.json"

# Read MapReduce output
word_counts = {}
with open(input_path, "r") as file:
    for line in file:
        word, count = line.strip().split("\t")
        word_counts[word] = int(count)

# Write to JSON file
with open(output_path, "w") as json_file:
    json.dump(word_counts, json_file, indent=4)

print(f"Word count saved to {output_path}")
