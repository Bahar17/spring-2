local rsa = require("lua.gytre.rsa")

local key_name = 'spring'
if key_name == nil then
    error('need a key name')
end

local util = require('lua.gytre.util')
local my_settings = require('lua.my_settings')
local settings = require('lua.settings')
util.table_merge(settings, my_settings)

local error = error


local rsa_public_key, rsa_priv_key, err = rsa:generate_rsa_keys(2048)
if not rsa_public_key then
    error('generate rsa keys err: ', err)
end
local path = settings.rsa_keys_path

local public_file = io.open(path .. settings.pub_key_name, "r")
if public_file then
    error('rsa keys already exits')
end

local public_file = io.open(path .. settings.pub_key_name, "w")
public_file:write(rsa_public_key)
public_file:close()


local private_file = io.open(path .. settings.priv_key_name, "w")
private_file:write(rsa_priv_key)
private_file:close()

