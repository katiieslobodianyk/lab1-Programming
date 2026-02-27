import typer

app = typer.Typer()

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    numbers = []
    for line in lines:
        if line.strip():
            numbers.append(int(line.strip()))
    return numbers

@app.command()
def main(
    numbers: list = typer.Argument(None, help="Числа для додавання"),
    file: str = typer.Option(None, "-f", help="Файл з числами"),
    output: str = typer.Option(None, "-o", help="Файл для результату")
):
    if file:
        nums = read_file(file)
    else:
        nums = numbers or []

    total = sum(nums)

    if output:
        with open(output, "w") as f:
            f.write(str(total))
        print(f"Сума {total} записана у файл {output}")
    else:
        print(total)

if __name__ == "__main__":
    app()
