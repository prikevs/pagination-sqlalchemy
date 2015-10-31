# Alternative-for-Flask-SQLAlchemy-Pagination
Alternative for flask-sqlalchemy pagination based on plain sqlalchemy

## Motivation
*   I am developing a project used to update, build and test Chromium project automatically. My project is using SQLAlchemy to manage the database, and I need to develop a website to show the running status. I chose to use Flask as the web framework and Flask-Bootstrap as the frontend frame. But the Flask-Bootstrap's pagination macro only accepts Flask-SQLAlchemy's pagination object. So I read its source code and combine the `Class Pagination` with [ahmadjavedse](https://github.com/ahmadjavedse)'s project [sqlalchemy-paginator](https://github.com/ahmadjavedse/sqlalchemy-paginator). Thanks for your contribution.

## Based on
*   [SQLAlchemy](http://http://www.sqlalchemy.org/)
*   [sqlalchemy-paginator](https://github.com/ahmadjavedse/sqlalchemy-paginator)

## Usage
*   Trandition usage of flask-sqlalchemy's pagiantion
```python
pagination = Modelname.query...paginate(page,per_page=PER_PAGE)
```

*   This alternative usage:
```python
from mypaginator import pager 
# just a query object
query = Session.query(Modelname)...
mypagination = pager(query, page, PER_PAGE)
```
*   Now you can pass mypagination to the template, it has the same methods as `pagination` above.

