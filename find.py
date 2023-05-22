from models import Author, Qoutes
import connect
import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

authors = Author.objects()
qoutes = Qoutes.objects()

@cache
def find_by_name(author_name):
    print("Called function 'find_by_name'")
    result = []
    for qoute in qoutes:
        if author_name.startswith(qoute.author.fullname.lower()[0:2])\
            or author_name == qoute.author.fullname.lower():
            result.append(qoute.qoute)
    return result

@cache
def find_by_tag(tag):
    print("Called function 'find_by_tag'")
    result = []
    for qoute in qoutes:
        for i in qoute.tags:
            if tag.startswith(i[0:2]):
                result.append(qoute.qoute)
                break
            elif tag.lower() == i:
                result.append(qoute.qoute)
                break
    return result


def find_by_tags(tags):
    for qoute in qoutes:
        for tag in tags:
            if tag.lower() in qoute.tags:
                print(qoute.qoute)
                break


def print_list(some_list):
    print("Called function 'print_list'")
    for i in some_list:
        print(i)


def inputting():
    while True:
        inp = input()
        splited_input = inp.lower().split(":")
        if splited_input[0] == "name":
            name_list = find_by_name(splited_input[1][1:])
            print_list(name_list)
        elif splited_input[0] == "tag":
            pass
            tag_list = find_by_tag(splited_input[1])
            print_list(tag_list)
        elif splited_input[0] == "tags":
            tags = splited_input[1].split(",")
            find_by_tags(tags)
        elif splited_input[0] == "exit":
            break
        print("\nEnter 'name:' name, 'tag:' tag or 'tags:' tags or 'exit'")




if __name__=="__main__":
    print("Enter 'name:' name, 'tag:' tag or 'tags:' tags")
    inputting()