registry = dict(version=0)
def bind():
    from cPickle import loads as _loads
    _attrs_4369730256 = _loads('(dp1\nVtype\np2\nVtext/css\np3\ns.')
    _lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
    _re_amp = _loads("cre\n_compile\np1\n(S'&(?!([A-Za-z]+|#[0-9]+);)'\np2\nI0\ntRp3\n.")
    _attrs_4369731408 = _loads('(dp1\n.')
    _init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
    _attrs_4369729936 = _loads('(dp1\nVtype\np2\nVtext/javascript\np3\ns.')
    _attrs_4369727696 = _loads('(dp1\nVstyle\np2\nVdisplay:none;\np3\nsVid\np4\nVmodels\np5\ns.')
    _attrs_4369730832 = _loads('(dp1\n.')
    _attrs_4369729296 = _loads('(dp1\nVid\np2\nVlanguages\np3\ns.')
    _init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
    _attrs_4369730768 = _loads('(dp1\n.')
    _attrs_4369730960 = _loads('(dp1\n.')
    _init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
    _attrs_4369727824 = _loads('(dp1\nVclass\np2\nVbreadcrumb\np3\ns.')
    _marker = _loads("ccopy_reg\n_reconstructor\np1\n(cchameleon.core.i18n\nStringMarker\np2\nc__builtin__\nstr\np3\nS''\ntRp4\n.")
    _attrs_4369728720 = _loads('(dp1\nVclass\np2\nVfooter-actions\np3\ns.')
    _attrs_4369729040 = _loads('(dp1\n.')
    _attrs_4369731536 = _loads('(dp1\nVid\np2\nVcontent\np3\nsVclass\np4\nVui-admin ui-widget\np5\ns.')
    _attrs_4369730000 = _loads('(dp1\nVtype\np2\nVtext/javascript\np3\ns.')
    _attrs_4369728784 = _loads('(dp1\n.')
    _attrs_4369728400 = _loads('(dp1\nVstyle\np2\nVdisplay:none\np3\nsVclass\np4\nVroot_url\np5\ns.')
    _attrs_4369730512 = _loads('(dp1\n.')
    _attrs_4369729808 = _loads('(dp1\nVid\np2\nVheader\np3\nsVclass\np4\nVui-widget-header ui-corner-all\np5\ns.')
    _init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
    _attrs_4369729872 = _loads('(dp1\nVid\np2\nVthemes\np3\ns.')
    _attrs_4369730896 = _loads('(dp1\n.')
    _attrs_4369727952 = _loads('(dp1\n.')
    def render(econtext, rcontext=None):
        macros = econtext.get('macros')
        _translate = econtext.get('_translate')
        _slots = econtext.get('_slots')
        target_language = econtext.get('target_language')
        "%(scope)s['%(out)s'], %(scope)s['%(write)s']"
        (_out, _write, ) = (econtext['_out'], econtext['_write'], )
        '_init_tal()'
        (_attributes, repeat, ) = _init_tal()
        '_init_default()'
        _default = _init_default()
        'None'
        default = None
        'None'
        _domain = None
        attrs = _attrs_4369728784
        _write('<html>\n    ')
        attrs = _attrs_4369731408
        "''"
        _write('<head>\n      ')
        _default.value = default = ''
        'request.model_name'
        _tmp1 = _lookup_attr(econtext['request'], 'model_name')
        if _tmp1:
            pass
            'model_class.plural'
            _content = _lookup_attr(econtext['model_class'], 'plural')
            attrs = _attrs_4369730768
            '_content'
            _write('<title>')
            _tmp1 = _content
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, str, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, str):
                    _tmp = str(_tmp)
                if ('&' in _tmp):
                    if (';' in _tmp):
                        _tmp = _re_amp.sub('&amp;', _tmp)
                    else:
                        _tmp = _tmp.replace('&', '&amp;')
                if ('<' in _tmp):
                    _tmp = _tmp.replace('<', '&lt;')
                if ('>' in _tmp):
                    _tmp = _tmp.replace('>', '&gt;')
                _write(_tmp)
            _write('</title>')
        _write('\n      ')
        _tmp_domain0 = _domain
        "u'fa_jquery'"
        _domain = 'fa_jquery'
        'request.model_name is None'
        _tmp1 = (_lookup_attr(econtext['request'], 'model_name') is None)
        if _tmp1:
            pass
            attrs = _attrs_4369730960
            "u'Models index'"
            _write('<title>')
            _msgid = 'Models index'
            "%(translate)s(' '.join(%(msgid)s.split()), domain=%(domain)s, mapping=None, target_language=%(language)s, default=%(msgid)s)"
            _result = _translate(_lookup_attr(' ', 'join')(_msgid.split()), domain=_domain, mapping=None, target_language=target_language, default=_msgid)
            '_result'
            _tmp1 = _result
            _write((_tmp1 + '</title>'))
        _write('\n      ')
        _domain = _tmp_domain0
        attrs = _attrs_4369730000
        "%(slots)s.get(u'javascript')"
        _write('<script type="text/javascript">\n        jQuery(document).ready(function() {\n          $(\'select#models, select#themes\')\n            .change(function() { window.location.href = $(this).val(); })\n            .selectmenu({\'style\':\'dropdown\', \'menuWidth\':\'20%\', \'width\':\'100%\'});\n        });\n      </script>\n      ')
        _tmp = _slots.get('javascript')
        '%(tmp)s is not None'
        _tmp1 = (_tmp is not None)
        if _tmp1:
            pass
            'isinstance(%(tmp)s, basestring)'
            _tmp2 = isinstance(_tmp, basestring)
            if not _tmp2:
                pass
                econtext.update(dict(rcontext=rcontext, _domain=_domain))
                _tmp(econtext, repeat)
            else:
                pass
                '%(tmp)s'
                _tmp2 = _tmp
                _tmp = _tmp2
                if (_tmp.__class__ not in (str, str, int, float, )):
                    try:
                        _tmp = _tmp.__html__
                    except:
                        _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                    else:
                        _tmp = _tmp()
                        _write(_tmp)
                        _tmp = None
                if (_tmp is not None):
                    if not isinstance(_tmp, str):
                        _tmp = str(_tmp)
                    _write(_tmp)
        else:
            pass
            attrs = _attrs_4369729936
            _write('<script type="text/javascript"></script>')
        _write('\n      ')
        attrs = _attrs_4369730256
        _write('<style type="text/css">\n        label {font-weight:bold;}\n        h1, h3 {padding:0.1 0.3em;}\n        h1 a, h3 a {text-decoration:none;}\n        #header { height: 2em; font-size:1.5em; }\n        #header div { font-size:1.5em; }\n        #header a { font-size:1em; }\n        ul#languages {float:right;}\n        ul#languages li {display: inline;}\n        ul#languages a {text-decoration:none; color: grey;}\n        ul#languages a.lang_active {text-decoration:underline;}\n        div.footer-actions {float:right;width: 300px;}\n        div.breadcrumb {float:right;width:20%;margin-right:20px;}\n        div.breadcrumb a {text-decoration:none;}\n        h1 a.ui-selectmenu {height:1em;}\n        a.ui-state-default {padding:0.1em 0.3em;}\n        a.fm-button {padding:0.4em 0.5em;}\n        a.fm-button-icon-left {padding-left:1.9em;}\n      </style>\n    </head>\n    ')
        attrs = _attrs_4369730896
        _write('<body>\n      ')
        attrs = _attrs_4369731536
        _write('<div id="content" class="ui-admin ui-widget">\n        ')
        attrs = _attrs_4369729808
        'request.model_name and breadcrumb'
        _write('<h1 id="header" class="ui-widget-header ui-corner-all">\n          ')
        _tmp1 = (_lookup_attr(econtext['request'], 'model_name') and econtext['breadcrumb'])
        if _tmp1:
            pass
            attrs = _attrs_4369727824
            "''"
            _write('<div class="breadcrumb">\n            ')
            _default.value = default = ''
            'breadcrumb.render(request)'
            _content = _lookup_attr(econtext['breadcrumb'], 'render')(econtext['request'])
            attrs = _attrs_4369727696
            '_content'
            _write('<select id="models" style="display:none;">')
            _tmp1 = _content
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, str, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, str):
                    _tmp = str(_tmp)
                _write(_tmp)
            _write('</select>\n          </div>')
        'request.model_name'
        _write('\n          ')
        _tmp1 = _lookup_attr(econtext['request'], 'model_name')
        if _tmp1:
            pass
            attrs = _attrs_4369727952
            "''"
            _write('<div>\n            ')
            _default.value = default = ''
            'model_class.plural'
            _content = _lookup_attr(econtext['model_class'], 'plural')
            attrs = _attrs_4369730832
            'request.fa_url(model_name)'
            _write('<a')
            _tmp1 = _lookup_attr(econtext['request'], 'fa_url')(econtext['model_name'])
            if (_tmp1 is _default):
                _tmp1 = None
            if ((_tmp1 is not None) and (_tmp1 is not False)):
                if (_tmp1.__class__ not in (str, str, int, float, )):
                    _tmp1 = str(_translate(_tmp1, domain=_domain, mapping=None, target_language=target_language, default=None))
                else:
                    if not isinstance(_tmp1, str):
                        _tmp1 = str(_tmp1)
                if ('&' in _tmp1):
                    if (';' in _tmp1):
                        _tmp1 = _re_amp.sub('&amp;', _tmp1)
                    else:
                        _tmp1 = _tmp1.replace('&', '&amp;')
                if ('<' in _tmp1):
                    _tmp1 = _tmp1.replace('<', '&lt;')
                if ('>' in _tmp1):
                    _tmp1 = _tmp1.replace('>', '&gt;')
                if ('"' in _tmp1):
                    _tmp1 = _tmp1.replace('"', '&quot;')
                _write(((' href="' + _tmp1) + '"'))
            '_content'
            _write('>')
            _tmp1 = _content
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, str, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, str):
                    _tmp = str(_tmp)
                if ('&' in _tmp):
                    if (';' in _tmp):
                        _tmp = _re_amp.sub('&amp;', _tmp)
                    else:
                        _tmp = _tmp.replace('&', '&amp;')
                if ('<' in _tmp):
                    _tmp = _tmp.replace('<', '&lt;')
                if ('>' in _tmp):
                    _tmp = _tmp.replace('>', '&gt;')
                _write(_tmp)
            "''"
            _write('</a>\n            ')
            _default.value = default = ''
            "request.model_id and hasattr(request.model_class, '__unicode__')"
            _tmp1 = (_lookup_attr(econtext['request'], 'model_id') and hasattr(_lookup_attr(econtext['request'], 'model_class'), '__unicode__'))
            if _tmp1:
                pass
                'unicode(request.model_instance)'
                _content = str(_lookup_attr(econtext['request'], 'model_instance'))
                '_content'
                _tmp1 = _content
                _tmp = _tmp1
                if (_tmp.__class__ not in (str, str, int, float, )):
                    try:
                        _tmp = _tmp.__html__
                    except:
                        _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                    else:
                        _tmp = _tmp()
                        _write(_tmp)
                        _tmp = None
                if (_tmp is not None):
                    if not isinstance(_tmp, str):
                        _tmp = str(_tmp)
                    if ('&' in _tmp):
                        if (';' in _tmp):
                            _tmp = _re_amp.sub('&amp;', _tmp)
                        else:
                            _tmp = _tmp.replace('&', '&amp;')
                    if ('<' in _tmp):
                        _tmp = _tmp.replace('<', '&lt;')
                    if ('>' in _tmp):
                        _tmp = _tmp.replace('>', '&gt;')
                    _write(_tmp)
            "''"
            _write('\n            ')
            _default.value = default = ''
            "request.model_id and not hasattr(request.model_class, '__unicode__')"
            _tmp1 = (_lookup_attr(econtext['request'], 'model_id') and not hasattr(_lookup_attr(econtext['request'], 'model_class'), '__unicode__'))
            if _tmp1:
                pass
                'request.model_id'
                _content = _lookup_attr(econtext['request'], 'model_id')
                '_content'
                _tmp1 = _content
                _tmp = _tmp1
                if (_tmp.__class__ not in (str, str, int, float, )):
                    try:
                        _tmp = _tmp.__html__
                    except:
                        _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                    else:
                        _tmp = _tmp()
                        _write(_tmp)
                        _tmp = None
                if (_tmp is not None):
                    if not isinstance(_tmp, str):
                        _tmp = str(_tmp)
                    if ('&' in _tmp):
                        if (';' in _tmp):
                            _tmp = _re_amp.sub('&amp;', _tmp)
                        else:
                            _tmp = _tmp.replace('&', '&amp;')
                    if ('<' in _tmp):
                        _tmp = _tmp.replace('<', '&lt;')
                    if ('>' in _tmp):
                        _tmp = _tmp.replace('>', '&gt;')
                    _write(_tmp)
            _write('\n          </div>')
        _write('\n          ')
        _tmp_domain0 = _domain
        "u'fa_jquery'"
        _domain = 'fa_jquery'
        'not request.model_name'
        _tmp1 = not _lookup_attr(econtext['request'], 'model_name')
        if _tmp1:
            pass
            attrs = _attrs_4369729040
            "u'Models index'"
            _write('<div>')
            _msgid = 'Models index'
            "%(translate)s(' '.join(%(msgid)s.split()), domain=%(domain)s, mapping=None, target_language=%(language)s, default=%(msgid)s)"
            _result = _translate(_lookup_attr(' ', 'join')(_msgid.split()), domain=_domain, mapping=None, target_language=target_language, default=_msgid)
            '_result'
            _tmp1 = _result
            _write((_tmp1 + '</div>'))
        _write('\n        ')
        _domain = _tmp_domain0
        "%(slots)s.get(u'main')"
        _write('</h1>\n        ')
        _tmp = _slots.get('main')
        '%(tmp)s is not None'
        _tmp1 = (_tmp is not None)
        if _tmp1:
            pass
            'isinstance(%(tmp)s, basestring)'
            _tmp2 = isinstance(_tmp, basestring)
            if not _tmp2:
                pass
                econtext.update(dict(rcontext=rcontext, _domain=_domain))
                _tmp(econtext, repeat)
            else:
                pass
                '%(tmp)s'
                _tmp2 = _tmp
                _tmp = _tmp2
                if (_tmp.__class__ not in (str, str, int, float, )):
                    try:
                        _tmp = _tmp.__html__
                    except:
                        _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                    else:
                        _tmp = _tmp()
                        _write(_tmp)
                        _tmp = None
                if (_tmp is not None):
                    if not isinstance(_tmp, str):
                        _tmp = str(_tmp)
                    _write(_tmp)
        else:
            pass
            attrs = _attrs_4369730512
            _write('<div>\n        </div>')
        _write('\n        ')
        attrs = _attrs_4369728720
        "''"
        _write('<div class="footer-actions">\n          ')
        _default.value = default = ''
        'actions.languages'
        _tmp1 = _lookup_attr(econtext['actions'], 'languages')
        if _tmp1:
            pass
            'actions.languages(request)'
            _content = _lookup_attr(econtext['actions'], 'languages')(econtext['request'])
            attrs = _attrs_4369729296
            '_content'
            _write('<ul id="languages">')
            _tmp1 = _content
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, str, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, str):
                    _tmp = str(_tmp)
                _write(_tmp)
            _write('</ul>')
        "''"
        _write('\n          ')
        _default.value = default = ''
        'actions.themes'
        _tmp1 = _lookup_attr(econtext['actions'], 'themes')
        if _tmp1:
            pass
            'actions.themes(request)'
            _content = _lookup_attr(econtext['actions'], 'themes')(econtext['request'])
            attrs = _attrs_4369729872
            '_content'
            _write('<select id="themes">')
            _tmp1 = _content
            _tmp = _tmp1
            if (_tmp.__class__ not in (str, str, int, float, )):
                try:
                    _tmp = _tmp.__html__
                except:
                    _tmp = _translate(_tmp, domain=_domain, mapping=None, target_language=target_language, default=None)
                else:
                    _tmp = _tmp()
                    _write(_tmp)
                    _tmp = None
            if (_tmp is not None):
                if not isinstance(_tmp, str):
                    _tmp = str(_tmp)
                _write(_tmp)
            _write('</select>')
        _write('\n        </div>\n        ')
        attrs = _attrs_4369728400
        'request.fa_url()'
        _write('<a style="display:none" class="root_url"')
        _tmp1 = _lookup_attr(econtext['request'], 'fa_url')()
        if (_tmp1 is _default):
            _tmp1 = None
        if ((_tmp1 is not None) and (_tmp1 is not False)):
            if (_tmp1.__class__ not in (str, str, int, float, )):
                _tmp1 = str(_translate(_tmp1, domain=_domain, mapping=None, target_language=target_language, default=None))
            else:
                if not isinstance(_tmp1, str):
                    _tmp1 = str(_tmp1)
            if ('&' in _tmp1):
                if (';' in _tmp1):
                    _tmp1 = _re_amp.sub('&amp;', _tmp1)
                else:
                    _tmp1 = _tmp1.replace('&', '&amp;')
            if ('<' in _tmp1):
                _tmp1 = _tmp1.replace('<', '&lt;')
            if ('>' in _tmp1):
                _tmp1 = _tmp1.replace('>', '&gt;')
            if ('"' in _tmp1):
                _tmp1 = _tmp1.replace('"', '&quot;')
            _write(((' href="' + _tmp1) + '"'))
        _write('></a>\n      </div>\n    </body>\n</html>')
        return
    return render

__filename__ = '/Users/gawel/py/formalchemy_project/fa.jquery/fa/jquery/templates/admin/master.pt'
registry[('master', False, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
