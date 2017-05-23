# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###


DefinitionsCreateprofession = {'properties': {'name': {'type': 'string'}}}
DefinitionsUpdateplacefile = {'properties': {'content': {'type': 'string'}, 'imgs': {'items': {'type': 'string'}, 'type': 'array'}, 'name': {'type': 'string'}}}
DefinitionsUpdategamerole = {'properties': {'profession_id': {'type': 'integer', 'format': 'int32'}, 'name': {'type': 'string'}, 'true_name': {'type': 'string'}, 'summary': {'type': 'string'}, 'play_script': {'items': {'type': 'string'}, 'type': 'array'}, '_avatar': {'type': 'string'}, 'hidden_profession_id': {'type': 'integer', 'format': 'int32'}, 'desc': {'type': 'string'}}}
DefinitionsGamerole = {'properties': {'profession_id': {'type': 'integer', 'format': 'int32'}, 'name': {'type': 'string'}, 'true_name': {'type': 'string'}, 'summary': {'type': 'string'}, 'play_script': {'items': {'type': 'string'}, 'type': 'array'}, '_avatar': {'type': 'string'}, 'hidden_profession_id': {'type': 'integer', 'format': 'int32'}, 'game_id': {'type': 'string'}, 'id': {'type': 'integer', 'format': 'int32'}, 'desc': {'type': 'string'}}}
DefinitionsCreategameplace = {'properties': {'hiding_keys': {'items': {'type': 'string'}, 'type': 'array'}, 'name': {'type': 'string'}, 'owner': {'type': 'integer', 'format': 'int32'}, 'allow_type': {'type': 'string'}, 'is_hiding': {'type': 'boolean'}, 'type': {'type': 'string'}, 'allow_ids': {'items': {'type': 'integer', 'format': 'int32'}, 'type': 'array'}}}
DefinitionsUpdateplaceclue = {'properties': {'content': {'type': 'string'}, 'imgs': {'items': {'type': 'string'}, 'type': 'array'}, 'order_score': {'type': 'integer'}}}
DefinitionsCreateplaceclue = {'properties': {'content': {'type': 'string'}, 'imgs': {'items': {'type': 'string'}, 'type': 'array'}, 'order_score': {'type': 'integer'}}}
DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsPlacefile = {'properties': {'content': {'type': 'string'}, 'imgs': {'items': {'type': 'string'}, 'type': 'array'}, 'place_id': {'type': 'integer'}, 'id': {'type': 'integer', 'format': 'int32'}, 'name': {'type': 'string'}}}
DefinitionsProfession = {'properties': {'id': {'type': 'integer', 'format': 'int32'}, 'name': {'type': 'string'}}}
DefinitionsCreatelarpgame = {'required': ['name'], 'properties': {'manager_manual': {'type': 'string'}, 'description': {'type': 'string'}, 'name': {'type': 'string'}, 'ap_num': {'type': 'integer', 'format': 'int32'}, 'price': {'type': 'integer', 'format': 'int32'}, 'max_required_num': {'type': 'integer', 'format': 'int32'}, 'player_manual': {'type': 'string'}, 'summary': {'type': 'string'}, 'others': {'type': 'string'}, 'mission_manual': {'type': 'string'}, 'icon': {'type': 'string'}, 'type': {'type': 'string'}, 'min_required_num': {'type': 'integer', 'format': 'int32'}}}
DefinitionsNone = {'type': 'object'}
DefinitionsUpdateprofession = {'properties': {'name': {'type': 'string'}}}
DefinitionsCreateplacefile = {'properties': {'content': {'type': 'string'}, 'imgs': {'items': {'type': 'string'}, 'type': 'array'}, 'name': {'type': 'string'}}}
DefinitionsPlaceclue = {'properties': {'content': {'type': 'string'}, 'imgs': {'items': {'type': 'string'}, 'type': 'array'}, 'place_id': {'type': 'integer'}, 'order_score': {'type': 'integer'}, 'id': {'type': 'integer', 'format': 'int32'}}}
DefinitionsGameplace = {'properties': {'name': {'type': 'string'}, 'type': {'type': 'string'}, 'is_hiding': {'type': 'boolean'}, 'hiding_keys': {'items': {'type': 'string'}, 'type': 'array'}, 'owner': {'type': 'integer', 'format': 'int32'}, 'game_id': {'type': 'string'}, 'allow_type': {'type': 'string'}, 'id': {'type': 'integer', 'format': 'int32'}, 'allow_ids': {'items': {'type': 'integer', 'format': 'int32'}, 'type': 'array'}}}
DefinitionsLarpgame = {'properties': {'manager_manual': {'type': 'string'}, 'description': {'type': 'string'}, 'ap_num': {'type': 'integer', 'format': 'int32'}, 'price': {'type': 'integer', 'format': 'int32'}, 'max_required_num': {'type': 'integer', 'format': 'int32'}, 'player_manual': {'type': 'string'}, 'summary': {'type': 'string'}, 'others': {'type': 'string'}, 'mission_manual': {'type': 'string'}, 'min_required_num': {'type': 'integer', 'format': 'int32'}, 'icon': {'type': 'string'}, 'type': {'type': 'string'}, 'id': {'type': 'string'}, 'name': {'type': 'string'}}}
DefinitionsUpdatelarpgame = {'properties': {'manager_manual': {'type': 'string'}, 'description': {'type': 'string'}, 'name': {'type': 'string'}, 'ap_num': {'type': 'integer', 'format': 'int32'}, 'price': {'type': 'integer', 'format': 'int32'}, 'max_required_num': {'type': 'integer', 'format': 'int32'}, 'player_manual': {'type': 'string'}, 'summary': {'type': 'string'}, 'others': {'type': 'string'}, 'mission_manual': {'type': 'string'}, 'icon': {'type': 'string'}, 'type': {'type': 'string'}, 'min_required_num': {'type': 'integer', 'format': 'int32'}}}
DefinitionsUpdategameplace = {'properties': {'hiding_keys': {'items': {'type': 'string'}, 'type': 'array'}, 'name': {'type': 'string'}, 'owner': {'type': 'integer', 'format': 'int32'}, 'allow_type': {'type': 'string'}, 'is_hiding': {'type': 'boolean'}, 'type': {'type': 'string'}, 'allow_ids': {'items': {'type': 'integer', 'format': 'int32'}, 'type': 'array'}}}
DefinitionsCreategamerole = {'properties': {'profession_id': {'type': 'integer', 'format': 'int32'}, 'name': {'type': 'string'}, 'true_name': {'type': 'string'}, 'summary': {'type': 'string'}, 'play_script': {'items': {'type': 'string'}, 'type': 'array'}, '_avatar': {'type': 'string'}, 'hidden_profession_id': {'type': 'integer', 'format': 'int32'}, 'desc': {'type': 'string'}}}
DefinitionsError = {'properties': {'text': {'type': 'string'}, 'message': {'type': 'string'}, 'error_code': {'type': 'string'}}}

