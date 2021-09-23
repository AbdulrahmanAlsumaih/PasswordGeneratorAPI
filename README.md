# PasswordGeneratorAPI

PasswordGeneratorAPI is REST API using FastAPI to generate random passwords that meet requirements that the user defines in POST requests.

## Installation

Install docker in your machine [docker](https://docs.docker.com/get-docker/). Please
visit the website for more information.

Install Docker Compose in your machine [Docker_Compose](https://docs.docker.com/compose/
install/). Please visit the website for more information.

- clone the project and run this command where Docker-Compose.yml at

```bash
docker compose up
```

## Usage

The json file define the user requirement. Here is a breakdown of the full structure of the JSON object:

```json
{
    "length": int,

    "allowed_characters": {
        "groups": {
            string: string,
            string: string,
            etc...
        },
        "constants": {
            string: string,
            string: string,
            etc...
        }
    },

    "required_characters" : [
        [int, string, string],
        [int, string, string],
        etc...
    ],

    "violations" : {
        "consecutive": int,
        "occurrence": int,
        "sequential": [
            [int, string, string],
            [int, string, string],
            etc...
        ],
        "verboten": [
            string,
            string,
            etc...
        ]
    }
}
```

Here are a few more notes on some of the subsections:

### `length`

This is optional, and a default value provided by the
application is `8`

### `allowed_characters`

This section is a mapping that can have two keys: `"groups"` and `"constants"`.

For an explanation of the values found in the `"constants"` section, see:
[Python - string - String constants](https://docs.python.org/3/library/string.
html#string-constants)

### `required_characters` and `violations`

The `[int, string, string]` pattern is always `[count, group_type, group]`. The
`group_type` will always be either `group` or `constant`, with the same meanings
of those terms as is found in the `allowed_characters` section.

If some element of the `violations` section is not provided in the POST request,
or if it is defined as `null`, that element has no rule to enforce.

### Here's an example of a `violations` section.

In plain English, here are some example violation requirements.

    A password may not contain:
    * A single character repeated 2 or more times consecutively
    * A single character that occurs 4 or more times
    * A series of sequential numbers (0-9) that is 3 or more characters long and
      was provided in the "groups" mapping of the "allowed_characters" requirement.
         ("123" is wrong, "765" is wrong, "465" is OK)
    * The substring "password"

In the POST request, these would be defined:

```json
{
    ...,
    "violations" :{
        "consecutive": 2,
        "occurrence":4,
        "sequential": [
            [3, "group", "numbers"]
        ],
        "verboten":[
            "password"
        ]
    }
}
```

## Example

Here is an example to construct Json file from user requirement

```json
{
  "allowed_characters": {
    "groups": {
      "numbers": "0123456789",
      "lowercase": "abcdefghijklmnopqrstuvwxyz",
      "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    }
  },

  "required_characters": [
    [2, "group", "numbers"],
    [1, "group", "uppercase"]
  ],

  "violations": {
    "consecutive": 2,
    "occurrence": 3,
    "verboten": ["password", "topsecret", "foobar", "spam"]
  }
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
