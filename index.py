import json
import csv

json_list = []
json_data = {}

# CSVファイルのロード
with open('data.csv', 'r', encoding="shift-jisx0213") as f:
    # list of dictの作成
    for line in csv.DictReader(f):
        json_list.append(line)

    json_data["data"] = json_list

with open('data.json', 'w') as f:
    # JSONへの書き込み
    f.write(json.dumps(json_data,ensure_ascii=False,indent=2))