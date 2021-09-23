from password_gen.password_generator import PasswordGenerator


def password_from_config_file(config) -> str:

    with open(config, 'rt') as f:
        config_file = f.read()

    pgen = PasswordGenerator(config_file)
    password = pgen.new()

    return password
