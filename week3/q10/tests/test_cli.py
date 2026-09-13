"""Tests for the greetlab command-line interface."""

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from greetlab.cli import main  # noqa: E402


class GreetlabCliTests(unittest.TestCase):
    def test_blank_name_exits_with_code_2(self):
        """Whitespace-only names are invalid command-line input."""
        with patch.object(sys, "argv", ["sdt-greet", "--name", "   "]):
            with self.assertRaises(SystemExit) as caught:
                main()

        self.assertEqual(caught.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
