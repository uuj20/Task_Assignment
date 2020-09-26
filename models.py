from django.db import models

class UploadPdf(models.Model): #model for upload and download
    resumes = models.FileField(upload_to='upload/', blank=True, null=True)


