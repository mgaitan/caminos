from django.db import models
from django import forms
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel,
    PageChooserPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from django.db import models
from wagtail.core.models import Orderable


class HomePage(Page):

    content_panels = [
        InlinePanel('slideshow_links', label="Slideshows links"),
    ]


class SlideshowLink(Orderable):
    home_page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='slideshow_links')
    page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.CASCADE,
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    text = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    button_text = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    panels = [
        PageChooserPanel('page'),
        ImageChooserPanel('image'),
        FieldPanel('text', widget=forms.Textarea),
        FieldPanel('button_text'),
    ]



class SectionPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]