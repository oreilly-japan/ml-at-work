# coding:utf-8

import glob
import json
import pandas
import pandas.io.json

project_list = []

for filename in glob.glob("result/*.json"):
    project = json.loads(open(filename).read())
    project_list.append(project)

df = pandas.io.json.json_normalize(project_list)

datetime_columns = filter(lambda a: a[-3:] == "_at", df.columns)
for column in datetime_columns:
    df[column] = pandas.to_datetime(df[column], unit='s')

csv_data = df.to_csv()
csv_data = csv_data.encode("cp932", "ignore")
fp = open("kickstarter_result.csv", "wb")
fp.write(csv_data)
fp.close()
