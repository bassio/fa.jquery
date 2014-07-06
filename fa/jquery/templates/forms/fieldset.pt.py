registry = dict(version=0)
def bind():
    from pickle import loads as _loads
    _lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
    _init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
    _re_amp = _loads("cre\n_compile\np1\n(S'&(?!([A-Za-z]+|#[0-9]+);)'\np2\nI0\ntRp3\n.")
    _attrs_4356366160 = _loads('(dp1\n.')
    _attrs_4356365968 = _loads('(dp1\nVclass\np2\nVlabel\np3\ns.')
    _attrs_4354644240 = _loads('(dp1\nVclass\np2\nVfield_input\np3\ns.')
    _init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
    _attrs_4356365520 = _loads('(dp1\nVclass\np2\nVfa_field ui-widget\np3\ns.')
    _attrs_4354605328 = _loads('(dp1\nVclass\np2\nVui-state-error ui-corner-all\np3\ns.')
    _init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
    _attrs_4356365072 = _loads('(dp1\nVclass\np2\nVfa_field\np3\ns.')
    _attrs_4354643792 = _loads('(dp1\n.')
    _attrs_4356365328 = _loads('(dp1\nVclass\np2\nVui-state-error ui-corner-all\np3\ns.')
    _attrs_4354664848 = _loads('(dp1\nVclass\np2\nVfa_instructions ui-corner-all\np3\ns.')
    _init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
    _attrs_4354644176 = _loads('(dp1\n.')
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
        'False'
        focus_rendered = False
        'fieldset.errors.get(None, False)'
        _write('\n')
        _tmp1 = _lookup_attr(_lookup_attr(econtext['fieldset'], 'errors'), 'get')(None, False)
        if _tmp1:
            pass
            attrs = _attrs_4356365072
            "''"
            _write('<div class="fa_field">\n  ')
            _default.value = default = ''
            'fieldset.errors.get(None)'
            _tmp1 = _lookup_attr(_lookup_attr(econtext['fieldset'], 'errors'), 'get')(None)
            error = None
            (_tmp1, _tmp2, ) = repeat.insert('error', _tmp1)
            for error in _tmp1:
                _tmp2 = (_tmp2 - 1)
                'error'
                _content = error
                attrs = _attrs_4356365328
                '_content'
                _write('<div class="ui-state-error ui-corner-all">')
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
                _write('</div>')
                if (_tmp2 == 0):
                    break
                _write(' ')
            _write('\n</div>')
        'fieldset.render_fields.itervalues()'
        _write('\n\n')
        _tmp1 = _lookup_attr(_lookup_attr(econtext['fieldset'], 'render_fields'), 'itervalues')()
        field = None
        (_tmp1, _tmp2, ) = repeat.insert('field', _tmp1)
        for field in _tmp1:
            _tmp2 = (_tmp2 - 1)
            _write('\n  ')
            attrs = _attrs_4356365520
            'field.requires_label'
            _write('<div class="fa_field ui-widget">\n    ')
            _tmp3 = _lookup_attr(field, 'requires_label')
            if _tmp3:
                pass
                attrs = _attrs_4356365968
                "''"
                _write('<div class="label">\n      ')
                _default.value = default = ''
                'isinstance(field.type, fatypes.Boolean)'
                _tmp3 = isinstance(_lookup_attr(field, 'type'), _lookup_attr(econtext['fatypes'], 'Boolean'))
                if _tmp3:
                    pass
                    'field.render()'
                    _content = _lookup_attr(field, 'render')()
                    attrs = _attrs_4356366160
                    '_content'
                    _write('<div>')
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
                        _write(_tmp)
                    _write('</div>')
                "''"
                _write('\n         ')
                _default.value = default = ''
                'field.label_tag()'
                _content = _lookup_attr(field, 'label_tag')()
                '_content'
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
                    _write(_tmp)
                _write('\n    </div>')
            "u'\\n    '"
            _write('\n    ')
            _default.value = default = '\n    '
            "'instructions' in field.metadata"
            _tmp3 = ('instructions' in _lookup_attr(field, 'metadata'))
            if _tmp3:
                pass
                "field.metadata['instructions']"
                _content = _lookup_attr(field, 'metadata')['instructions']
                attrs = _attrs_4354664848
                '_content'
                _write('<div class="fa_instructions ui-corner-all">')
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
                _write('</div>')
            'field.errors'
            _write('\n    ')
            _tmp3 = _lookup_attr(field, 'errors')
            if _tmp3:
                pass
                attrs = _attrs_4354605328
                "''"
                _write('<div class="ui-state-error ui-corner-all">\n      ')
                _default.value = default = ''
                'field.errors'
                _tmp3 = _lookup_attr(field, 'errors')
                error = None
                (_tmp3, _tmp4, ) = repeat.insert('error', _tmp3)
                for error in _tmp3:
                    _tmp4 = (_tmp4 - 1)
                    'error'
                    _content = error
                    attrs = _attrs_4354644176
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
                    _write('</div>')
                    if (_tmp4 == 0):
                        break
                    _write(' ')
                _write('\n    </div>')
            "''"
            _write('\n    ')
            _default.value = default = ''
            'not isinstance(field.type, fatypes.Boolean)'
            _tmp3 = not isinstance(_lookup_attr(field, 'type'), _lookup_attr(econtext['fatypes'], 'Boolean'))
            if _tmp3:
                pass
                'field.render()'
                _content = _lookup_attr(field, 'render')()
                attrs = _attrs_4354644240
                '_content'
                _write('<div class="field_input">')
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
                    _write(_tmp)
                _write('</div>')
            'not field.is_readonly() and (fieldset.focus == field or fieldset.focus is True) and not focus_rendered'
            _write('\n  </div>\n  ')
            _tmp3 = (not _lookup_attr(field, 'is_readonly')() and ((_lookup_attr(econtext['fieldset'], 'focus') == field) or (_lookup_attr(econtext['fieldset'], 'focus') is True)) and not focus_rendered)
            if _tmp3:
                pass
                attrs = _attrs_4354643792
                'True'
                _write('<script>\n    ')
                focus_rendered = True
                'field.renderer.name'
                _write('\n    jQuery(document).ready(function(){jQuery("[name=\'')
                _tmp3 = _lookup_attr(_lookup_attr(field, 'renderer'), 'name')
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
                _write('\']").focus();});\n  </script>')
            _write('\n')
            if (_tmp2 == 0):
                break
            _write(' ')
        _write('')
        return _out.getvalue()
    return render

__filename__ = '/Users/gawel/py/formalchemy_project/fa.jquery/fa/jquery/templates/forms/fieldset.pt'
registry[(None, True, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
