from __future__ import unicode_literals

from django.test import TestCase
from django import forms
from jstree import widgets
from django.template import Template


class JsTreeWidgetTestCase(TestCase):
    def get_form(self):
        class MyForm(forms.Form):
            my_field = forms.CharField(label="My Field", widget=widgets.JsTreeWidget(url="/test/url/"))

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
            {'form': self.form, }
        )

    def test_field_ispresent(self):
        self.assertIn('id="id_my_field"', self.form_rendering)

    def test_tree_field_ispresent(self):
        self.assertIn('id="my_field-tree"', self.form_rendering)

    def test_css_ispresent(self):
        for css in JsTreeWidgetTestCase._Media.css['all']:
            self.assertIn(css, self.form_rendering)

    def test_js_ispresent(self):
        for js in JsTreeWidgetTestCase._Media.js:
            self.assertIn(js, self.form_rendering)
