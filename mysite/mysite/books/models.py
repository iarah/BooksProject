from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name']

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title', 'author']
