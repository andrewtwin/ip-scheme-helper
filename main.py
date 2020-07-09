import ipaddress


def main():
    max_prefix = 24
    indent_char = ","
    parent_network = ipaddress.ip_network("192.168.0.0/16")
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
