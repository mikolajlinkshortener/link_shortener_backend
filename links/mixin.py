from django.db.models.fields import NOT_PROVIDED


class ModelSerializerDefaultsMixin:
    def __init__(self, *args, **kwargs):
        extra_kwargs = {}
        for field in self.Meta.model._meta.fields:
            if field.default != NOT_PROVIDED:
                extra_kwargs[field.name] = {"default": field.default}
        self.Meta.extra_kwargs = extra_kwargs
        super(ModelSerializerDefaultsMixin, self).__init__(*args, **kwargs)
