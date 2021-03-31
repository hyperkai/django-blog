from storages.backends.s3boto3 import S3Boto3Storage

StaticRootS3Boto3Storage = lambda: S3Boto3Storage(location='static')
MediaRootS3Boto3Storage  = lambda: S3Boto3Storage(location='media')


#class StaticRootS3Boto3Storage(S3Boto3Storage):
#    location = 'static'


#class MediaRootS3Boto3Storage(S3Boto3Storage):
#    location = 'media'

#class MediaRootS3Boto3Storage(S3Boto3Storage):
#    location = 'media'
#    file_overwrite = False