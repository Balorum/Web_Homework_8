from models import Author, Qoutes
import connect
import json
from datetime import datetime


with open("authors.json", "r") as author:
    authors = json.load(author)
with open("qoutes.json", "r") as qoute:
    qoutes = json.load(qoute)


for auth in authors:
    date_time_str = auth["born_date"]
    date_time_obj = datetime.strptime(date_time_str, '%B %d, %Y')
    Author(fullname=auth["fullname"], born_date=date_time_obj.date()\
            , born_location=auth["born_location"], description=auth["description"]).save()


got_authors = Author.objects()
for qout in qoutes:
    for i in got_authors:
        if i.fullname == qout["author"]:
            Qoutes(tags=qout["tags"], author=i, qoute=qout["quote"]).save()
