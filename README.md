# Refugees
## 어떻게 실행하나요?

`docker-compose up`

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
	"is_from_refugee": true,
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

- `GET /qa/{message_id}`

```json
{
    "correct_answer_image": "",
    "wrong_answer_image": "",
}
