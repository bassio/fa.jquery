registry = dict(version=0)
def bind():
    from cPickle import loads as _loads
    _lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
    _attrs_4362880848 = _loads('(dp1\nVlanguage\np2\nVjavascript\np3\ns.')
    _init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
    _re_amp = _loads("cre\n_compile\np1\n(S'&(?!([A-Za-z]+|#[0-9]+);)'\np2\nI0\ntRp3\n.")
    _attrs_4362881360 = _loads('(dp1\nVclass\np2\nVui-icon ui-icon-circle-plus\np3\ns.')
    _attrs_4362880976 = _loads('(dp1\n.')
    _attrs_4362880592 = _loads('(dp1\nVtype\np2\nVtext/javascript\np3\ns.')
    _attrs_4362880016 = _loads('(dp1\n.')
    _attrs_4362881168 = _loads('(dp1\nVclass\np2\nVui-widget-header ui-widget-link ui-corner-all\np3\ns.')
    _init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
    _attrs_4362880912 = _loads('(dp1\n.')
    _attrs_4362880208 = _loads('(dp1\n.')
    _attrs_4362880528 = _loads('(dp1\nVrel\np2\nVstylesheet\np3\ns.')
    _init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
    _attrs_4362880720 = _loads('(dp1\n.')
    _attrs_4362880464 = _loads('(dp1\nVrel\np2\nVstylesheet\np3\ns.')
    _attrs_4362880400 = _loads('(dp1\n.')
    _init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
    def render(econtext, rcontext=None):
        macros = econtext.get('macros')
        _translate = econtext.get('_translate')
        _slots = econtext.get('_slots')
        target_language = econtext.get('target_language')
        '_init_stream()'
        (_out, _write, ) = _init_stream()
        '_init_tal()'
        (_attributes, repeat, ) = _init_tal()
        '_init_default()'
        _default = _init_default()
        'None'
        default = None
        'None'
        _domain = None
        attrs = _attrs_4362880208
        _write('<html>\n  ')
        attrs = _attrs_4362880016
        _write('<head>\n      ')
        attrs = _attrs_4362880464
        "request.static_url('fa.jquery:jquery-ui/css/smoothness/jquery-ui-1.8.8.custom.css')"
        _write('<link rel="stylesheet"')
        _tmp1 = _lookup_attr(econtext['request'], 'static_url')('fa.jquery:jquery-ui/css/smoothness/jquery-ui-1.8.8.custom.css')
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
        _write(' />\n      ')
        attrs = _attrs_4362880528
        "request.static_url('fa.jquery:jquery-ui/fa.jquery.min.css')"
        _write('<link rel="stylesheet"')
        _tmp1 = _lookup_attr(econtext['request'], 'static_url')('fa.jquery:jquery-ui/fa.jquery.min.css')
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
        _write(' />\n      ')
        attrs = _attrs_4362880592
        "request.static_url('fa.jquery:jquery-ui/fa.jquery.min.js')"
        _write('<script type="text/javascript"')
        _tmp1 = _lookup_attr(econtext['request'], 'static_url')('fa.jquery:jquery-ui/fa.jquery.min.js')
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
            _write(((' src="' + _tmp1) + '"'))
        _write('></script>\n  </head>\n  ')
        attrs = _attrs_4362880400
        _write('<body>\n    ')
        attrs = _attrs_4362880720
        _write('<div>\n      ')
        attrs = _attrs_4362880848
        "''"
        _write('<script language="javascript">\n        var USE_POPUP = false;\n      </script>\n      ')
        _default.value = default = ''
        "fs.render(renderer='fa.jquery:templates/forms/jqgrid.pt', request=request)"
        _content = _lookup_attr(econtext['fs'], 'render')(renderer='fa.jquery:templates/forms/jqgrid.pt', request=econtext['request'])
        attrs = _attrs_4362880912
        '_content'
        _write('<div>')
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
        _write('</div>\n      ')
        attrs = _attrs_4362880976
        _write('<p>\n        ')
        attrs = _attrs_4362881168
        "request.route_url(request.route_name, traverse='%s/new' % request.model_name)"
        _write('<a class="ui-widget-header ui-widget-link ui-corner-all"')
        _tmp1 = _lookup_attr(econtext['request'], 'route_url')(_lookup_attr(econtext['request'], 'route_name'), traverse=('%s/new' % _lookup_attr(econtext['request'], 'model_name')))
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
        _write('>\n            ')
        attrs = _attrs_4362881360
        "F_('New')"
        _write('<span class="ui-icon ui-icon-circle-plus"></span>\n            ')
        _tmp1 = econtext['F_']('New')
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
        'model_name'
        _write(' ')
        _tmp1 = econtext['model_name']
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
        _write('\n        </a>\n      </p>\n    </div>\n  </body>\n</html>')
        return _out.getvalue()
    return render

__filename__ = '/Users/gawel/py/formalchemy_project/fa.jquery/fa/jquery/templates/admin/relation.pt'
registry[(None, True, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
