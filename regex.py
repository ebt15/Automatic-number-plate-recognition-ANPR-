import re


# To validate Indian Vehicle Licence Numbers
class Regex:

    def validate(result):
        pattern1 = re.compile("[A-Z]{2}\d{2}[A-Z]{1}\d{1}")
        pattern2 = re.compile("[A-Z]{2}\d{2}[A-Z]{2}\d{1}")
        if (re.match(pattern1, result) or re.match(pattern2, result)):
            return True
        else:
            return False


# Test the Regex class
if __name__ == "__main__":
    print(Regex.validate("KL31AC2325"))