import os


def remove():
        if os.path.exists("crop4.jpg"):
               os.remove("crop4.jpg")
        else:
                pass

        if os.path.exists("ocr.txt"):
               os.remove("ocr.txt")
        else:
                pass
