## Link shortener project backend repository.

If you want to change SHORT_LINK_LENGTH after migration:
at a longer value then change SHORT_LINK_LENGTH and run the following commands in the container:
```
python manage.py makemigrations link
python manage.py migrate link
```

at a shorter value then you need change short_link field in ShortLink model. Change max_length=settings.SHORT_LINK_LENGTH to max_length=value of SHORT_LINK_LENGTH. After this change SHORT_LINK_LENGTH in .env.dev. This ensures backward compatibility. 
