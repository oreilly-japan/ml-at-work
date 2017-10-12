#coding: utf-8
import urllib.request
import json
import datetime
import os
import time

os.makedirs('result', exist_ok=True)

search_term = ""
sort_key = 'newest'
category_list = [16, 331, 332, 333, 334, 335, 336, 337, 52, 362, 338, 51, 339, 340, 341, 342] # technology category

for category_id in category_list:
    project_count = 0
    for page_id in range(1, 201):
        try:
            query = "http://www.kickstarter.com/projects/search.json?term=%s&category_id=%d&page=%d&sort=%s" % (search_term, category_id, page_id, sort_key)
            response_json = json.loads(urllib.request.urlopen(query).read())
        except:
            break

        if len(response_json["projects"]) == 0:
            break

        project_count += len(response_json["projects"])
        total_hits = response_json["total_hits"]

        print(category_id ,"progress", project_count, "/", total_hits, round(float(project_count)/total_hits * 100, 2), "%")

        for project in response_json["projects"]:
            filepath = "result/%d.json" % project["id"]
            fp = open(filepath, "w")
            fp.write(json.dumps(project, sort_keys=True, indent=2))
            fp.close()

        time.sleep(1)
