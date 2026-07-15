import re
import unicodedata


class SemanticNormalizer:
    def normalize(self, value: str) -> str:
        normalized = unicodedata.normalize("NFKD", value)
        normalized = "".join(
            character
            for character in normalized
            if not unicodedata.combining(character)
        )
        normalized = normalized.lower().strip()
        normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
        return normalized.strip("_")
