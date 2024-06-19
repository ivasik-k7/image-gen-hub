import hashlib
import unicodedata


def normalize_string(value: str) -> str:
    """
    Normalize the input string by removing accents, converting to lowercase,
    and removing leading/trailing whitespace.

    Parameters:
    - value (str): The input string to be normalized.

    Returns:
    - str: The normalized string.
    """
    normalized_value = (
        unicodedata.normalize("NFKD", value.casefold())
        .encode("ascii", "ignore")
        .decode("utf-8")
    )
    return normalized_value.strip()


def encode_string(
    value: str,
    key: str,
    algorithm="sha256",
) -> str:
    """
    Encode a string using a key and specified hashing algorithm.

    Parameters:
    - value (str): The input string to be encoded.
    - key (str): The key used for encoding.
    - algorithm (str, optional): The hashing algorithm to use (default is "sha256").

    Returns:
    - str: The hexadecimal digest of the hashed string.
    """
    if not isinstance(key, str):
        raise ValueError("Key must be a string.")

    key_bytes = key.encode("utf-8")
    input_bytes = value.encode("utf-8")

    hash_obj = hashlib.new(algorithm)

    hash_obj.update(key_bytes)
    hash_obj.update(input_bytes)

    hashed_string = hash_obj.hexdigest()

    return hashed_string


def verify_string(value: str, hash: str, key: str, algorithm="sha256") -> bool:
    """
    Verify if a string matches a hashed value using a key and specified hashing algorithm.

    Parameters:
    - value (str): The input string to verify.
    - hash_value (str): The hashed value to compare against.
    - key (str): The key used for hashing.
    - algorithm (str, optional): The hashing algorithm used (default is "sha256").

    Returns:
    - bool: True if the hashed value of the input string matches hash_value, False otherwise.
    """
    if not isinstance(key, str):
        raise ValueError("Key must be a string.")

    key_bytes = key.encode("utf-8")
    input_bytes = value.encode("utf-8")

    hash_obj = hashlib.new(algorithm)

    hash_obj.update(key_bytes)
    hash_obj.update(input_bytes)

    hashed_string_to_verify = hash_obj.hexdigest()

    return hashed_string_to_verify == hash
