def read_last_line(file):
    """Reads the last line of a given file."""
    with open(file, 'r') as file:
        lines = file.readlines()
        return lines[-1].strip() if lines else None

def assert_true(content, username, status):
    find_text = content.find('Login')
    actual = content[find_text:]
    assert actual == f'Login event - Username: {username}, Status: {status}'