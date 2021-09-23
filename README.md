# PasswordGeneratorAPI

PasswordGeneratorAPI is REST API using FastAPI to generate random passwords that meet requirements that the user defines in POST requests.

## Installation

Install docker in your machine [docker](https://docs.docker.com/get-docker/). Please
visit the website for more information.

Install Docker Compose in your machine [Docker Compose](https://docs.docker.com/compose/
install/). Please visit the website for more information.

- after install docker and Docker Compose, run this command

```bash
docker compose up
```

## Usage

```json
{
  "length": 12,

  "allowed_characters": {
    "groups": {
      "special": "!@#$%&*()[]{}"
    },
    "constants": {
      "lowercase": "ascii_lowercase",
      "uppercase": "ascii_uppercase",
      "numbers": "digits"
    }
  },

  "required_characters": [
    [1, "group", "special"],
    [2, "constant", "uppercase"],
    [2, "constant", "lowercase"],
    [2, "constant", "numbers"]
  ],

  "violations": {
    "consecutive": 2,
    "occurrence": 2,
    "sequential": [
      [3, "constant", "numbers"],
      [3, "constant", "uppercase"],
      [3, "constant", "lowercase"]
    ],
    "verboten": ["password", "topsecret", "foobar", "spam"]
  }
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
