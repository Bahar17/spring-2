--
-- Created by IntelliJ IDEA.
-- User: legenove
-- Date: 17/6/9
-- Time: 下午5:54
-- To change this template use File | Settings | File Templates.
--

local settings = {
    rsa_keys_path = '',
    pub_key_name = '/.pem',
    priv_key_name = '/.pem',
    JWT_SECRET_KEY = 'secret_key',
    JWT_TTL = '60',
    JWT_REFRESH_TTL = '30240',
    JWT_ALGORITHM = 'HS256',
}

return settings