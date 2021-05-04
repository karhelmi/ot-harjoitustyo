from database_initialize import initialize_database


def pytest_configure():
    initialize_database()
