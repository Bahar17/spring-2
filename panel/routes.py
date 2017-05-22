# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.places_place_id import PlacesPlaceId
from .api.games_id import GamesId
from .api.games import Games
from .api.games_id_places import GamesIdPlaces
from .api.professions_id import ProfessionsId
from .api.professions import Professions
from .api.games_id_roles import GamesIdRoles
from .api.roles_role_id import RolesRoleId


url_prefix = 'panel'

routes = [
    dict(resource=PlacesPlaceId, urls=[r"/places/(?P<place_id>[^/]+?)"], endpoint='places_place_id'),
    dict(resource=GamesId, urls=[r"/games/(?P<id>[^/]+?)"], endpoint='games_id'),
    dict(resource=Games, urls=[r"/games"], endpoint='games'),
    dict(resource=GamesIdPlaces, urls=[r"/games/(?P<id>[^/]+?)/places"], endpoint='games_id_places'),
    dict(resource=ProfessionsId, urls=[r"/professions/(?P<id>[^/]+?)"], endpoint='professions_id'),
    dict(resource=Professions, urls=[r"/professions"], endpoint='professions'),
    dict(resource=GamesIdRoles, urls=[r"/games/(?P<id>[^/]+?)/roles"], endpoint='games_id_roles'),
    dict(resource=RolesRoleId, urls=[r"/roles/(?P<role_id>[^/]+?)"], endpoint='roles_role_id'),
]

def load_uris(config):
    try:
        config.update_uri(routes, url_prefix)
    except:
        pass