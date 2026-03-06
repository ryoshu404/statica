

class StringExtractor:

    def __init__(self, min_len=6):
        self.min_len = min_len

    def extract(self, data: bytes) -> list[str]:
        strings = []
        buffer = []

        def flush_buffer():

            if len(buffer) >= self.min_len:
                stripped = bytes(buffer).decode("ascii").strip()
                if len(stripped) >= self.min_len:
                    strings.append(stripped)
            buffer.clear()

        for byte in data:
            if not 32 <= byte <= 126:
                flush_buffer()
                continue
            buffer.append(byte)
        flush_buffer()

        return strings
 


