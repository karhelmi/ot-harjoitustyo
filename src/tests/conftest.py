from build_database_for_tests import build_database_for_tests


def pytest_configure():
    build_database_for_tests()
