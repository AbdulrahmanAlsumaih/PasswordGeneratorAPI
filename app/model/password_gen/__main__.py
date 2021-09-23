from password_gen.password_generator import PasswordGenerator
import sys


def password_command(arg1):
    with open(arg1, 'rt') as f:
        config_file = f.read()
    password = PasswordGenerator(config_file)

    print(password.new())


def main():
    arg1 = sys.argv[1]
    password_command(arg1)


if __name__ == "__main__":
    main()
