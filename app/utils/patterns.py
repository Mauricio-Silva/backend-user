# All Matchs: strings that are not empty and do not consist entirely of spaces

# Match: no spaces; only letters and numbers; length of exactly 24 characters
# Example: 507f1f77bcf86cd799439011
UUID_REGEX = r"^[a-zA-Z0-9]{24}$"

# Match: no spaces; Username or Email
# Example: Ana@TL_15 or ana@gmail.com
QUERY_SEARCH_REGEX = r"^[a-zA-Z0-9._%+-@]+$"

# Match: only letters and spaces
# Example: Ana Maria
NAME_REGEX = r"^[a-zA-Z\s]+$"

# Match: no spaces; only letters, numbers and underscores
# Example: Ana@TL_15
USERNAME_REGEX = r"^[a-zA-Z0-9_]+$"

# Match: basic email validation rules
# Example: ana@gmail.com
EMAIL_REGEX = r"^([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$"

# Match: no spaces; only letters and numbers
# Example: ana123
PASSWORD_REGEX = r"^[a-zA-Z0-9]+$"

# Match: may contain spaces; only letters, numbers and underscores
# Example: I love to play the violin
BIO_REGEX = r"^[a-zA-Z0-9_ ]+$"

# Match: basic url validation rules
# Example: http://www.google.com.br
URL_REGEX = r"^(https?|ftp):\/\/[^\s\$.?#].[^\s]*$"

# Match: basic phone validation rules
# Example: 00900110011
PHONE_REGEX = r"^\d{2}9\d{8}$"
