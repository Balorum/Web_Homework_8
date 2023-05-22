import connect
from mongoengine import Document
from mongoengine.fields import BooleanField, StringField


class Contact(Document):
    fullname = StringField()
    email = StringField()
    query_flag = BooleanField(default=False)
    phone = StringField()