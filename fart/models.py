import datetime
from uuid import uuid4

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model

FART_SETTINGS = getattr(settings, 'FART', {
    'fast-login': {
        'name': _(u'Fast login'),
        'duration': 60,
        'one-time': True,
    },
    'slow-login': {
        'name': _(u'Slow login'),
        'duration': 60*60*24,
        'one-time': False
    },
    'alwais-login': {
        'name': _(u'Alwais login'),
        'one-time': False,
        'duration': None,
    },
})
FART_TYPE_CHOICES = [ (key, value['name']) for key, value in FART_SETTINGS.iteritems() ]

class FART(models.Model):
    uuid = models.CharField(max_length=50, null=False, blank=False, verbose_name=_('Uuid'))
    type = models.SlugField(max_length=50, choices=FART_TYPE_CHOICES, null=False, blank=False, verbose_name=_('FART type'))
    user = models.ForeignKey(get_user_model(), null=False, blank=False, verbose_name=_('user'))
    session_data = models.TextField(null=True, blank=True, verbose_name=_('Jsoned Session Data'))
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name=_('creation date'))

    def verify(self):
        if not self.type in FART_SETTINGS:
            return False

        duration = FART_SETTINGS.get(self.type).get('duration', None)

        if duration == None:
            return True
        else:
            return (self.created + datetime.timedelta(seconds=duration)) > datetime.datetime.now()

    def is_one_time(self):
        return FART_SETTINGS.get(self.type, {}).get('one-time', False)

    def save(self, *args, **kwargs):
        if self.id and not kwargs.pop('force_modification', False):
            raise Exception('Modification not allowed (you can force it with the force_modification parameter on save)')
        self.uuid = uuid4()
        super(FART, self).save(*args, **kwargs)