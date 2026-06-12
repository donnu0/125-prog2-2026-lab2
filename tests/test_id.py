import importlib
import io
import unittest
from contextlib import redirect_stderr, redirect_stdout


class IdCommandTests(unittest.TestCase):
    def test_id_without_arguments_prints_identity(self):
        id_command = importlib.import_module("commands.id.id")
        stdout = io.StringIO()
        stderr = io.StringIO()

        with redirect_stdout(stdout), redirect_stderr(stderr):
            exit_code = id_command.run(["id"], [])

        self.assertEqual(exit_code, 0)
        self.assertIn("uid=", stdout.getvalue())
        self.assertIn("gid=", stdout.getvalue())
        self.assertIn("user=", stdout.getvalue())
        self.assertEqual(stderr.getvalue(), "")

    def test_id_with_extra_argument_prints_usage_to_stderr(self):
        id_command = importlib.import_module("commands.id.id")
        stdout = io.StringIO()
        stderr = io.StringIO()

        with redirect_stdout(stdout), redirect_stderr(stderr):
            exit_code = id_command.run(["id", "test"], [])

        self.assertEqual(exit_code, 2)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("usage: id", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
