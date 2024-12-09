class ServiceResult:
    def __init__(self, success: bool, status_code: int, data=None, error_message=None, error_code=None):
        self.success = success
        self.status_code = status_code
        self.data = data
        self.error_message = error_message
        self.error_code = error_code

    def get_error_map(self):
        return {
            "errorMessage": self.error_message,
            "errorCode": self.error_code
        }