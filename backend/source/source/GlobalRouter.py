class DBRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ('portal', 'users'):
            return 'portal_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ('portal', 'users'):
            return 'portal_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in 'portal' or obj2._meta.app_label in 'portal':
            return True
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in 'portal':
            return db == 'portal_db'
        return None
