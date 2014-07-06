from fa.jquery.utils import TemplateEngine
from fa.jquery.utils import HTML
from fa.jquery.utils import Color
from fa.jquery.utils import Slider
from fa.jquery.utils import url

from fa.jquery.renderers import plugin
from fa.jquery.renderers import AutoCompleteFieldRenderer as autocomplete
from fa.jquery.renderers import ColorPickerFieldRenderer as colorpicker
from fa.jquery.renderers import DateFieldRenderer as date
from fa.jquery.renderers import DateTimeFieldRenderer as datetime
from fa.jquery.renderers import SliderFieldRenderer as slider
#from fa.jquery.renderers import SelectableFieldRenderer(multiple=False) as selectable
#from fa.jquery.renderers import SelectableFieldRenderer(multiple=True) as selectables
#from fa.jquery.renderers import ButtonSetFieldRenderer(multiple=False) as radioset
#from fa.jquery.renderers import ButtonSetFieldRenderer(multiple=True) as checkboxset
#from fa.jquery.renderers import RichTextFieldRenderer(use='tinymce') as tinymce
#from fa.jquery.renderers import RichTextFieldRenderer(use='markdown') as markdown
#from fa.jquery.renderers import RichTextFieldRenderer(use='textile') as textile
#from fa.jquery.renderers import RichTextFieldRenderer(use='bbcode') as bbcode
#from fa.jquery.renderers import default_renderers

from fa.jquery.forms import Tabs
from fa.jquery.forms import Accordion
from fa.jquery.forms import MultiFieldSet

try:
    from fa.jquery.pylons import relation
    from fa.jquery.pylons import relations
except ImportError:
    pass

try:
    from fa.jquery.pyramid.renderers import relation
    from fa.jquery.pyramid.renderers import relations
except ImportError:
    pass

def includeme(config):
    config.add_translation_dirs('fa.jquery:locale/')
    config.override_asset(
        to_override="pyramid_formalchemy:templates/admin/",
        override_with="fa.jquery:templates/admin/")
    config.override_asset(
        to_override="pyramid_formalchemy:templates/forms/",
        override_with="fa.jquery:templates/forms/")

    config.add_route('markup_parser', '/markup_parser.html')
    config.add_view('fa.jquery.pyramid.markup_parser', route_name='markup_parser')
    config.scan("fa.jquery.pyramid")
