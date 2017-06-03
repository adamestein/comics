# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comic'
        db.create_table(u'comic_app_comic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sequence', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, unique=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'comic_app', ['Comic'])


    def backwards(self, orm):
        # Deleting model 'Comic'
        db.delete_table(u'comic_app_comic')


    models = {
        u'comic_app.comic': {
            'Meta': {'object_name': 'Comic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sequence': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['comic_app']