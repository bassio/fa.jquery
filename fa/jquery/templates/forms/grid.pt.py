registry = dict(version=0)
def bind():
    from pickle import loads as _loads
    _lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
    _init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
    _re_amp = _loads("cre\n_compile\np1\n(S'&(?!([A-Za-z]+|#[0-9]+);)'\np2\nI0\ntRp3\n.")
    _attrs_4355504080 = _loads('(dp1\n.')
    _attrs_4355531408 = _loads('(dp1\n.')
    _attrs_4355533904 = _loads('(dp1\n.')
    _attrs_4355533264 = _loads('(dp1\nVclass\np2\nVlayout-grid\np3\ns.')
    _attrs_4355533520 = _loads('(dp1\n.')
    _init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
    _attrs_4355533648 = _loads('(dp1\nVclass\np2\nVui-widget-header\np3\ns.')
    _attrs_4355504144 = _loads('(dp1\n.')
    _init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
    _attrs_4355503824 = _loads('(dp1\n.')
    _init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
    _attrs_4355534032 = _loads('(dp1\nVclass\np2\nVgrid_error\np3\ns.')
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
        attrs = _attrs_4355533264
        _write('<table class="layout-grid">\n')
        attrs = _attrs_4355533520
        _write('<thead>\n  ')
        attrs = _attrs_4355533648
        "''"
        _write('<tr class="ui-widget-header">\n    ')
        _default.value = default = ''
        'collection.render_fields.itervalues()'
        _tmp1 = _lookup_attr(_lookup_attr(econtext['collection'], 'render_fields'), 'itervalues')()
        field = None
        (_tmp1, _tmp2, ) = repeat.insert('field', _tmp1)
        for field in _tmp1:
            _tmp2 = (_tmp2 - 1)
            'field.label()'
            _content = _lookup_attr(field, 'label')()
            attrs = _attrs_4355503824
            '_content'
            _write('<th>')
            _tmp3 = _content
            _tmp = _tmp3
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
            _write('</th>')
            if (_tmp2 == 0):
                break
            _write(' ')
        _write('\n  </tr>\n</thead>\n')
        attrs = _attrs_4355504080
        'collection.rows'
        _write('<tbody>\n  ')
        _tmp1 = _lookup_attr(econtext['collection'], 'rows')
        row = None
        (_tmp1, _tmp2, ) = repeat.insert('row', _tmp1)
        for row in _tmp1:
            _tmp2 = (_tmp2 - 1)
            'collection._set_active(row)'
            _write('')
            dummy = _lookup_attr(econtext['collection'], '_set_active')(row)
            'collection.get_errors(row)'
            row_errors = _lookup_attr(econtext['collection'], 'get_errors')(row)
            attrs = _attrs_4355504144
            "ui-widget-${repeat.row.even and 'even' or 'odd'}"
            _write('<tr')
            _tmp3 = ('%s%s' % ('ui-widget-', ((_lookup_attr(repeat.row, 'even') and 'even') or 'odd'), ))
            if (_tmp3 is _default):
                _tmp3 = None
            if ((_tmp3 is not None) and (_tmp3 is not False)):
                if (_tmp3.__class__ not in (str, str, int, float, )):
                    _tmp3 = str(_translate(_tmp3, domain=_domain, mapping=None, target_language=target_language, default=None))
                else:
                    if not isinstance(_tmp3, str):
                        _tmp3 = str(_tmp3)
                if ('&' in _tmp3):
                    if (';' in _tmp3):
                        _tmp3 = _re_amp.sub('&amp;', _tmp3)
                    else:
                        _tmp3 = _tmp3.replace('&', '&amp;')
                if ('<' in _tmp3):
                    _tmp3 = _tmp3.replace('<', '&lt;')
                if ('>' in _tmp3):
                    _tmp3 = _tmp3.replace('>', '&gt;')
                if ('"' in _tmp3):
                    _tmp3 = _tmp3.replace('"', '&quot;')
                _write(((' class="' + _tmp3) + '"'))
            'collection.render_fields.itervalues()'
            _write('>\n      ')
            _tmp3 = _lookup_attr(_lookup_attr(econtext['collection'], 'render_fields'), 'itervalues')()
            field = None
            (_tmp3, _tmp4, ) = repeat.insert('field', _tmp3)
            for field in _tmp3:
                _tmp4 = (_tmp4 - 1)
                attrs = _attrs_4355531408
                "''"
                _write('<td>\n        ')
                _default.value = default = ''
                'field.render()'
                _content = _lookup_attr(field, 'render')()
                attrs = _attrs_4355533904
                '_content'
                _write('<div>')
                _tmp5 = _content
                _tmp = _tmp5
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
                'row_errors.get(field, [])'
                _write('</div>\n        ')
                _tmp5 = _lookup_attr(row_errors, 'get')(field, [])
                error = None
                (_tmp5, _tmp6, ) = repeat.insert('error', _tmp5)
                for error in _tmp5:
                    _tmp6 = (_tmp6 - 1)
                    attrs = _attrs_4355534032
                    'error'
                    _write('<span class="grid_error">')
                    _tmp7 = error
                    _tmp = _tmp7
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
                    _write('</span>')
                    if (_tmp6 == 0):
                        break
                    _write(' ')
                _write('\n      </td>')
                if (_tmp4 == 0):
                    break
                _write(' ')
            _write('\n    </tr>\n  ')
            if (_tmp2 == 0):
                break
            _write(' ')
        _write('\n</tbody>\n</table>')
        return _out.getvalue()
    return render

__filename__ = '/Users/gawel/py/formalchemy_project/fa.jquery/fa/jquery/templates/forms/grid.pt'
registry[(None, True, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
