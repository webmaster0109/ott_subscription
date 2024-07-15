from django.contrib import admin
from ott_schemas.models.user_role import UserRole
from ott_schemas.models.users import User
from ott_schemas.models.roles import Role
from ott_schemas.models.plans import Plan
from ott_schemas.models.content import Content
from ott_schemas.models.settings import Setting
from ott_schemas.models.notifications import Notification
from ott_schemas.models.subscriptions import Subscription
from ott_schemas.models.payments import Payment
from ott_schemas.models.user_contents import UserContent

admin.site.register(UserRole)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Plan)
admin.site.register(Content)
admin.site.register(Setting)
admin.site.register(Notification)
admin.site.register(Subscription)
admin.site.register(Payment)
admin.site.register(UserContent)
