# coding:utf-8

import os
import glob
import json
import datetime
import csv

fp = open("kickstarter_result.csv", "wb")
cw = csv.writer(fp,lineterminator="\n")

cw.writerow([
    "project_id",
    "category",
    "pledged","goal",
    "currency",
    "backers_count",
    "state",
    "name",
    "launched_at",
    "deadline",
    "blurb",
    "url",
    "creator_id",
    "country"
    ])

for filename in glob.glob("result/*.json"):
    project = json.loads(open(filename).read())

    items = []
    items.append(project['id'])
    items.append(project["category"]["slug"])
    items.append(project["pledged"])
    items.append(project["goal"])
    items.append(project["currency"])
    items.append(project["backers_count"])
    items.append(project["state"])
    items.append(project["name"])
    items.append(str(datetime.datetime.fromtimestamp(project["launched_at"])))
    items.append(str(datetime.datetime.fromtimestamp(project["deadline"])))
    items.append(project["blurb"].replace("\n", " ").replace("\r", " ").replace("," , " "))
    items.append(project["urls"]["web"]["project"])
    items.append(project['creator']['id'])
    items.append(project['country'])


    out = []
    for item in items:
        if type(item) is unicode:
            item = item.encode("shift-jis", "ignore")
        else:
            item = str(item)
        out.append(item)
    cw.writerow(out)
    print filename
fp.close()


