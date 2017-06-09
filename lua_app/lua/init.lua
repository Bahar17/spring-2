local ngx = ngx
local R = require('lua.gytre.router')
local assert = assert
local io_open = io.open
local routers = require('lua.routers')
local ipairs = ipairs
local settings = require('lua.my_settings')

-- load router
local _R = R:new()

for _, tree in ipairs(routers) do
    for _, router in ipairs(tree[2]) do
        _R:Register(tree[1], router[1], router[2])
    end
end
-- 全局变量Router
Router = _R
ngx.log(ngx.ERR, "=======finish Router initial=======")

-- load rsa key --
local function read_files(fileName)
    local f = assert(io_open(fileName,'r'))
    local content = f:read("*all")
    f:close()
    return content
end
local path = settings.rsa_keys_path
local share_data = ngx.shared.share_data
share_data:set('RSA_PUB_KEY', read_files(path .. settings.pub_key_name))
share_data:set('RSA_PRIV_KEY', read_files(path .. settings.priv_key_name))
share_data:set('JWT_SECRET_KEY', settings.JWT_SECRET_KEY)
share_data:set('JWT_TTL', settings.JWT_TTL)
share_data:set('JWT_REFRESH_TTL', settings.JWT_REFRESH_TTL)
share_data:set('JWT_ALGORITHM', settings.JWT_ALGORITHM)

ngx.log(ngx.ERR, "=======finish jwt keys initial=======")
