from django.db import models

# Create your models here.
class First_Name(models.Model):
    first_name = models.CharField(max_length=100)

class People(models.Model):
    FName = models.CharField(max_length=100, default='')
    Group = models.ManyToManyField("self", through='Grouping', symmetrical=False, related_name='grouped', default='')
    Connections = models.CharField(max_length=1, default='', editable=False)

def __str__(self):
    return self.FName

GROUPING_ONE = 1
GROUPING_TWO = 2
CONNECTIONS = (
(GROUPING_ONE, 'CONNECTED'),
(GROUPING_TWO, 'UNCONNECTED'),
)

class Grouping(models.Model):
    From_Group=models.ForeignKey(People, on_delete=models.CASCADE, related_name='fromgroup', default='')
    To_Group = models.ForeignKey(People, on_delete=models.CASCADE, related_name='togroup', default='')
    Connections = models.IntegerField(choices=CONNECTIONS)



def add_grouping(self, People, Connections):
    Grouping, created = Grouping.objects.get_or_create(
        fromgroup=self,
        togroup=People,
        connection=Connections)
    return Grouping

def remove_grouping(self, People, Connections, symm=True):
    Grouping.objects.filter(
        fromgroup=self,
        togroup=People,
        connection=Connections).delete()
    
def get_grouping(self, Connections):
    return self.Grouping.filter(
        fromgroup__Connections=Connections,
        togroup__fromPeople=self)

def get_grouping(self, Connections):
    return self.Grouping.filter(
        togroup__Connections=Connections,
        togroup__fromPeople=self)

def get_related_to(self, Connections):
    return self.grouped.filter(
        fromgroup__Connections=Connections,
        fromgroup__togroup=self)

def get_grouping(self):
    return self.get_grouping(GROUPING_ONE)

def get_grouping(self):
    return self.get_related_to(GROUPING_ONE)

def get_grouped(self):
    return self.Grouping.filter(
        togroup__status=GROUPING_ONE,
        togroup__fromgroup=self,
        fromgroup__Connection=GROUPING_ONE,
        fromgroup__togroup=self)
