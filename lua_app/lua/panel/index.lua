local require = require
local ngx = ngx
local _o = {

}
local baseHandle = require('lua.base.handle')
local _H = baseHandle:new(_o)
function _H:get()
    ngx.say('hello world')
end

return _H
