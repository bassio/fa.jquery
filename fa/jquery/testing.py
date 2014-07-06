# -*- coding: utf-8 -*-
from formalchemy.ext.zope import FieldSet
from zope import interface, schema
from fa.jquery.utils import url
from fa.jquery.renderers import *

FieldSet.default_renderers.update(default_renderers)

class ITab1(interface.Interface):
    title = schema.TextLine(title='title')

class ITab2(interface.Interface):
    title = schema.TextLine(title='title')
    description = schema.TextLine(title='description')

class IAccordion(interface.Interface):
    field1 = schema.TextLine(title='field 1')
    field2 = schema.TextLine(title='field 2')

fs1 = FieldSet(ITab1)
obj1 = fs1.gen_model()
fs2 = FieldSet(ITab2)
obj2 = fs2.gen_model()
fs3 = FieldSet(IAccordion)
fs3.configure(include=[fs3.field1])
obj3 = fs3.gen_model()
fs4 = FieldSet(IAccordion)
fs4.configure(include=[fs4.field2])

class ISample(interface.Interface):
    title = schema.TextLine(title='Autocomplete')
    ajax = schema.TextLine(title='Auto complete with an ajax request')
    color = schema.TextLine(title='Color picker')
    rich = schema.Text(title='TinyMCE')
    markdown = schema.Text(title='Markdown editor using Markitup!. Textile and bbcode format are also supported')
    radioset = schema.TextLine(title='Radio Set')
    checkboxset = schema.List(title='Checkbox Set')
    selectable = schema.TextLine(title='Selectable')
    selectables = schema.List(title='Selectables')
    sortable = schema.TextLine(title='Sortable token',
                              description='Save values as a string separate by a semi comma')
    slider = schema.Int(title='Integer as slider')
    date = schema.Date(title='Date')
    datetime = schema.Datetime(title='Datetime')
    resources  = schema.TextLine(title='Plugin with resources')

Form = FieldSet(ISample)
Form.title.set(renderer=AutoCompleteFieldRenderer(['aa', 'bb']))
Form.ajax.set(renderer=AutoCompleteFieldRenderer('/fa.jquery/ajax_values'))
Form.rich.set(renderer=tinymce())
Form.markdown.set(renderer=markdown())
Form.color.set(renderer=ColorPickerFieldRenderer())
Form.slider.set(renderer=SliderFieldRenderer)
Form.radioset.set(renderer=radioset(), options=[l for l in 'abcdef'])
Form.checkboxset.set(renderer=checkboxset(), options=[l for l in 'abcdef'])
Form.selectable.set(renderer=selectable(), options=[l for l in 'abcdef'])
Form.selectables.set(renderer=selectables(), options=[l for l in 'abcdef'])
Form.sortable.set(renderer=SortableTokenTextFieldRenderer())
Form.resources.set(renderer=jQueryFieldRenderer('test_resources',
                                                resources=['/jquery/fa.resource.js','/jquery/fa.resource.css']))

obj = Form.gen_model()
obj.context['sortable'] = 'fisrt;second'
fs = Form.bind(obj)

