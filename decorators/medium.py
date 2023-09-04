
def permission_checker(permissions):
    def decorator(func):
        def wrapper(user):
            user_permissions = {
                "user1": ["read", "write"],
                "user2": ["read"],
                "user3": ["write"],
            }
            if user in user_permissions:
                users_permissions = user_permissions[user]
                for permission in permissions:
                    if permission not in users_permissions:
                        raise PermissionError(f"User {user} does not have permission {permission}")
                return func(user)
            else:
                raise PermissionError(f"User {user} does not exist")
        return wrapper
    return decorator

@permission_checker(["read", "write"])
def secure_function(user):
    print(f"Secure data for {user}")
    return

secure_function("user1")  # Should execute successfully
secure_function("user2")  # Should raise a PermissionError
