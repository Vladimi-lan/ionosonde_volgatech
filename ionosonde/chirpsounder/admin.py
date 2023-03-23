from django.contrib import admin

from users.models import CustomUser
from .models import (ConfigSettings, Swtracks, ScheduleSettings)


admin.site.register(ConfigSettings)
admin.site.register(Swtracks)
admin.site.register(ScheduleSettings)
admin.site.register(CustomUser)
