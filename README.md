## Short Link Api

###### -- create
POST  /api/1.0/short_links
<br>
request
<br>
{

    link: https://someurl.com/,
    days_actual: 16
}
<br>
response, `201`
<br>
{

    id: 1, 
    default_url: https://someurl.com/, 
    short_url: http://127.0.0.1:5000/cjy6s, 
    days_actual: 16
    
}
<br>
<br>
`link` - link to shorten
<br>
`days_actual` - number of days the link will be available, must be between 1 and 366
<br>
<br>
###### -- get instance
GET  /api/1.0/short_links/1
<br>
request
<br>
{
}
<br>
response, `200`
<br>
{

    id: 1, 
    default_url: https://someurl.com/, 
    short_url: http://127.0.0.1:5000/cjy6s, 
    days_actual: 16
    
}
<br>
###### -- edit instance
PUT  /api/1.0/short_links/1
<br>
request
<br>
{

    default_url: https://someurl/somepage.com/, 
    days_actual: 300
}
<br>
response, `204`
<br>
{
}
<br>
###### -- delete instance
PUT  /api/1.0/short_links/1
<br>
request
<br>
{
}
<br>
response, `204`
<br>
{
}
<br>

## Setup

create database
<br>
`python manage.py db_startup`
<br>

run app
<br>
`python manage.py`
