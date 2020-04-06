from django.db import models


class Building(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=255)

    def natural_key(self):
        return self.code

    def __str__(self):
        return self.name

    class Meta:
        db_table = "building"


class Room(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.IntegerField()
    capacity = models.IntegerField()

    def natural_key(self):
        return "{}".format(self.code)

    @property
    def key(self):
        return self.natural_key()

    def __str__(self):
        return self.natural_key()

    class Meta:
        db_table = "room"
