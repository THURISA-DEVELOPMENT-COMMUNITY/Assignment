from django.db import models
from django.contrib.auth.models import User


class CollaboratorModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


class FileModel(models.Model):

    FILE_TYPE = [
        ('IMG', 'Images'),
        ('MP4', 'Videos'),
        ('DOC', 'Documents'),
    ]

    file = models.FileField()
    file_type = models.CharField(
        max_length=10, choices=FILE_TYPE, default='IMG')
    text = models.TextField(null=True, blank=True)
    collaborators = models.ManyToManyField(CollaboratorModel)
    time_stamp = models.DateTimeField(auto_created=True)


# Create your models here.


# class DocumentImage(models.Model):
#     primary_img = models.ImageField(null=False)
#     img_1 = models.ImageField()
#     img_2 = models.ImageField()
#     img_3 = models.ImageField()
#     img_4 = models.ImageField()


# class Document(models.Model):
#     title = models.CharField(max_length=300)
#     msg = models.TextField()
#     image = models.ForeignKey(DocumentImage, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_created=True)
#     modified_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
