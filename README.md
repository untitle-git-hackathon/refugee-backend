# Refugees

## API Scheme

- `GET /refugees`

```json
[
    {
        "id": 0,
        "name": "",
        "location_id": 0
    }
]
```

- `GET /stories/{refugee_id}`

```json
[
    {
        "message": "test message",
        "image_src": "",
    }
]
```

- `GET /location/{id}`

```json
{
    "name": "",
    "description": "",
    "url": "",
}
```