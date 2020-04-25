# user.py

if user.find_by_username(data['username']):
    return {"message": "A user with that username already exists"}, 400
