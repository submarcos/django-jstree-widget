from __future__ import unicode_literals

from django.http.request import HttpRequest
from django.template.context import RequestContext
from django.test import TestCase
from django import forms
from jstree import widgets
from django.template import Template


class JsTreeWidgetTestCase(TestCase):
    def get_widget(self):
        return widgets.JsTreeWidget(url="/test/url/")

    def get_form(self):
        class MyForm(forms.Form):
            my_field = forms.CharField(label="My Field", widget=self.get_widget())

        return MyForm()

    def setUp(self):
        self.form = self.get_form()
        self.template = Template(
            """
            {{ form.media }}
            <form method="POST">
                {% for field in form %}
                    {{ field.label }}: {{ field }}
                {% endfor %}
            </form>
            """
        )
        self.form_rendering = self.template.render(
            RequestContext(request=HttpRequest(), dict_={'form': self.form, })
        )

    def test_field_ispresent(self):
        self.assertIn('id="id_my_field"', self.form_rendering)

    def test_tree_field_ispresent(self):
        self.assertIn('id="my_field-tree"', self.form_rendering)

    def test_css_ispresent(self):
        widget = self.get_widget()
        self.assertIn("{}".format(widget.media['css']), self.form_rendering)

    def test_js_ispresent(self):
        widget = self.get_widget()
        self.assertIn("{}".format(widget.media['js']), self.form_rendering)

    def test_custom_js_ispresent(self):
        self.assertIn('<script type="text/javascript">', self.form_rendering)
