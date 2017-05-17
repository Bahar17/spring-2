# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###


DefinitionsContent = {'minLength': 2, 'type': 'string', 'maxLength': 1024}
DefinitionsQuestionrefusereason = {'properties': {'content': {'type': 'string'}}}
DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsCreatelarpgame = {'required': ['name'], 'properties': {'manager_manual': {'type': 'string'}, 'description': {'type': 'string'}, 'name': {'type': 'string'}, 'ap_num': {'type': 'integer', 'format': 'int32'}, 'price': {'type': 'integer', 'format': 'int32'}, 'max_required_num': {'type': 'integer', 'format': 'int32'}, 'player_manual': {'type': 'string'}, 'summary': {'type': 'string'}, 'others': {'type': 'string'}, 'mission_manual': {'type': 'string'}, 'icon': {'type': 'string'}, 'type': {'type': 'string'}, 'min_required_num': {'type': 'integer', 'format': 'int32'}}}
DefinitionsPay_type = {'enum': ['weixin_pay'], 'type': 'string'}
DefinitionsDatetime = {'type': 'string', 'format': 'datetime'}
DefinitionsNone = {'type': 'object'}
DefinitionsIntroduction = {'minLength': 2, 'type': 'string', 'maxLength': 128}
DefinitionsUrl = {'minLength': 5, 'type': 'string', 'maxLength': 256}
DefinitionsId = {'type': 'integer', 'format': 'int32'}
DefinitionsVoice_id = {'minLength': 16, 'type': 'string', 'maxLength': 32}
DefinitionsCreateweixinpay = {'required': ['order_type', 'trade_type', 'target_type', 'target_id'], 'properties': {'trade_type': {'default': 'NATIVE', 'enum': ['JSAPI', 'NATIVE', 'APP'], 'type': 'string'}, 'target_id': {'type': 'string'}, 'order_type': {'enum': ['ask', 'visit', 'bonus', 'recourse', 'speech'], 'type': 'string', 'description': u'\u8ba2\u5355\u7c7b\u578b \u63d0\u95ee/\u5077\u542c/\u8d5e\u8d4f/\u60ac\u8d4f/\u5c0f\u8bb2'}, 'target_type': {'enum': ['question', 'recourse', 'speech'], 'type': 'string'}}}
DefinitionsQuestion_id = {'minLength': 16, 'type': 'string', 'maxLength': 32}
DefinitionsVoice = {'required': ['id', 'url'], 'properties': {'url': {'type': 'string'}, 'id': {'type': 'string'}}}
DefinitionsWordsearch = {'properties': {'account_id': {'type': 'integer'}, 'name': {'type': 'string'}}}
DefinitionsLarpgame = {'properties': {'manager_manual': {'type': 'string'}, 'description': {'type': 'string'}, 'name': {'type': 'string'}, 'ap_num': {'type': 'integer', 'format': 'int32'}, 'price': {'type': 'integer', 'format': 'int32'}, 'max_required_num': {'type': 'integer', 'format': 'int32'}, 'player_manual': {'type': 'string'}, 'summary': {'type': 'string'}, 'others': {'type': 'string'}, 'mission_manual': {'type': 'string'}, 'icon': {'type': 'string'}, 'type': {'type': 'string'}, 'min_required_num': {'type': 'integer', 'format': 'int32'}}}
DefinitionsQuestion_type = {'enum': ['talk', 'fenda', 'normal', 'tenant', 'recover', 'top_line', 'broadcast', 'commonweal', 'long_voice', 'free_long_voice'], 'type': 'string'}
DefinitionsError = {'properties': {'text': {'type': 'string'}, 'message': {'type': 'string'}, 'error_code': {'type': 'string'}}}
DefinitionsTopic = {'properties': {'id': {'type': 'integer'}, 'name': {'type': 'string'}}}
DefinitionsTaglite = {'properties': {'id': {'type': 'integer'}, 'name': {'type': 'string'}}}
DefinitionsAnswer_id = {'minLength': 16, 'type': 'string', 'maxLength': 32}
DefinitionsUnifiedorder = {'required': ['return_code'], 'properties': {'trade_type': {'enum': ['JSAPI', 'NATIVE', 'APP'], 'type': 'string'}, 'prepay_id': {'type': 'string'}, 'nonce_str': {'type': 'string'}, 'return_code': {'enum': ['SUCCESS', 'FAIL'], 'type': 'string'}, 'return_msg': {'type': 'string', 'description': u'\u9519\u8bef\u539f\u56e0'}, 'sign': {'type': 'string'}, 'device_info': {'type': 'string'}, 'mch_type': {'enum': ['guokr', 'zaihang'], 'type': 'string'}, 'err_code_des': {'type': 'string'}, 'appid': {'type': 'string'}, 'time_stamp': {'type': 'string'}, 'code_url': {'type': 'string', 'description': u'trade_type\u4e3aNATIVE\u662f\u6709\u8fd4\u56de'}, 'result_code': {'enum': ['SUCCESS', 'FAIL'], 'type': 'string', 'description': u'\u4e1a\u52a1\u7ed3\u679c'}, 'err_code': {'type': 'string'}}}
DefinitionsName = {'minLength': 1, 'type': 'string', 'maxLength': 64}
DefinitionsTitle = {'minLength': 2, 'type': 'string', 'maxLength': 18}
DefinitionsMobile = {'minLength': 11, 'type': 'string', 'maxLength': 14}
DefinitionsQuestion_status = {'enum': ['draft', 'paid', 'review', 'rejected', 'succeed', 'refused', 'closed', 'refunded', 'answered', 'revoked'], 'type': 'string'}
DefinitionsOffer = {'minimum': 1, 'type': 'integer', 'maximum': 2000000, 'format': 'int32'}
DefinitionsCount = {'default': 0, 'type': 'integer', 'format': 'int32'}
DefinitionsCreatequestionlisten = {'required': ['source', 'voice_id'], 'properties': {'source': {'enum': ['android', 'yidian', 'weixin', 'web', 'ios'], 'type': 'string', 'description': u'\u542c\u7684\u6765\u6e90'}, 'uid': {'type': 'string'}, 'voice_id': {'type': 'string'}}}
DefinitionsAccountlite = {'required': ['id', 'nickname', 'avatar'], 'properties': {'avatar': DefinitionsUrl, 'title': DefinitionsTitle, 'is_verified': {'type': 'boolean'}, 'price': {'type': 'integer', 'format': 'int32'}, 'nickname': {'minLength': 1, 'type': 'string', 'maxLength': 64}, 'id': DefinitionsId, 'answers_count': {'type': 'integer', 'format': 'int32'}}}
DefinitionsAnswer = {'properties': {'status': {'enum': ['rejected'], 'type': 'string'}, 'is_reanswered': {'type': 'boolean'}, 'date_updated': DefinitionsDatetime, 'is_liked': {'type': 'boolean'}, 'content': {'type': 'string'}, 'likings_count': {'type': 'integer', 'format': 'int32'}, 'duration': {'type': 'integer', 'format': 'int32'}, 'type': {'enum': ['text', 'answer'], 'type': 'string'}, 'id': DefinitionsAnswer_id, 'voice_id': {'type': 'string'}, 'question_id': DefinitionsQuestion_id}}
DefinitionsQuestion = {'required': ['id', 'type', 'offer', 'status', 'content', 'account_id', 'respondent_id', 'date_created', 'date_updated'], 'properties': {'status': DefinitionsQuestion_status, 'account_id': DefinitionsId, 'offer': DefinitionsOffer, 'date_updated': DefinitionsDatetime, 'respondent_id': DefinitionsId, 'content': DefinitionsContent, 'date_created': DefinitionsDatetime, 'type': DefinitionsQuestion_type, 'id': DefinitionsQuestion_id}}
DefinitionsAnswerinpubliclist = {'properties': {'status': {'enum': ['rejected'], 'type': 'string'}, 'date_updated': DefinitionsDatetime, 'is_liked': {'type': 'boolean'}, 'content': {'type': 'string'}, 'likings_count': {'type': 'integer', 'format': 'int32'}, 'duration': {'type': 'integer', 'format': 'int32'}, 'id': DefinitionsAnswer_id, 'voice_id': {'type': 'string'}, 'question_id': DefinitionsQuestion_id}}
DefinitionsCreatequestionvisit = {'required': ['question_id'], 'properties': {'source': {'enum': ['share', 'fenda', 'free', 'bonus', 'talk'], 'type': 'string', 'description': u'\u542c\u7684\u6765\u6e90 \u4ed8\u8d39\u5077\u542c/\u597d\u53cb\u514d\u8d39\u542c/\u5206\u7b54\u95ee/\u9650\u514d\u542c/\u8d5e\u8d4f\u542c/\u8ba8\u8bba'}, 'question_id': DefinitionsQuestion_id, 'free_key': {'type': 'string'}, 'rewarder_id': {'type': 'integer', 'description': u'\u6253\u8d4f\u8005id'}}}
DefinitionsAccount = {'required': ['id', 'nickname', 'avatar'], 'properties': {'is_receive_image_question': {'type': 'boolean'}, 'title': DefinitionsTitle, 'introduction': DefinitionsIntroduction, 'nickname': {'minLength': 1, 'type': 'string', 'maxLength': 64}, 'price': {'type': 'integer', 'format': 'int32'}, 'tags': {'items': DefinitionsTaglite, 'type': 'array'}, 'followers_count': {'type': 'integer', 'format': 'int32'}, 'avatar': DefinitionsUrl, 'answers_count': {'type': 'integer', 'format': 'int32'}, 'id': DefinitionsId}}
DefinitionsSelfaskquestionwithansweroptional = {'required': ['id', 'offer', 'content', 'status', 'date_created'], 'description': u'\u6211\u95ee\u5217\u8868', 'properties': {'status': DefinitionsQuestion_status, 'respondent': DefinitionsAccountlite, 'offer': DefinitionsOffer, 'date_updated': DefinitionsDatetime, 'images_count': {'type': 'integer', 'format': 'int32'}, 'content': DefinitionsContent, 'date_created': DefinitionsDatetime, 'is_public': {'type': 'boolean'}, 'type': DefinitionsQuestion_type, 'id': DefinitionsQuestion_id}}
DefinitionsQuestionwithanswer = {'allOf': [DefinitionsQuestion, {'type': 'object'}], 'properties': {'free_type': {'type': 'string'}, 'discussions_count': {'type': 'integer', 'format': 'int32'}, 'respondent': DefinitionsAccountlite, 'is_sticky': {'type': 'boolean'}, 'asker': DefinitionsAccountlite, 'listenings_count': DefinitionsCount, 'images_count': {'type': 'integer', 'format': 'int32'}, 'remaining_seconds': {'type': 'integer', 'format': 'int32'}, 'is_free': {'type': 'boolean'}, 'answer': DefinitionsAnswerinpubliclist}, 'description': u'\u5df2\u7ecf\u56de\u7b54\u7684\u516c\u5f00\u7684\u95ee\u9898 \u6211\u56de\u7b54\u7684\u95ee\u9898\u5217\u8868'}
DefinitionsQuestionbeforeanswered = {'required': ['id', 'type', 'offer', 'status', 'content', 'account_id', 'respondent_id', 'date_created', 'date_updated'], 'properties': {'asker': DefinitionsAccountlite, 'respondent': DefinitionsAccountlite, 'images_count': {'type': 'integer', 'format': 'int32'}}, 'allOf': [DefinitionsQuestion, {'type': 'object'}]}
DefinitionsQuestiondetail = {'allOf': [DefinitionsQuestion, {'type': 'object'}], 'properties': {'free_type': {'type': 'string'}, 'is_enable_inquiry': {'type': 'boolean'}, 'listenings_count': DefinitionsCount, 'respondent': DefinitionsAccountlite, 'bonus': {'type': 'integer', 'description': u'\u5f53\u524d\u7528\u6237\u8d5e\u8d4f\u91d1\u989d', 'format': 'int32'}, 'topics': {'items': DefinitionsTopic, 'type': 'array'}, 'discussions_count': {'type': 'integer', 'format': 'int32'}, 'is_free': {'type': 'boolean'}, 'has_quota': {'type': 'boolean'}, 'is_enable_revoke': {'type': 'boolean'}, 'topic_short_title': {'type': 'string'}, 'is_public': {'type': 'boolean'}, 'refuse_reason': DefinitionsQuestionrefusereason, 'asker': DefinitionsAccountlite, 'has_discussions': {'type': 'boolean'}, 'images_count': {'type': 'integer', 'format': 'int32'}, 'bonuses': {'type': 'integer', 'description': u'\u88ab\u8d5e\u8d4f\u91d1\u989d', 'format': 'int32'}, 'remaining_seconds': {'type': 'integer', 'format': 'int32'}, 'answer': DefinitionsAnswer, 'visitor_count': DefinitionsCount}, 'description': u'\u81ea\u5df1\u63d0\u51fa\u7684\u95ee\u9898\u624d\u53ef\u8c03\u7528'}
DefinitionsAnswerwithvoiceurl = {'properties': {'voice_url': {'type': 'string'}}, 'allOf': [DefinitionsAnswer, {'type': 'object'}]}
DefinitionsTenantquestion = {'allOf': [{'type': 'object'}, DefinitionsQuestionwithanswer]}

validators = {
    ('games', 'POST'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'json': DefinitionsCreatelarpgame},
    ('games', 'GET'): {'headers': {'required': ['Authorization'], 'properties': {'Authorization': {'type': 'string'}}}, 'args': {'required': [], 'properties': {'per_page': {'description': 'per_page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'limit': {'description': 'limit number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 100}, 'page': {'description': 'page number', 'format': 'int32', 'required': False, 'type': 'integer', 'maximum': 10000}, 'offset': {'description': 'offset number', 'format': 'int32', 'required': False, 'type': 'integer'}}}},
}

filters = {
    ('games', 'POST'): {201: {'headers': None, 'schema': DefinitionsLarpgame}},
    ('games', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsLarpgame, 'type': 'array'}}},
}

scopes = {
    ('games', 'POST'): ['panel'],
    ('games', 'GET'): ['panel'],
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

