import ipaddress
import argparse


def main():
    parser = argparse.ArgumentParser(description="Subnet a network.")
    parser.add_argument(
        "network", type=str, help="Network to subnet.",
    )
    parser.add_argument(
        "-m",
        "--max-prefix",
        dest="max_prefix",
        type=int,
        default=25,
        help="Maximum prefix length.",
    )
    parser.add_argument(
        "-c",
        "--indent-char",
        dest="indent",
        type=str,
        default=" ",
        help="Characters to use for indentation.",
    )

    args = parser.parse_args()
    max_prefix = args.max_prefix
    indent_char = args.indent
    parent_network = ipaddress.ip_network(args.network)

    print(f"{parent_network}")
    get_subnets(parent_network, depth=max_prefix, indent_char=indent_char)


def get_subnets(ip_network, **options):
    start = ip_network

    indent_char = options.get("indent_char")
    if indent_char is None:
        indent = " "

    indent = options.get("indent")
    if indent is None:
        indent = ""

    indent = indent + indent_char

    max_prefix = options.get("depth")
    if max_prefix is None:
        max_prefix = 32
    else:
        max_prefix = int(max_prefix)

    if max_prefix < start.prefixlen:
        print(
            f"Network prefix {start.prefixlen} already beyond max prefix length {max_prefix}"
        )
        exit(1)

    for network in start.subnets(1):
        print(f"{indent}{network}")
        if network.prefixlen < max_prefix:
            get_subnets(
                network, depth=max_prefix, indent=indent, indent_char=indent_char
            )


if __name__ == "__main__":
    main()
