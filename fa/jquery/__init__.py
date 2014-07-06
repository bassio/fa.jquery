from fa.jquery.utils import TemplateEngine
from fa.jquery.utils import HTML
from fa.jquery.utils import Color
from fa.jquery.utils import Slider
from fa.jquery.utils import url

from fa.jquery.renderers import plugin
from fa.jquery.renderers import autocomplete
from fa.jquery.renderers import colorpicker
from fa.jquery.renderers import date
from fa.jquery.renderers import datetime
from fa.jquery.renderers import slider
from fa.jquery.renderers import selectable
from fa.jquery.renderers import selectables
from fa.jquery.renderers import radioset
from fa.jquery.renderers import checkboxset
from fa.jquery.renderers import tinymce
from fa.jquery.renderers import markdown
from fa.jquery.renderers import textile
from fa.jquery.renderers import bbcode
from fa.jquery.renderers import default_renderers

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
