import connect
from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ReferenceField, DateTimeField, EmbeddedDocumentField, ListField, StringField


class Author(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Qoutes(Document):
    tags = ListField()
    author = ReferenceField(Author)
    qoute = StringField()