def xml_automation(test):
    with open(test, "r") as f:
        temp_copy = f.read().split("\n")