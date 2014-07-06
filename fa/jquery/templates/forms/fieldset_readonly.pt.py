registry = dict(version=0)
def bind():
    from cPickle import loads as _loads
    _attrs_4354711824 = _loads('(dp1\nVclass\np2\nVfield_readonly\np3\ns.')
    _lookup_attr = _loads('cchameleon.core.codegen\nlookup_attr\np1\n.')
    _init_scope = _loads('cchameleon.core.utils\necontext\np1\n.')
    _attrs_4354712656 = _loads('(dp1\n.')
    _init_stream = _loads('cchameleon.core.generation\ninitialize_stream\np1\n.')
    _attrs_4354712144 = _loads('(dp1\n.')
    _init_default = _loads('cchameleon.core.generation\ninitialize_default\np1\n.')
    _attrs_4354693392 = _loads('(dp1\nVstyle\np2\nVdisplay:none\np3\ns.')
    _attrs_4356436944 = _loads('(dp1\n.')
    _attrs_4356363984 = _loads('(dp1\n.')
    _init_tal = _loads('cchameleon.core.generation\ninitialize_tal\np1\n.')
    _attrs_4354715280 = _loads('(dp1\n.')
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
        attrs = _attrs_4356363984
        'fieldset.render_fields.itervalues()'
        _write('<tbody>\n  ')
        _tmp1 = _lookup_attr(_lookup_attr(econtext['fieldset'], 'render_fields'), 'itervalues')()
        field = None
        (_tmp1, _tmp2, ) = repeat.insert('field', _tmp1)
        for field in _tmp1:
            _tmp2 = (_tmp2 - 1)
            'field.requires_label'
            _write('')
            _tmp3 = _lookup_attr(field, 'requires_label')
            if _tmp3:
                pass
                attrs = _attrs_4356436944
                _write('<tr>\n      ')
                attrs = _attrs_4354711824
                "''"
                _write('<td class="field_readonly">\n        ')
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
                "''"
                _write('\n      </td>\n      ')
                _default.value = default = ''
                'field.render_readonly()'
                _content = _lookup_attr(field, 'render_readonly')()
                attrs = _attrs_4354712656
                '_content'
                _write('<td>')
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
                _write('</td>\n    </tr>')
            _write('\n  ')
            if (_tmp2 == 0):
                break
            _write(' ')
        _write('\n  ')
        attrs = _attrs_4354693392
        _write('<tr style="display:none">')
        attrs = _attrs_4354712144
        _write('<td>&nbsp;</td>')
        attrs = _attrs_4354715280
        'fieldset.render_fields.itervalues()'
        _write('<td>\n    ')
        _tmp1 = _lookup_attr(_lookup_attr(econtext['fieldset'], 'render_fields'), 'itervalues')()
        field = None
        (_tmp1, _tmp2, ) = repeat.insert('field', _tmp1)
        for field in _tmp1:
            _tmp2 = (_tmp2 - 1)
            "''"
            _write('')
            _default.value = default = ''
            'not field.requires_label'
            _tmp3 = not _lookup_attr(field, 'requires_label')
            if _tmp3:
                pass
                'field.render_readonly()'
                _content = _lookup_attr(field, 'render_readonly')()
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
            _write('\n    ')
            if (_tmp2 == 0):
                break
            _write(' ')
        _write('\n  </td>\n  </tr>\n</tbody>')
        return _out.getvalue()
    return render

__filename__ = '/Users/gawel/py/formalchemy_project/fa.jquery/fa/jquery/templates/forms/fieldset_readonly.pt'
registry[(None, True, '1488bdb950901f8f258549439ef6661a49aae984')] = bind()
