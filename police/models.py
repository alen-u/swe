from django.db import models

# Create your models here.
from django.contrib.auth.models import User


def image_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_images/%Y/%m/%d/', filename)

def video_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_videos/%Y/%m/%d/', filename)

def doc_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_docs/%Y/%m/%d/', filename)

def audio_upload_location(instance,filename):
    return '%s/%s/%s' % (instance.case.id, 'evidence_audios/%Y/%m/%d/', filename)


designation_choice = (
    ('DGP', 'Director General of Police'),
    ('ADGP', 'Addl. Director General of Police'),
    ('IGP', 'Inspector General of Police'),
    ('DIGP', 'Deputy Inspector General of Police'),
    ('SPDCP', 'Superintendent of police Deputy Commissioner of Police(Selection Grade)'),
    ('SPDCPJ', 'Superintendent of police Deputy Commissioner of Police(Junior Management Grade)'),
    ('ASPADCP', 'Addl. Superintendent of police Addl.Deputy Commissioner of Police'),
    ('ASP', 'Assistant Superintendent of Police'),
    ('INSP', 'Inspector of Police'),
    ('SUB_INSP', 'Sub Inspector of Police.'),
    ('HVLDRM', 'Asst. Sub. Inspector/Havildar Major'),
    ('HVLDR', 'Havildar.'),
    ('LN', 'Lance Naik.'),
    ('CONS', 'Constable.'),
)


class Police(User):
    police_id = models.CharField(max_length=20)
    designation = models.CharField(max_length=10, choices=designation_choice, null=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='image/police')

    class Meta:
        verbose_name = 'Officer'

    def __str__(self):
        return self.username



class Criminal(models.Model):
    name = models.CharField(max_length=255, blank=False)
    father_name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    birth_mark_desc=models.TextField()
    height=models.CharField(max_length=255)
    complexion=models.CharField(max_length=255)
    eyes=models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/criminal')
    def __str__(self):
        return self.name
