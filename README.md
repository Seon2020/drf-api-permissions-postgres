# drf-api-permissions-postgres
## Lab 32-34
#### Most Recent PR: https://github.com/Seon2020/drf-api-permissions-postgres/pull/3
#### DEPLOYED URL: http://18.221.170.219:8000/api/v1/hot_100s/. 



- Check snippets file for proof of boilerplate.

#### Include steps to manually test using httpie:
- run poetry add httpie
- run docker-compose up -d
- run docker-compose run web python manage.py migrate 
- Ensure you have superuser created 
- run http post localhost:8000/api/token/ username="enter username no quotes" password="enter password no quotes" 
- copy token 
- run http :8000/api/v1/"insert app name"/ 'Authorization: Bearer "paste token here no quotes"' 
- make sure you get data
