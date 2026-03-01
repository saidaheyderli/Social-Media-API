SocialMedia API :
About the Project:
This project is a Blog and Comment management system built using Django REST Framework. The current version  focuses on retrieving full details for specific entities and implementing clean error handling for non-existent objects.

Features
List Posts (newest first)
List Post previews (lightweight response)
Create Post (Swagger documented)
List Comments (most liked first)
Retrieve single Post by ID
Retrieve single Comment by ID
Clean 404 response for non-existent objects
Clean 404 Handling: The API returns a proper 404 NOT FOUND response (with { "detail": "Not found." }) when the requested object does not exist.

Tech Stack:
Backend: Python, Django, Django REST Framework
Documentation: Swagger UI (drf-yasg)
Database: SQLite (Default)
