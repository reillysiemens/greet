def greet(name: str, greeting: str = "Hello, ", punctuation: str = "!") -> str:
    """Greet someone by name."""
    return f"{greeting}{name}{punctuation}"
