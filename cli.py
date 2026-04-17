import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Simple CLI Password Manager")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list")

    add = sub.add_parser("add")
    add.add_argument("name")
    add.add_argument("username")
    add.add_argument("password")
    get = sub.add_parser("get")
    get.add_argument("name")

    return parser.parse_args()