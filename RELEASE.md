Release type: minor

The default resolver is now able to resolve dictionaries as well as objects.

For example, if you have the following type:

```py
@strawberry.type
class User:
    id: strawberry.ID
    name: str
```

The following query will work:

```py
@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return {"id": 1, "name": "Rick Astley"}
```

This does not introduce any breaking changes.
