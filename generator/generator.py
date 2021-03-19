def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row # instead of return row

file_generator = csv_reader("example_file.txt")

for row in file_generator:
    # csv_reader is suspended until next loop
    parts = row.split(",")
    print(f"{parts[0]}:{parts[1]}")

