
class BBBException(Exception):
    HTTP_ERROR = "httpError"
    NOT_FOUND = "notFound"
    NO_ACTION = "noActionSpecified"
    ID_NOT_UNIQUE = "idNotUnique"
    NOT_STARTED = "notStarted"
    ALREADY_ENDED = "alreadyEnded"
    INTERNAL_ERROR = "internalError"
    UNREACHABLE_SERVER = "unreachableServer"
    INVALID_RESPONSE = "invalidResponse"
    GENERAL_ERROR = "generalError"

    def __init__(self, key, message):
        Exception.__init__(self, message)
        self.key = key

