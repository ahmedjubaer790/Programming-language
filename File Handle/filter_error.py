import re

input_file = "D:\\Python Prc & Environment\\python\\File Handle\\server.log"
output_file = "errors.log"

# লাইনের ফরম্যাট: DATE TIME LEVEL MESSAGE
# শুধু LEVEL জায়গায় ERROR থাকলে মিলবে
pattern = re.compile(r"^\S+\s+\S+\s+ERROR\b")

count = 0
try:
    with open(input_file, "r", encoding="utf-8", errors="replace") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            if pattern.search(line):
                outfile.write(line)
                count += 1
    print(f"Done! {count}  ERROR ms '{output_file}' file is sved")

except FileNotFoundError:
    print(f"Error: '{input_file}'cant find it")