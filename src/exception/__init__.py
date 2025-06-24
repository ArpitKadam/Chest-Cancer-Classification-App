from src.logger import logger
import sys
import traceback

class CustomException(Exception):
    def __init__(self, error_message: str, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message

        _, _, exc_tb = error_details.exc_info()
        self.filename = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        self.lineno = exc_tb.tb_lineno if exc_tb else -1
        self.traceback_str = "".join(traceback.format_exception(*error_details.exc_info()))

        # Logging the full traceback
        logger.error(self.__str__())
        logger.error("Traceback:\n" + self.traceback_str)

    def __str__(self):
        return (
            f"\n--- Exception Details ---\n"
            f"File      : {self.filename}\n"
            f"Line      : {self.lineno}\n"
            f"Message   : {self.error_message}\n"
            f"--------------------------"
        )

if __name__ == "__main__":
    try:
         a = 1/0
         print(a)
    except Exception as e:
        print("Custom Exception")
        raise CustomException(e, sys)