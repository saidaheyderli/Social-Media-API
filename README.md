# SocialMedia API

## About the Project
This project is a Blog and Comment management system built using Django REST Framework.

The current version focuses on:
- Retrieving full details for specific entities
- Implementing clean error handling for non-existent objects

---

## Features

- List Posts (newest first)
- List Post previews (lightweight response)
- Create Post (Swagger documented)
- List Comments (most liked first)
- Retrieve single Post by ID
- Retrieve single Comment by ID
- Clean 404 handling

The API returns:
{
  "detail": "Not found."
}

when the requested object does not exist.

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Swagger UI (drf-yasg)
- SQLite (Default)
