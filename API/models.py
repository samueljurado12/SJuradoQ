from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=20, blank=False, unique=True)

    def __str__(self):
        return "{}".format(self.tag)


class Project(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images', default='/media/')
    date_added = models.DateField(auto_now_add=True)
    project_tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Link(models.Model):
    GITHUB = 'GH'
    ITCH = 'IO'
    WEB = 'WB'
    LINK_TYPE_CHOICES = (
        (ITCH, 'ITCH.IO'),
        (GITHUB, 'GITHUB'),
        (WEB, 'WEBPAGE')
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='links')
    link = models.CharField(max_length=150)
    link_type = models.CharField(max_length=2, choices=LINK_TYPE_CHOICES, default=GITHUB)

    def __str__(self):
        return self.project.name + ': ' + self.link_type


class Screenshot(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='screenshots_reference')
    image = models.ImageField(upload_to='project_images/screenshots', default='/media/')

    def __str__(self):
        return self.project.name + '_' + self.id.__str__()
