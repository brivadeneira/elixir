# Elixir
Proof of concept for the development of a bar API.

> it is an API that provides cocktails and beers.

[![](https://media1.giphy.com/media/ylzObgDRgAI9JpFgOU/giphy.gif)](https://www.youtube.com/embed/LiZIKRgYXxU?si=p7PjcLcZMoYLTOaL)

*Elixir reference*

## How to run

```sh
~$ git clone https://github.com/brivadeneira/elixir.git
~$ cd elixir
```

### docker container

- Clone this repo, build and run the docker image:

```sh
~$ docker build -t elixir .
~$ docker run -p 80:80 elixir
```

- Look for the local IP *(`ip addr` could be useful)*

### locally
```sh
~$ pip install -r requirements.txt
~$ python main.py
```

## How to use

- with the base URL: `<IP>`:80
  - `IP`: `127.0.0.1` running locally, local IP running with docker
- Request drinks thorugh the endpoints:
    - `/beer`: returns a random beer
    - `/cocktail`: returns a random cocktail
    - `/suggestion`: returns a beer during daytime or a cocktail with the first name of the user during the night
    - `/docs`: for more info

## Test
```sh
~$ pip install -r dev-requirements.txt
~$ pytest .
```

## Design comments

### Models
       +--------------+
       |    User      |
       +--------------+
       | name: str    |
       | timezone: str|
       +--------------+

- The user object is mocked and injected the [Random User API](https://randomuser.me/api/)

                +----------------+
                |     Drink      |
                +----------------+
                | - name: str    |
                | - tagline: str |
                +----------------+
                       ^
                       |
                       |
               +-------+--------+
               |                |
        +---------------+    +----------------+
        |    Beer       |    |    Cocktail    |
        +---------------+    +----------------+
        | - abv: float  |    | - ingredients: |
        | - ibu: int    |    |   list[str]    |
        | - food_pairing:    | - instructions:|
        |   list[str]   |    |   str          |
        +---------------+    +----------------+
- For symplicity, beers and cocktails are generated using the `factory-boy` lib.
  - *You can find funny combinations!*
