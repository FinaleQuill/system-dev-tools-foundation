import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    args = parser.parse_args()

    if not args.name.strip():
        parser.error("--name must contain non-whitespace characters")

    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
