import re

def remove_powershell_string_format(string):
    # First, escape any backslashes in the string
    string = string.replace('\\', '\\\\')

    # Use a regular expression to match and capture the parts of the string
    # that are wrapped in quotes, as well as any characters preceding or
    # following the quotes that are not backslashes or dollar signs
    regex = r'(^|[^\\$])(\$[^{]*?\{[^}]*?\}[^\\$]*?)($|[^\\$])'
    match = re.search(regex, string)
    while match:
        # Extract the captured groups from the match
        pre_quote = match.group(1)
        quoted_string = match.group(2)
        post_quote = match.group(3)

        # Replace the quoted string with just the contents of the quotes
        # (excluding the quotes themselves)
        replacement = quoted_string[1:-1]
        string = string[:match.start()] + pre_quote + replacement + post_quote + string[match.end():]

        # Search for the next occurrence of the pattern in the string
        match = re.search(regex, string)

    # Use another regular expression to match and capture any dollar signs
    # that are not preceded by a backslash
    regex = r'(^|[^\\])(\$)'
    match = re.search(regex, string)
    while match:
        # Extract the captured groups from the match
        pre_dollar = match.group(1)
        dollar_sign = match.group(2)

        # Replace the dollar sign with an empty string
        string = string[:match.start()] + pre_dollar + string[match.end():]

        # Search for the next occurrence of the pattern in the string
        match = re.search(regex, string)

    return string
