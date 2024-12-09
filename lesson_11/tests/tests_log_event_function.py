import pytest
import sys
import pathlib
from unittest.mock import patch
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from homework_11 import log_event
from core.function_asserts import read_last_line, assert_true
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from utils import BASE_DIR
import os


class TestLogEventFunction:
    @pytest.mark.parametrize("username, status", [
        ("Test Name", "success"),
        ("TestName", "expired"),
        ("TestName", "error"),
        (12345, "success"),
        ("TestUser", 67890),
        ([], "success"),
        ("TestUser", {"key": 1}),
    ])
    def test_log_event_messages_is_correct(self, username, status):
        log_event(username, status)
        content = read_last_line(os.path.join(BASE_DIR, 'login_system.log'))
        assert_true(content, username, status)


    @pytest.mark.parametrize("level, status", [
        ("info", "success"),
        ("warning", "expired"),
        ("error", "failed"),
        ("error", ""),
    ])
    def test_log_event_level_is_correct(self, level: str, status:str):
        with patch('homework_11.logging.getLogger') as mock_get_logger:
            mock_logger = mock_get_logger.return_value
            log_event("TestName", status)

            getattr(mock_logger, level).assert_called_once()

