import easyocr
import remove
from insert import insert
import find_date
from regex import Regex


class ocr:

    def image_to_text():
        try:
            # Create an OCR instance
            reader = easyocr.Reader(['en'])
            # Read the image file
            result = reader.readtext("crop4.jpg", paragraph="True")
            result = result[0][1]
            # Removing characters from the result so that it only contains the
            # Alphabets and Numbers
            filtered_result = list(
                filter(lambda ch: ch not in " ?.!/;:-", result))
            ocr_text = ''.join([str(elem) for elem in filtered_result])
            date, time = find_date.date_time()
            # Removing the Crop4.jpg file and ocr.txt file
            remove.remove()
            # Inserting the OCR text into the database
            if (Regex.validate(ocr_text)):  # Check if the OCR text is valid
                print(ocr_text)
                insert.connect_insert("sqlite/data.db", ocr_text, date, time)
                return ocr_text

        except Exception as e:
            print(e)
