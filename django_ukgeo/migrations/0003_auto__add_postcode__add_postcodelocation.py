# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Postcode'
        db.create_table('django_ukgeo_postcode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('sector', self.gf('django.db.models.fields.IntegerField')()),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('django_ukgeo', ['Postcode'])

        # Adding model 'PostcodeLocation'
        db.create_table('django_ukgeo_postcodelocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postcode', self.gf('django.db.models.fields.related.OneToOneField')(related_name='location', unique=True, to=orm['django_ukgeo.Postcode'])),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lat', self.gf('django.db.models.fields.IntegerField')()),
            ('lng', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('django_ukgeo', ['PostcodeLocation'])


    def backwards(self, orm):
        
        # Deleting model 'Postcode'
        db.delete_table('django_ukgeo_postcode')

        # Deleting model 'PostcodeLocation'
        db.delete_table('django_ukgeo_postcodelocation')


    models = {
        'django_ukgeo.postcode': {
            'Meta': {'object_name': 'Postcode'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sector': ('django.db.models.fields.IntegerField', [], {}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '2'})
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
