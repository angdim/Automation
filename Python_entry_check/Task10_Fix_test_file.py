
def xml_automation(test):
    with open(test, "r") as f:
        temp_copy = f.read().split("\n")
        with open("test-automated.xml", "w") as new_file:
            for current_line in temp_copy:
                if temp_copy.index(current_line)+1 < len(temp_copy):
                    if "<subclass>Recovery</subclass>" in temp_copy[temp_copy.index(current_line)+1]:
                        new_line = current_line.replace('<description>', '<description>(Automated) ')
                        new_file.write(new_line + "\n")
                    else:
                        new_file.write(current_line + "\n")
                else:
                    new_file.write(current_line)

xml_automation("test-suite.xml")