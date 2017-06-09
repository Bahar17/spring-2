local cjson = require("cjson")
local crypto = require("crypto")
local os_time = os.time
local ngx_b64_encode = ngx.encode_base64
local ngx_b64_decode = ngx.decode_base64
local hmac = require("crypto.hmac")

local ret = hmac.digest("sha256", "abcdefg", "hmackey")

print(ret)

local a = { a = 100, b = '123' }
local b = { b = '123', a = 100 }

local function table_dict_sort(dict)
    local keys = {}
    local res = {}
    for i in pairs(dict) do
        table.insert(keys, i)
    end
    table.sort(keys)
    for i,v in pairs(keys) do
       res[v]=dict[v]
    end
    return res
end

--lua table 拷贝
local function table_copy_table(ori_tab)
    if (type(ori_tab) ~= "table") then
        return nil
    end
    local new_tab = {}
    for i,v in pairs(ori_tab) do
        local vtyp = type(v)
        if (vtyp == "table") then
            new_tab[i] = table_copy_table(v)
        elseif (vtyp == "thread") then
            new_tab[i] = v
        elseif (vtyp == "userdata") then
            new_tab[i] = v
        else
            new_tab[i] = v
        end
    end
    return new_tab
end

local c = table_copy_table(b)
b['d'] = 3843
c['c'] = 'kdjf'

print(cjson.encode(a))
print(cjson.encode(b))
print(cjson.encode(c))
