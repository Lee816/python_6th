from typing import Any
from django.views.generic import TemplateView

from django.apps import apps


class Index(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["app_list"] = ["polls", "books"]
        dictVerbose = {}
        for app in apps.get_app_configs():  # setting에 app을 추가한 순서대로 나옴
            if "site-packages" not in app.path:
                dictVerbose[app.label] = app.verbose_name
        context["verbose_dict"] = dictVerbose
        return context
