def make_uppercase(value):
    """make the string uppercased"""
    return value.upper()

def capitalize_words(value: str) -> str:
  """Принимает на вход строку и возвращает ее,

  делая заглавными первые буквы каждого слова.
  """
  return " ".join(word.capitalize() for word in value.split())
