# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-08 00:03
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('description', models.TextField(default='')),
                ('url', models.TextField(default='')),
                ('original_pk', models.IntegerField()),
                ('deleter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleter', to=settings.AUTH_USER_MODEL)),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_uploader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DVAPQL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_type', models.CharField(choices=[('S', 'Schedule'), ('V', 'Process'), ('Q', 'Query')], default='Q', max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('script', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('results_metadata', models.TextField(default='')),
                ('results_available', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submitter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_index', models.IntegerField()),
                ('name', models.CharField(max_length=200, null=True)),
                ('subdir', models.TextField(default='')),
                ('h', models.IntegerField(default=0)),
                ('w', models.IntegerField(default=0)),
                ('t', models.FloatField(null=True)),
                ('keyframe', models.BooleanField(default=False)),
                ('segment_index', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FrameLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_index', models.IntegerField(default=-1)),
                ('segment_index', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndexEntries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features_file_name', models.CharField(max_length=100)),
                ('entries_file_name', models.CharField(max_length=100)),
                ('algorithm', models.CharField(max_length=100)),
                ('indexer_shasum', models.CharField(max_length=40)),
                ('approximator_shasum', models.CharField(max_length=40, null=True)),
                ('detection_name', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('approximate', models.BooleanField(default=False)),
                ('contains_frames', models.BooleanField(default=False)),
                ('contains_detections', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='IngestEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingest_index', models.IntegerField()),
                ('ingest_filename', models.CharField(max_length=500)),
                ('start_segment_index', models.IntegerField(null=True)),
                ('start_frame_index', models.IntegerField(null=True)),
                ('segments', models.IntegerField(null=True)),
                ('frames', models.IntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('set', models.CharField(default='', max_length=200)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='ManagementAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_task', models.CharField(default='', max_length=500)),
                ('op', models.CharField(default='', max_length=500)),
                ('host', models.CharField(default='', max_length=500)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('ping_index', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QueryRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_type', models.CharField(choices=[('A', 'Annotation'), ('D', 'Detection'), ('P', 'Polygon'), ('S', 'Segmentation'), ('T', 'Transform')], db_index=True, max_length=1)),
                ('text', models.TextField(default='')),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('full_frame', models.BooleanField(default=False)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('h', models.IntegerField(default=0)),
                ('w', models.IntegerField(default=0)),
                ('polygon_points', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('object_name', models.CharField(max_length=100)),
                ('confidence', models.FloatField(default=0.0)),
                ('png', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QueryRegionIndexVector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vector', models.BinaryField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='QueryRegionResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('algorithm', models.CharField(max_length=100)),
                ('distance', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='QueryResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('algorithm', models.CharField(max_length=100)),
                ('distance', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_type', models.CharField(choices=[('A', 'Annotation'), ('D', 'Detection'), ('P', 'Polygon'), ('S', 'Segmentation'), ('T', 'Transform')], db_index=True, max_length=1)),
                ('frame_index', models.IntegerField(default=-1)),
                ('segment_index', models.IntegerField(default=-1, null=True)),
                ('text', models.TextField(default='')),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('full_frame', models.BooleanField(default=False)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
                ('h', models.IntegerField(default=0)),
                ('w', models.IntegerField(default=0)),
                ('polygon_points', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('object_name', models.CharField(max_length=100)),
                ('confidence', models.FloatField(default=0.0)),
                ('materialized', models.BooleanField(default=False)),
                ('png', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RegionLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_index', models.IntegerField(default=-1)),
                ('segment_index', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Retriever',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algorithm', models.CharField(choices=[('L', 'LOPQ'), ('E', 'Exact')], db_index=True, default='E', max_length=1)),
                ('name', models.CharField(default='', max_length=200)),
                ('indexer_shasum', models.CharField(max_length=40, null=True)),
                ('approximator_shasum', models.CharField(max_length=40, null=True)),
                ('source_filters', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment_index', models.IntegerField()),
                ('start_time', models.FloatField(default=0.0)),
                ('end_time', models.FloatField(default=0.0)),
                ('metadata', models.TextField(default='{}')),
                ('frame_count', models.IntegerField(default=0)),
                ('start_index', models.IntegerField(default=0)),
                ('end_frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='segment_end', to='dvaapp.Frame')),
            ],
        ),
        migrations.CreateModel(
            name='SegmentLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment_index', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='SystemState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('tasks', models.IntegerField(default=0)),
                ('pending_tasks', models.IntegerField(default=0)),
                ('completed_tasks', models.IntegerField(default=0)),
                ('processes', models.IntegerField(default=0)),
                ('pending_processes', models.IntegerField(default=0)),
                ('completed_processes', models.IntegerField(default=0)),
                ('queues', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('hosts', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('errored', models.BooleanField(default=False)),
                ('error_message', models.TextField(default='')),
                ('operation', models.CharField(default='', max_length=100)),
                ('queue', models.CharField(default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('start_ts', models.DateTimeField(null=True, verbose_name='date started')),
                ('duration', models.FloatField(default=-1)),
                ('arguments', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('task_id', models.TextField(null=True)),
                ('imported', models.BooleanField(default=False)),
                ('task_group_id', models.IntegerField(default=-1)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
                ('parent_process', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.DVAPQL')),
            ],
        ),
        migrations.CreateModel(
            name='TrainedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detector_type', models.CharField(choices=[('T', 'Tensorflow'), ('Y', 'YOLO V2')], db_index=True, max_length=1, null=True)),
                ('mode', models.CharField(choices=[('T', 'Tensorflow'), ('C', 'Caffe'), ('P', 'Pytorch'), ('O', 'OpenCV'), ('M', 'MXNet')], db_index=True, default='T', max_length=1)),
                ('model_type', models.CharField(choices=[('P', 'Approximator'), ('I', 'Indexer'), ('D', 'Detector'), ('A', 'Analyzer'), ('S', 'Segmenter')], db_index=True, default='I', max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('algorithm', models.CharField(default='', max_length=100)),
                ('shasum', models.CharField(max_length=40, null=True, unique=True)),
                ('model_filename', models.CharField(default='', max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('arguments', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('trained', models.BooleanField(default=False)),
                ('url', models.CharField(default='', max_length=200)),
                ('files', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('produces_labels', models.BooleanField(default=False)),
                ('produces_json', models.BooleanField(default=False)),
                ('produces_text', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TrainedModel')),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_task_type', models.CharField(choices=[('D', 'Detection'), ('I', 'Indexing'), ('C', 'Classication')], db_index=True, default='D', max_length=1)),
                ('instance_type', models.CharField(choices=[('I', 'images'), ('V', 'videos')], db_index=True, default='I', max_length=1)),
                ('count', models.IntegerField(null=True)),
                ('name', models.CharField(default='', max_length=500)),
                ('built', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
            ],
        ),
        migrations.CreateModel(
            name='Tube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_level', models.BooleanField(default=False)),
                ('start_frame_index', models.IntegerField()),
                ('end_frame_index', models.IntegerField()),
                ('text', models.TextField(default='')),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('end_frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_frame', to='dvaapp.Frame')),
                ('end_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_region', to='dvaapp.Region')),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
                ('start_frame', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_frame', to='dvaapp.Frame')),
                ('start_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_region', to='dvaapp.Region')),
            ],
        ),
        migrations.CreateModel(
            name='TubeLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Label')),
                ('tube', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Tube')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=500)),
                ('length_in_seconds', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('width', models.IntegerField(default=0)),
                ('metadata', models.TextField(default='')),
                ('frames', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('description', models.TextField(default='')),
                ('uploaded', models.BooleanField(default=False)),
                ('dataset', models.BooleanField(default=False)),
                ('segments', models.IntegerField(default=0)),
                ('url', models.TextField(default='')),
                ('youtube_video', models.BooleanField(default=False)),
                ('parent_process', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.DVAPQL')),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VideoLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Label')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queue_name', models.CharField(default='', max_length=500)),
                ('host', models.CharField(default='', max_length=500)),
                ('pid', models.IntegerField()),
                ('alive', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.AddField(
            model_name='tubelabel',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='tube',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='tevent',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='tevent',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Worker'),
        ),
        migrations.AddField(
            model_name='segmentlabel',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='segmentlabel',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Label'),
        ),
        migrations.AddField(
            model_name='segmentlabel',
            name='segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Segment'),
        ),
        migrations.AddField(
            model_name='segmentlabel',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='segment',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='segment',
            name='start_frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='segment_start', to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='segment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='regionlabel',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='regionlabel',
            name='frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='regionlabel',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Label'),
        ),
        migrations.AddField(
            model_name='regionlabel',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Region'),
        ),
        migrations.AddField(
            model_name='regionlabel',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='region',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='region',
            name='frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='region',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='region',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='queryresults',
            name='detection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Region'),
        ),
        migrations.AddField(
            model_name='queryresults',
            name='frame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='queryresults',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.DVAPQL'),
        ),
        migrations.AddField(
            model_name='queryresults',
            name='retrieval_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='queryresults',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='queryregionresults',
            name='detection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Region'),
        ),
        migrations.AddField(
            model_name='queryregionresults',
            name='frame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='queryregionresults',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.DVAPQL'),
        ),
        migrations.AddField(
            model_name='queryregionresults',
            name='query_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.QueryRegion'),
        ),
        migrations.AddField(
            model_name='queryregionresults',
            name='retrieval_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='queryregionresults',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='queryregionindexvector',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='queryregionindexvector',
            name='query_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.QueryRegion'),
        ),
        migrations.AddField(
            model_name='queryregion',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='queryregion',
            name='query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.DVAPQL'),
        ),
        migrations.AlterUniqueTogether(
            name='label',
            unique_together=set([('name', 'set')]),
        ),
        migrations.AddField(
            model_name='ingestentry',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='indexentries',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='indexentries',
            name='indexer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TrainedModel'),
        ),
        migrations.AddField(
            model_name='indexentries',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='framelabel',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='framelabel',
            name='frame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Frame'),
        ),
        migrations.AddField(
            model_name='framelabel',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Label'),
        ),
        migrations.AddField(
            model_name='framelabel',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AddField(
            model_name='frame',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.TEvent'),
        ),
        migrations.AddField(
            model_name='frame',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Video'),
        ),
        migrations.AlterUniqueTogether(
            name='segment',
            unique_together=set([('video', 'segment_index')]),
        ),
        migrations.AlterUniqueTogether(
            name='ingestentry',
            unique_together=set([('video', 'ingest_filename', 'ingest_index')]),
        ),
        migrations.AlterUniqueTogether(
            name='indexentries',
            unique_together=set([('video', 'entries_file_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='frame',
            unique_together=set([('video', 'frame_index')]),
        ),
    ]
