class ClientException(Exception):
    """ClientException"""

    def __init__(self, code, msg, http_status=None, request_id=None, log=None):
        Exception.__init__(self)
        self.error_code = code
        self.message = msg
        self.http_status = http_status
        self.request_id = request_id
        self.log = log

    def __str__(self):
        return "%s %s" % (
            self.error_code,
            self.message,
        )

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.message

    def get_log(self):
        return self.log


class ServerException(Exception):
    """ServerException"""

    def __init__(self, code, msg, http_status=None, request_id=None, log=None):
        Exception.__init__(self)
        self.error_code = code
        self.message = msg
        self.http_status = http_status
        self.request_id = request_id
        self.log = log

    def __str__(self):
        return "%s %s" % (
            self.error_code,
            self.message,
        )

    def get_error_code(self):
        return self.error_code

    def get_error_msg(self):
        return self.message

    def get_log(self):
        return self.log
