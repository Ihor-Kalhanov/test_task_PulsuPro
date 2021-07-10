from flask import redirect, url_for, request

from flask_admin.contrib.sqla import ModelView

from flask_admin import AdminIndexView
from flask_security import current_user

class AdminSecurityMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url ))

class AdminSecurityView(AdminSecurityMixin, ModelView):
   pass

class HomeSecurityView(AdminSecurityMixin,AdminIndexView):
    pass
