from os.path import basename

from django.conf import settings
from django.db import models
from django.db.models import Max
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


def next_sequence_number():
    max_sequence = Comic.objects.all().aggregate(Max('sequence'))['sequence__max']
    return 1 if max_sequence is None else max_sequence + 1


class Comic(models.Model):
    name = models.CharField(max_length=50)
    sequence = models.PositiveIntegerField(default=next_sequence_number, unique=True)
    image = models.ImageField(upload_to='.')    # Stores images in MEDIA_ROOT
    slug = models.SlugField()

    class Meta:
        ordering = ('sequence', )

    def __unicode__(self):
        return u'{:04d}: {}'.format(self.sequence, self.name)


@receiver(pre_delete, sender=Comic)
def comic_delete(sender, instance, **kwargs):
    # Pass False so ImageField doesn't save the model
    instance.image.delete(False)
