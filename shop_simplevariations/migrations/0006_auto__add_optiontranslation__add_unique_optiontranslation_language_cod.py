# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OptionTranslation'
        db.create_table(u'shop_simplevariations_option_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['shop_simplevariations.Option'])),
        ))
        db.send_create_signal(u'shop_simplevariations', ['OptionTranslation'])

        # Adding unique constraint on 'OptionTranslation', fields ['language_code', 'master']
        db.create_unique(u'shop_simplevariations_option_translation', ['language_code', 'master_id'])

        # Adding model 'OptionGroupTranslation'
        db.create_table(u'shop_simplevariations_optiongroup_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['shop_simplevariations.OptionGroup'])),
        ))
        db.send_create_signal(u'shop_simplevariations', ['OptionGroupTranslation'])

        # Adding unique constraint on 'OptionGroupTranslation', fields ['language_code', 'master']
        db.create_unique(u'shop_simplevariations_optiongroup_translation', ['language_code', 'master_id'])

        # Adding model 'TextOptionTranslation'
        db.create_table(u'shop_simplevariations_textoption_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['shop_simplevariations.TextOption'])),
        ))
        db.send_create_signal(u'shop_simplevariations', ['TextOptionTranslation'])

        # Adding unique constraint on 'TextOptionTranslation', fields ['language_code', 'master']
        db.create_unique(u'shop_simplevariations_textoption_translation', ['language_code', 'master_id'])

        # Deleting field 'Option.name'
        db.delete_column(u'shop_simplevariations_option', 'name')


        # Changing field 'Option.price'
        db.alter_column(u'shop_simplevariations_option', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=2))
        # Deleting field 'TextOption.description'
        db.delete_column(u'shop_simplevariations_textoption', 'description')

        # Deleting field 'TextOption.name'
        db.delete_column(u'shop_simplevariations_textoption', 'name')


        # Changing field 'TextOption.price'
        db.alter_column(u'shop_simplevariations_textoption', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=2))
        # Deleting field 'OptionGroup.description'
        db.delete_column(u'shop_simplevariations_optiongroup', 'description')

        # Deleting field 'OptionGroup.name'
        db.delete_column(u'shop_simplevariations_optiongroup', 'name')


    def backwards(self, orm):
        # Removing unique constraint on 'TextOptionTranslation', fields ['language_code', 'master']
        db.delete_unique(u'shop_simplevariations_textoption_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'OptionGroupTranslation', fields ['language_code', 'master']
        db.delete_unique(u'shop_simplevariations_optiongroup_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'OptionTranslation', fields ['language_code', 'master']
        db.delete_unique(u'shop_simplevariations_option_translation', ['language_code', 'master_id'])

        # Deleting model 'OptionTranslation'
        db.delete_table(u'shop_simplevariations_option_translation')

        # Deleting model 'OptionGroupTranslation'
        db.delete_table(u'shop_simplevariations_optiongroup_translation')

        # Deleting model 'TextOptionTranslation'
        db.delete_table(u'shop_simplevariations_textoption_translation')


        # User chose to not deal with backwards NULL issues for 'Option.name'
        raise RuntimeError("Cannot reverse this migration. 'Option.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Option.name'
        db.add_column(u'shop_simplevariations_option', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # Changing field 'Option.price'
        db.alter_column(u'shop_simplevariations_option', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2))
        # Adding field 'TextOption.description'
        db.add_column(u'shop_simplevariations_textoption', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'TextOption.name'
        raise RuntimeError("Cannot reverse this migration. 'TextOption.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'TextOption.name'
        db.add_column(u'shop_simplevariations_textoption', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


        # Changing field 'TextOption.price'
        db.alter_column(u'shop_simplevariations_textoption', 'price', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2))
        # Adding field 'OptionGroup.description'
        db.add_column(u'shop_simplevariations_optiongroup', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'OptionGroup.name'
        raise RuntimeError("Cannot reverse this migration. 'OptionGroup.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'OptionGroup.name'
        db.add_column(u'shop_simplevariations_optiongroup', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=255),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shop.cart': {
            'Meta': {'object_name': 'Cart'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'shop.cartitem': {
            'Meta': {'object_name': 'CartItem'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['shop.Cart']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        'shop.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_shop.product_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        },
        u'shop_simplevariations.cartitemoption': {
            'Meta': {'object_name': 'CartItemOption'},
            'cartitem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.CartItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop_simplevariations.Option']"})
        },
        u'shop_simplevariations.cartitemtextoption': {
            'Meta': {'object_name': 'CartItemTextOption'},
            'cartitem': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'text_option'", 'to': "orm['shop.CartItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text_option': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop_simplevariations.TextOption']"})
        },
        u'shop_simplevariations.option': {
            'Meta': {'object_name': 'Option'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shop_simplevariations.OptionGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'})
        },
        u'shop_simplevariations.optiongroup': {
            'Meta': {'object_name': 'OptionGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'option_groups'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['shop.Product']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'shop_simplevariations.optiongrouptranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'OptionGroupTranslation', 'db_table': "u'shop_simplevariations_optiongroup_translation'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['shop_simplevariations.OptionGroup']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'shop_simplevariations.optiontranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'OptionTranslation', 'db_table': "u'shop_simplevariations_option_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['shop_simplevariations.Option']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'shop_simplevariations.textoption': {
            'Meta': {'object_name': 'TextOption'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'text_options'", 'symmetrical': 'False', 'to': "orm['shop.Product']"})
        },
        u'shop_simplevariations.textoptiontranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'TextOptionTranslation', 'db_table': "u'shop_simplevariations_textoption_translation'"},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['shop_simplevariations.TextOption']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['shop_simplevariations']