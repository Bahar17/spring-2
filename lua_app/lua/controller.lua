-- 这里面做路由，选择model，controlor，view

-- config
local base_package = { 'views', 'lua' }

local require = require
local ngx = ngx
local string_lower = string.lower
local string_gsub = string.gsub
local table_insert = table.insert
local table_concat = table.concat
local Router = Router
local uri = ngx.var.uri
local uris = {}
string_gsub(uri, '[^/]+', function(w) table_insert(uris, w) end)
if uris[1] ~= base_package[1] then
    ngx.log(ngx.ERR, ngx.var.uri ..
            ' has no this package:' .. base_package[2])
    ngx.exit(ngx.HTTP_NOT_FOUND)
end

local sub_path = '/' .. table_concat(uris, '/', 2)
local handle, p, tsr = Router:GetHandle(base_package[1], sub_path)
if handle then
    local handler = require(base_package[2] .. '.' .. handle)
    local method = string_lower(ngx.req.get_method())
    handler:Handle(method, p)
else
    ngx.log(ngx.ERR, ngx.var.uri ..
            ' not found handle:' .. base_package[2])
    ngx.exit(ngx.HTTP_NOT_FOUND)
end