# Fampay Backend Assignment

# Project Goal 

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Search query: Cricket

# Basic Requirements (Covered):

- Server calls the YouTube API continuously in background (async) with an interval of 10 seconds for fetching the latest Cricket videos  and stores the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs  in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Dockerized the project.
- Project is scalable and optimised.

# Bonus Points (Covered):

- Added support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- Made a dashboard to view the stored videos with filters and sorting options.

# Setup and Test Instructions
1. `docker-compose up -d --build `
2. a. Visit `http://localhost:1337/videos` in the browser.
2. b. Click on the `Filter` button (in the top right) for search and sorting options.   
3. `docker ps` for running containers.
4. `docker-compose exec web python manage.py shell` for Django shell access.
5. `docker-compose logs -f 'celery'` for checking Celery logs.
6. `docker-compose exec db psql --username=hello_django --dbname=hello_django_dev` for checking Postgres DB.
