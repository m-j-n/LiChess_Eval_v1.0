# Compares source code of lichess.org to previous version, returns '1' if different. Adapted from techguides.com


def file_compare(file1, file2):
    f1 = open(file1)
    f2 = open(file2)

    # Read the first line from the files
    f1_line = f1.readline()
    f2_line = f2.readline()

    # Initialize counter for line number
    line_no = 1

    # Loop if either file1 or file2 has not reached EOF
    while f1_line != '' or f2_line != '':

        # Strip the leading whitespaces
        f1_line = f1_line.rstrip()
        f2_line = f2_line.rstrip()

        # Compare the lines from both file
        if f1_line != f2_line:
            return 1

        # Read the next line from the file
        f1_line = f1.readline()
        f2_line = f2.readline()

        # Increment line counter
        line_no += 1

    f1.close()
    f2.close()
    return 0
