from pathlib import Path
import unittest
from built_ins import BuiltIns
from codes import StatusCode


class BuiltInTester(unittest.TestCase):
    def setUp(self) -> None:
        self.cwd = Path.cwd()
        self.home = Path.home()
        self.built_ins = BuiltIns()
        return super().setUp()

    def test_allEmptyChecks(self):
        self.assertEqual(
            (StatusCode.OKAY, self.cwd), self.built_ins.empty(self.cwd, [])
        )
        self.assertEqual(
            (StatusCode.OKAY, self.home), self.built_ins.empty(Path.home(), [])
        )
        self.assertEqual(
            (StatusCode.OKAY, self.cwd), self.built_ins.empty(self.cwd, ["asd ", "yo "])
        )
        self.assertEqual(
            (StatusCode.OKAY, self.home),
            self.built_ins.empty(Path.home(), ["asd ", "yo "]),
        )

    def test_lsTooManyArgs(self):
        self.assertEqual(
            (StatusCode.ERROR, self.cwd),
            self.built_ins.ls(self.cwd, ["ls", "yo", "yo"]),
        )

    def test_lsOneArgument(self):
        self.assertEqual(
            (StatusCode.OKAY, self.cwd),
            self.built_ins.ls(self.cwd, ["ls"]),
        )

    def test_lsTwoArguments(self):
        self.assertEqual(
            (StatusCode.OKAY, self.cwd),
            self.built_ins.ls(self.cwd, ["ls .."]),
        )

    def test_allExitingChecks(self):
        self.assertEqual((StatusCode.EXIT, self.cwd), self.built_ins.exit(self.cwd, []))
        self.assertEqual(
            (StatusCode.EXIT, self.cwd), self.built_ins.exit(self.cwd, ["asd"])
        )

    def test_cdTooManyArgs(self):
        self.assertEqual(
            (StatusCode.ERROR, self.cwd),
            self.built_ins.cd(self.cwd, ["cd", "123", "456"]),
        )

    def test_cdOneArgumentGoesHome(self):
        self.assertEqual(
            (StatusCode.ERROR, self.cwd),
            self.built_ins.cd(self.cwd, ["cd", "123", "456"]),
        )

    def test_cdDotDotBackwards(self):
        self.assertEqual(
            (StatusCode.OKAY, self.cwd.parent),
            self.built_ins.cd(self.cwd, ["cd", ".."]),
        )

    def test_cdIntoOnePath(self):
        self.assertEqual(
            (StatusCode.OKAY, self.cwd / ".venv"),
            self.built_ins.cd(self.cwd, ["cd", ".venv"]),
        )

    def test_cdNonExistantDirectory(self):
        self.assertEqual(
            (StatusCode.ERROR, self.cwd),
            self.built_ins.cd(self.cwd, ["cd", "whatsupchat"]),
        )


if __name__ == "__main__":
    unittest.main()
