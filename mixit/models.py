# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Answer(models.Model):
    text = models.CharField(max_length=200)
    pic_uri = models.URLField()
    pub_date = models.DateTimeField('date published')

    def save(self, *args, **kw):
        if not self.id:
            self.pub_date = timezone.now()
        return super(Answer, self).save(*args, **kw)

    def __unicode__(self):
        return "%s [%s]" % (self.text, self.pic_uri)
