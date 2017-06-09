local require = require
local template = require("resty.template")
local _o = {

}
local baseHandle = require('lua.base.handle')
local _H = baseHandle:new(_o)
function _H:get()
    template.render("t1.html")
end

return _H
