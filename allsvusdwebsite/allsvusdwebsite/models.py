from cms.models.pluginmodel import CMSPlugin

from django.db import models
# from filer.fields.image import FilerImageField

class QuickLinkCardInfo(CMSPlugin):
    image = models.ImageField(null = True, upload_to='quick_link_images')
    title = models.CharField(max_length=50, default='Title')
    text_body = models.CharField(max_length=500, default='text body')