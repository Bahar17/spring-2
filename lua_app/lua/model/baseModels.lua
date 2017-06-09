--
-- Created by IntelliJ IDEA.
-- User: legenove
-- Date: 17/5/24
-- Time: 下午8:38
-- To change this template use File | Settings | File Templates.
--

--local baseModel = require("lua.model.baseModels")
--local panelModel = baseModel:new(nil, {port=8000 })
--
--
--local options = {path='/panel',args="a=1&b=2"}
--options.success = function(res)
--    ngx.say(res.body)
--end
--options.fail = function(res)
--end
--
--
--panelModel:request(options)

local ngx = ngx
local type = type
local require = require
local setmetatable = setmetatable
local string_format = string.format
local string_upper = string.upper



local http = require("resty.http")

local BaseModel = {protocal = "http", host = "0.0.0.0", port = "8080", timeout=2000}

function BaseModel:new(o, args)
    o = o or {}
    args = args or {}
    self.__index = self
    setmetatable(o, self)
    local host = args.host
    local port = args.port
    if host then
        o.host = host
    end
    if port then
        o.port = port
    end
    return o
end

function BaseModel:set_protocal (protocal)
    self.protocal = protocal
end

function BaseModel:set_host (host)
    self.host = host
end

function BaseModel:set_port (port)
    self.port = port
end

function BaseModel:set_timeout (timeout)
    self.timeout = timeout
end

function BaseModel:get_host(path, args)
    return string_format(
        "%s://%s:%s%s?%s",
        self.protocal,
        self.host,
        self.port,
        path,
        args
    )
end

function BaseModel:is_https()
    return self.protocal == 'https'
end

function BaseModel:request(options)
    --[[
    options:
        param: path
        param: args
        param: headers
        param: authorization
        param: method
        param: body
        param: success
        param: fail
    ]]

    options = options or {}
    local authorization = options.authorization or 'Basic d3hhcHA6ZDQyeURpa0o4aXJjVDZHQjlxcktKOTZzVzJFOXBoRTI=';
    local headers = options.headers or {}
    headers["Authorization"] = authorization
    local url = self:get_host(options.path or '/', options.args or '')
    local httpc = http.new()
    local method =  string_upper(options.method or 'get')
    local res, err = httpc:request_uri(url, {
        method =  method,
        body = options.body or "",
        headers = headers
    })
    if not res then
        ngx.log(ngx.ERR, "*[LuaAPI]* %s %s TCP request  error"%
                method, url)
        ngx.exit(500)
        return
    end

    if res.status >= 200 and res.status < 400 then
        if type(options.success) == 'function' then
            options.success(res)
        else
            ngx.log(ngx.ERR,'no success callback')
            ngx.exit(500)
        end
    else
        if type(options.fail) == 'function' then
            options.fail(res)
        else
            ngx.log(ngx.ERR,'no fail callback')
            ngx.exit(500)
        end
    end

end

return BaseModel