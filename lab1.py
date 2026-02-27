import argparse

def read_numbers_from_file(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', nargs='*', type=int)
    parser.add_argument('-f')
    parser.add_argument('-o')
    args = parser.parse_args()

    if args.f:
        numbers = read_numbers_from_file(args.f)
    else:
        numbers = args.numbers

    total = sum(numbers)

    if args.o:
        with open(args.o, 'w') as f:
            f.write(str(total))
    else:
        print(total)

if __name__ == '__main__':
    main()
