# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Postcode.area'
        db.alter_column('django_ukgeo_postcode', 'area', self.gf('django.db.models.fields.CharField')(max_length=3))


    def backwards(self, orm):
        
        # Changing field 'Postcode.area'
        db.alter_column('django_ukgeo_postcode', 'area', self.gf('django.db.models.fields.CharField')(max_length=2))


    models = {
        'django_ukgeo.postcode': {
            'Meta': {'object_name': 'Postcode'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sector': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        'django_ukgeo.postcodelocation': {
            'Meta': {'object_name': 'PostcodeLocation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.IntegerField', [], {}),
            'lng': ('django.db.models.fields.IntegerField', [], {}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'postcode': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'location'", 'unique': 'True', 'to': "orm['django_ukgeo.Postcode']"})
        },
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
