# Artists API

A small Django application to retrieve artists information.

## How to run

You need to have [Docker](https://www.docker.com/) installed.

Then, clone this repository:

```
git clone https://github.com/manugrandio/artists-api.git
```

Change directory:

```
cd artists-api
```

Build the project (this will build the image, install dependencies, run migrations and create some sample data for you to test):

```
docker build -t artists-api .
```

Run the application with:

```
docker run -it --rm -p 8000:8000 --name running-artists-api artists-api
```

If you want, you can also download the artist images so that the endpoint responses include links to them:

```
docker exec -it running-artists-api python manage.py get_artists_images
```

## Manual testing

The build command creates a user whose credentials are:

- user: `user`
- password: `password`

So you can use it to make requests to endpoints that need authentication.

### API usage examples

Get list of artists:

```
curl localhost:8000/artists/ | python -m json.tool
```

Get list of albums:

```
curl localhost:8000/albums/ -u user:password | python -m json.tool
```

Get an artist albums:

```
curl localhost:8000/artists/1/albums/ -u user:password | python -m json.tool
```

Get list of albums with details:

```
curl localhost:8000/albums-details/ -u user:password | python -m json.tool
```

Get number of valid basic passphrases:

```
curl -X POST localhost:8000/passphrase/basic/ -H "Content-Type: application/json" --data '{"passphrases":"aa bb cc\naa bb dd"}' -u user:password | python -m json.tool
```

Get number of valid advanced passphrases:

```
curl -X POST localhost:8000/passphrase/advanced/ -H "Content-Type: application/json" --data '{"passphrases":"asd dsa\nhello world"}' -u user:password | python -m json.tool
```

## Project shortcomings

- For simplicity, it uses the development server and SQLite.
In a production environment I would use a real server such as Nginx and a more powerful database such as PostgreSQL.
- It stores and serves media files in a way that is only suitable for development.
I couldn't figure out how to do it with Django REST Framework the proper way (but I think I could fix it if I had some more time).
- I think the project has a pretty good test coverage overall.
For simplicity, the two missing pieces that lack automated tests are the `get_artists_images` command and the `Scrapper`.
In a production scenario I would write tests for those classes too.
- For simplicity, I used `FileField` to store images instead `ImageField` because it didn't provide any functionality I needed for this exercise.
In a production scenario, I would use `ImageField`, though.
- Passphrase logic is in `utils`.
I didn't create an app because I didn't need models, just the views.
- I didn't implement the "Extra points" section (S3 usage and different development and production environments).
