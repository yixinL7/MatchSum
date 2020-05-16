import json

def load_jsonl(data_path):
    data = []
    with open(data_path) as f:
        for line in f:
            data.append(json.loads(line))
    return data

def average(x):
    cnt = 0
    for i in x:
        cnt += i
    return cnt / len(x)

oracle = load_jsonl("test_CNNDM_bert_new.jsonl")
bertsum = load_jsonl("test_CNNDM_bert_sum.jsonl")

avg_oracle, avg_bertsum = 0, 0
for i in range(len(oracle)):
    oracle_score = oracle[i]["score"]
    bertsum_score = bertsum[i]["score"]
    # print(max(oracle_score))
    # print(max(bertsum_score))
    # print()
    avg_bertsum += max(bertsum_score)
    avg_oracle += max(oracle_score)

print(avg_oracle / len(oracle))
print(avg_bertsum / len(oracle))