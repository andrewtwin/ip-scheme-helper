import ipaddress
import argparse


def main():
    parser = argparse.ArgumentParser(description="Subnet a network.")
    parser.add_argument(
        "network", type=str, help="Network to subnet.",
    )
    parser.add_argument(
        "-m", "--max-prefix",
        type=int,
        default=25,
        help="Maximum prefix length.",
    )
    parser.add_argument(
        "-c", "--indent-char",
        default=" ",
        help="Characters to use for indentation.",
    )

    args = parser.parse_args()
    parent_network = ipaddress.ip_network(args.network)

    if args.max_prefix < parent_network.prefixlen:
        exit(f"Network prefix {args.max_prefix} already beyond max prefix length {parent_network.prefixlen}")

    print(parent_network)
    get_subnets(parent_network, depth=args.max_prefix, indent_char=args.indent_char)


def get_subnets(ip_network, indent="", indent_char=" ", depth=32):
    indent = indent + indent_char

    for network in ip_network.subnets(1):
        print(f"{indent}{network}")
        if network.prefixlen < depth:
            get_subnets(network, depth=depth, indent=indent, indent_char=indent_char)


if __name__ == "__main__":
    main()
