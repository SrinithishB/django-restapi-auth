Here are the endpoints:

1. `logout/`
2. `forgotpass/`
3. `resetpass/<uidb64>/<token>/`
4. `createuser/`
5. `token/`
6. `token/refresh/`

### 1. Logout

For a logout endpoint, you typically only need the refresh token to invalidate it.

#### Example JSON Request:
```json
{
    "refresh": "your_refresh_token_here"
}
```

### 2. Forgot Password

For the forgot password endpoint, you'll usually provide the user's email address.

#### Example JSON Request:
```json
{
    "email": "user@example.com"
}
```

### 3. Reset Password

For the reset password endpoint, you'll provide the new password. This URL also requires `uidb64` and `token` parameters in the URL.

#### Example URL:
```
http://localhost:8000/api/resetpass/<uidb64>/<token>/
```

#### Example JSON Request:
```json
{
    "password": "new_password"
}
```

### 4. Create User

For creating a new user, you need to provide the necessary user details like username, email, and password.

#### Example JSON Request:
```json
{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "newpassword"
}
```

### 5. Obtain Token

To obtain a JWT token, you'll need to provide the username and password.

#### Example JSON Request:
```json
{
    "username": "user",
    "password": "password"
}
```

### 6. Refresh Token

To refresh an access token, you'll need to provide the refresh token.

#### Example JSON Request:
```json
{
    "refresh": "your_refresh_token_here"
}
```

### Summary of JSON Request Bodies:

Here's a summary of all the request bodies in one place:

```json
{
    "logout": {
        "refresh": "your_refresh_token_here"
    },
    "forgotpass": {
        "email": "user@example.com"
    },
    "resetpass": {
        "password": "new_password"
    },
    "createuser": {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "newpassword"
    },
    "token": {
        "username": "user",
        "password": "password"
    },
    "token_refresh": {
        "refresh": "your_refresh_token_here"
    }
}
