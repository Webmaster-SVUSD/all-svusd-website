from cms.models.pluginmodel import CMSPlugin

from django.db import models
# from filer.fields.image import FilerImageField

class QuickLinkCardInfo(CMSPlugin):
    image = models.ImageField(null = True, upload_to='quick_link_images')
    title = models.CharField(max_length=50, default='Title')
    text_body = models.CharField(max_length=500, default='text body')
    
class EventCardInfo(CMSPlugin):
    image = models.ImageField(null = True, upload_to='quick_link_images', blank=True)
    title = models. CharField (max_length=500, default='Title')
    date = models.CharField (max_length=500, default="")
    time = models.CharField(max_length=500, default='')
    link1_button_info = models.CharField (max_length=500, default="", blank=True)
    link_1 = models.TextField(max_length=5000, default="", blank=True)
    link2_button_info = models.CharField(max_length=500, default="", blank=True)
    link_2 = models.TextField(max_length=5000, default="", blank=True)
    link3_button_info = models.CharField(max_length=500, default="", blank=True)
    link_3 = models.TextField(max_length=5000, default="", blank=True)
    link4_button_info = models.CharField (max_length=500, default="", blank=True)
    link_4 = models.TextField(max_length=5000, default="", blank=True)
    text_body = models.TextField (max_length=5000, default='Text Body')