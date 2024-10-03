from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    access_token = fields.CharField(max_length=400)

    def __str__(self):
        return self.username
