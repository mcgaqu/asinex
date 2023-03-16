from importlib import import_module
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import  gettext_lazy as _
from apps_admin.main1.models.modelbase import ModelBase


class Wsite(ModelBase):
    repository = models.CharField(max_length=250, null=True, blank=True)

    class Meta(ModelBase.Meta):
        verbose_name="Wsite"
        verbose_name_plural="Wsites"
        unique_together=(('alias', 'repository'))

    def __str__(self):
        return "%s" % self.alias

    def load_inidata(self):
        get_INIDATA = getattr(
            import_module('%s.datainit' % settings.WSITE_NAME),
            'get_INIDATA')
        data = get_INIDATA()
        #--------------------------
        count = 0
        for data_row in data:
            count +=1
            alias = data_row[1]
            grade = data_row[0]
            try:
                obj = Dataload.objects.get(wsite=self, alias=alias, grade=grade)
                if obj.locked or not obj.replace:
                    continue
            except Dataload.DoesNotExist:
                obj = Dataload(wsite=self, name=data_row[2],alias=alias, grade=grade)
                for campo in data_row[3].keys():
                    setattr(obj, campo, data_row[3][campo])
            obj.sort = "%02d" % count
            obj.mark='S'
            obj.datet = timezone.now()
            obj.save()
        return


class Dataload(ModelBase):
    wsite = models.ForeignKey(Wsite,  on_delete=models.CASCADE,
                                null=True, blank=True)

    class Meta(ModelBase.Meta):
        verbose_name= _("Dataload")
        verbose_name_plural= _("Dataloads")
        unique_together= (('wsite','alias','sort'),)
        ordering = ['sort']

    def __str__(self):
        return "%s" % self.alias


    def run(self):
        my_function = getattr(import_module('%s' % self.grade), self.alias)
        my_function()
        # kwargs = {}
        # my_function(**kwargs)
        return


