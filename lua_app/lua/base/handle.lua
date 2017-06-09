local ngx = ngx
local pcall = pcall
local setmetatable = setmetatable

local _H = {}

function _H:new(o)
    o = o or {}
    self.__index = self
    setmetatable(o, self)
    return o
end

function _H:Handle(method, params)
    if self[method] then
        pcall(self[method], self, params)
    else
        ngx.log(ngx.ERR, ngx.var.uri ..
                ' not allowed method:' .. ngx.req.get_method())
        ngx.exit(ngx.HTTP_NOT_ALLOWED)
    end
end

return _H