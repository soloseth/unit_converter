import argparse
from core import convert


def main():
    parser = argparse.ArgumentParser(
        description="Unit Converter CLI Tool"
    )

    parser.add_argument("value", type=float, help="Numeric value to convert")
    parser.add_argument("from_unit", type=str, help="Unit to convert from")
    parser.add_argument("to_unit", type=str, help="Unit to convert to")

    args = parser.parse_args()

    try:
        result = convert(args.value, args.from_unit, args.to_unit)
        print(f"{args.value} {args.from_unit} = {result:.4f} {args.to_unit}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
