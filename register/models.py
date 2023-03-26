from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    salt = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    isdelete = models.BooleanField(default=False)
    avatar = models.CharField(max_length=255)

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)

        return d

    def toString(self, uid):
        print("userinfo: uid: " + str(uid) + ",name: " + self.name + ",email: " + str(self.email)
              + ",salt: " + self.salt + ",passwd: " + self.passwd + ",time: " + self.time
              + ",isdelete: " + str(self.isdelete) + ",avatar: " + self.avatar)
