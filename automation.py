import os
from datetime import datetime

folder = "sample_files"
log_file = "log.txt"

try:
    if not os.path.exists(folder):
        os.mkdir(folder)

    with open(log_file, "w") as log:
        log.write("Automation Script Log\n")
        log.write("=====================\n")

        for i in range(1, 6):
            filename = os.path.join(folder, f"file{i}.txt")

            with open(filename, "w") as f:
                f.write(f"This is file number {i}\n")

            log.write(f"{filename} created at {datetime.now()}\n")

    print("Files created successfully!\n")

    print("Reading all files:\n")

    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        with open(filepath, "r") as f:
            print(file)
            print(f.read())

    print("\nLog file created successfully!")

except Exception as e:
    print("Error:", e)