validators = {
    ('places_id_clue', 'POST'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsCreateplaceclue},
    ('places_id_clue', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'per_page': {'description': 'per_page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'limit': {'description': 'limit number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'page': {'description': 'page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 10000}, 'offset': {'description': 'offset number', 'format': 'int32', 'required': False, 'type': 'integer'}}}},
    ('places_place_id', 'PUT'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsUpdategameplace},
    ('places_place_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('places_place_id', 'DELETE'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('games_id', 'PUT'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsUpdatelarpgame},
    ('games_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('clue_id', 'PUT'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsUpdateplaceclue},
    ('clue_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('clue_id', 'DELETE'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('games', 'POST'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsCreatelarpgame},
    ('games', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'per_page': {'description': 'per_page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'limit': {'description': 'limit number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'page': {'description': 'page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 10000}, 'offset': {'description': 'offset number', 'format': 'int32', 'required': False, 'type': 'integer'}}}},
    ('file_id', 'PUT'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsUpdateplacefile},
    ('file_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('file_id', 'DELETE'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('games_id_places', 'POST'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsCreategameplace},
    ('games_id_places', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'per_page': {'description': 'per_page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'limit': {'description': 'limit number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'page': {'description': 'page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 10000}, 'offset': {'description': 'offset number', 'format': 'int32', 'required': False, 'type': 'integer'}}}},
    ('places_id_file', 'POST'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsCreateplacefile},
    ('places_id_file', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'per_page': {'description': 'per_page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'limit': {'description': 'limit number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'page': {'description': 'page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 10000}, 'offset': {'description': 'offset number', 'format': 'int32', 'required': False, 'type': 'integer'}}}},
    ('professions_id', 'PUT'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsUpdateprofession},
    ('professions_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('professions_id', 'DELETE'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('professions', 'POST'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsCreateprofession},
    ('professions', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'per_page': {'description': 'per_page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'limit': {'description': 'limit number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'page': {'description': 'page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 10000}, 'offset': {'description': 'offset number', 'format': 'int32', 'required': False, 'type': 'integer'}}}},
    ('games_id_roles', 'POST'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsCreategamerole},
    ('games_id_roles', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'per_page': {'description': 'per_page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'limit': {'description': 'limit number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'page': {'description': 'page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 10000}, 'offset': {'description': 'offset number', 'format': 'int32', 'required': False, 'type': 'integer'}}}},
    ('roles_role_id', 'PUT'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsUpdategamerole},
    ('roles_role_id', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
    ('roles_role_id', 'DELETE'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}},
}

filters = {
    ('places_id_clue', 'POST'): {201: {'headers': None, 'schema': DefinitionsPlaceclue}},
    ('places_id_clue', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsPlaceclue, 'type': 'array'}}},
    ('places_place_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsGameplace}},
    ('places_place_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsGameplace}},
    ('places_place_id', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
    ('games_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsLarpgame}},
    ('games_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsLarpgame}},
    ('clue_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsPlaceclue}},
    ('clue_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsPlaceclue}},
    ('clue_id', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
    ('games', 'POST'): {201: {'headers': None, 'schema': DefinitionsLarpgame}},
    ('games', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsLarpgame, 'type': 'array'}}},
    ('file_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsPlacefile}},
    ('file_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsPlacefile}},
    ('file_id', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
    ('games_id_places', 'POST'): {201: {'headers': None, 'schema': DefinitionsGameplace}},
    ('games_id_places', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsGameplace, 'type': 'array'}}},
    ('places_id_file', 'POST'): {201: {'headers': None, 'schema': DefinitionsPlacefile}},
    ('places_id_file', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsPlacefile, 'type': 'array'}}},
    ('professions_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsProfession}},
    ('professions_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsProfession}},
    ('professions_id', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
    ('professions', 'POST'): {201: {'headers': None, 'schema': DefinitionsProfession}},
    ('professions', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsProfession, 'type': 'array'}}},
    ('games_id_roles', 'POST'): {201: {'headers': None, 'schema': DefinitionsGamerole}},
    ('games_id_roles', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsGamerole, 'type': 'array'}}},
    ('roles_role_id', 'PUT'): {200: {'headers': None, 'schema': DefinitionsGamerole}},
    ('roles_role_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsGamerole}},
    ('roles_role_id', 'DELETE'): {204: {'headers': None, 'schema': DefinitionsSuccess}},
}

scopes = {
    ('places_id_clue', 'POST'): ['panel'],
    ('places_id_clue', 'GET'): ['panel'],
    ('places_place_id', 'PUT'): ['panel'],
    ('places_place_id', 'GET'): ['panel'],
    ('places_place_id', 'DELETE'): ['panel'],
    ('games_id', 'PUT'): ['panel'],
    ('games_id', 'GET'): ['panel'],
    ('clue_id', 'PUT'): ['panel'],
    ('clue_id', 'GET'): ['panel'],
    ('clue_id', 'DELETE'): ['panel'],
    ('games', 'POST'): ['panel'],
    ('games', 'GET'): ['panel'],
    ('file_id', 'PUT'): ['panel'],
    ('file_id', 'GET'): ['panel'],
    ('file_id', 'DELETE'): ['panel'],
    ('games_id_places', 'POST'): ['panel'],
    ('games_id_places', 'GET'): ['panel'],
    ('places_id_file', 'POST'): ['panel'],
    ('places_id_file', 'GET'): ['panel'],
    ('professions_id', 'PUT'): ['panel'],
    ('professions_id', 'GET'): ['panel'],
    ('professions_id', 'DELETE'): ['panel'],
    ('professions', 'POST'): ['panel'],
    ('professions', 'GET'): ['panel'],
    ('games_id_roles', 'POST'): ['panel'],
    ('games_id_roles', 'GET'): ['panel'],
    ('roles_role_id', 'PUT'): ['panel'],
    ('roles_role_id', 'GET'): ['panel'],
    ('roles_role_id', 'DELETE'): ['panel'],
}


class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None):

    import six

    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(vars(self.data).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            rs_component.update(result)
            result = rs_component

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, dict):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize(schema, data):
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if not type_ in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors

