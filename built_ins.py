import os
from pathlib import Path
from codes import StatusCode
from colors import Colors


class BuiltIns:
    def __init__(self):
        self.strings = {
            "": self.empty,  # empty (just hitting enter)
            "cd": self.cd,
            "exit": self.exit,
            "ls": self.ls,
        }

    def empty(self, cwd: Path, args: list[str]) -> tuple[StatusCode, Path]:
        return StatusCode.OKAY, cwd

    def ls(self, cwd: Path, args: list[str]) -> tuple[StatusCode, Path]:
        argument_error: str = "1 or 2 required (ls, ls [directory])"
        target = cwd

        if len(args) == 2:
            if os.path.isdir(args[1]):
                target = args[1]
            else:
                print("cd: not a directory:", args[1])
                return StatusCode.ERROR, cwd

        if len(args) > 2:
            print("cd: too many arguments:", argument_error)
            return StatusCode.ERROR, cwd

        for _, dirs, files in os.walk(target):
            for dir in dirs:
                print(Colors.DIRECTORY + dir + Colors.RESET + "/")

            for file in files:
                print(file)
            break

        return StatusCode.OKAY, cwd

    def exit(self, cwd: Path, args: list[str]) -> tuple[StatusCode, Path]:
        return StatusCode.EXIT, cwd

    def cd(self, cwd: Path, args: list[str]) -> tuple[StatusCode, Path]:
        argument_error: str = "1 required (cd [directory])"

        if len(args) == 1:
            cwd = Path.home()
            return StatusCode.OKAY, cwd

        if len(args) > 2:
            print("cd: too many arguments:", argument_error)
            return StatusCode.ERROR, cwd

        dir: str = args[1]
        potential = cwd / dir

        if dir == "..":
            potential = cwd.parent

        if not Path.exists(potential):
            print(f"cd: directory not found: [{potential}]")
            return StatusCode.ERROR, cwd

        cwd = potential

        return StatusCode.OKAY, cwd
