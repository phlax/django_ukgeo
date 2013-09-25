# encoding: utf-8
import datetime
import os
 
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UKCity'
        db.create_table('django_ukgeo_ukcity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='label', overwrite=False, db_index=True)),
        ))
        db.send_create_signal('django_ukgeo', ['UKCity'])

        # Adding model 'UKTown'
        db.create_table('django_ukgeo_uktown', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='label', overwrite=False, db_index=True)),
        ))
        db.send_create_signal('django_ukgeo', ['UKTown'])

        # Adding model 'UKCounty'
        db.create_table('django_ukgeo_ukcounty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='label', overwrite=False, db_index=True)),
        ))
        db.send_create_signal('django_ukgeo', ['UKCounty'])


    def backwards(self, orm):
        
        # Deleting model 'UKCity'
        db.delete_table('django_ukgeo_ukcity')

        # Deleting model 'UKTown'
        db.delete_table('django_ukgeo_uktown')

        # Deleting model 'UKCounty'
        db.delete_table('django_ukgeo_ukcounty')


    models = {
        'django_ukgeo.ukcity': {
            'Meta': {'object_name': 'UKCity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'label'", 'overwrite': 'False', 'db_index': 'True'})
        },
        'django_ukgeo.ukcounty': {
            'Meta': {'object_name': 'UKCounty'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'label'", 'overwrite': 'False', 'db_index': 'True'})
        },
        'django_ukgeo.uktown': {
            'Meta': {'object_name': 'UKTown'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'label'", 'overwrite': 'False', 'db_index': 'True'})
        }
    }

    complete_apps = ['django_ukgeo']
