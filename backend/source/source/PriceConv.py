from django.apps import apps


class Conversions:
    pass


class FieldSelection:
    
    def __init__(self, model):
        self.model = model.__class__.__name__

        c = self.model.objects.filter()
