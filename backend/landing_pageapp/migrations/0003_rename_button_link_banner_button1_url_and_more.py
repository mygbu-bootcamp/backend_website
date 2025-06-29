# Generated by Django 5.2.2 on 2025-06-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_pageapp', '0002_campus_gallery_campus_life_companies_hiring_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='button_link',
            new_name='button1_url',
        ),
        migrations.RemoveField(
            model_name='about',
            name='content',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='campus_life',
            name='content',
        ),
        migrations.RemoveField(
            model_name='companies_hiring',
            name='value',
        ),
        migrations.RemoveField(
            model_name='glancestat',
            name='value',
        ),
        migrations.RemoveField(
            model_name='quickaccess',
            name='description',
        ),
        migrations.AddField(
            model_name='about',
            name='button1_text',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='button1_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='button2_text',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='button1_text',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='button2_text',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='button2_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='campus_gallery',
            name='button1_text',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campus_gallery',
            name='button1_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campus_life',
            name='card_content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='campus_life',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='campus_life',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companies_hiring',
            name='Companies_hiring',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companies_hiring',
            name='alumini_count',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companies_hiring',
            name='placement_rate',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='excellence_in_education',
            name='category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='glancestat',
            name='acres_camus',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='glancestat',
            name='background_color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='glancestat',
            name='faculty_member',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='glancestat',
            name='placement_rate',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='glancestat',
            name='programs_count',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='glancestat',
            name='student_count',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='leadership',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quickaccess',
            name='card_description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='quickaccess',
            name='card_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualexperience',
            name='background_color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='virtualexperience',
            name='button1_text',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualexperience',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
