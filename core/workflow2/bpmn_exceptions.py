class BPMNException(Exception):
    pass


class BPMNParseException(BPMNException):
    pass


class BPMNValidationException(BPMNException):
    pass


class BPMNExportException(BPMNException):
    pass
