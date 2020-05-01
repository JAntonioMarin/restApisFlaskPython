# Postman

# Manage Environments url = 127.0.0.1
# Then in the get use {{url}}

# jwt_token = token
# {{jwt_token}}

# Test part
# JS Test

# Test for auth

# var jsonData = JSON.parse(responseBody);
# test["Access token was not empty"] = jsonData.access_token !== undefined;
#
# postman.setEnvironmentVariable("jwt_token", jsonData.access_token);

# Test for /items

# test["Response time is less than 200ms" = responseTime < 200;
# test["Status code is 201"] = responseCode.code === 201;
