from codes import StatusCode
from built_ins import BuiltIns
from pathlib import Path
from colors import Colors


class Shell:
    def __init__(self):
        self.cwd: Path = Path.cwd()
        self.status: StatusCode = StatusCode.OKAY

    def loop(self):
        while True:
            if self.status == StatusCode.EXIT:
                break
            print()

            self._prompt()
            line = self._read()
            args = self._split_into_args(line)
            self.status = self._execute(args)

    def _prompt(self):
        print(Colors.PROMPT, end="")
        print(f"{self.cwd} ", end="")
        print(Colors.RESET, end="")

    def _execute(self, args) -> StatusCode:
        builts = BuiltIns()
        for command, func in builts.strings.items():
            if args[0] == command:
                code, new_cwd = func(self.cwd, args)
                self.cwd = new_cwd
                return code

        print("sh: command not found:", args[0])
        return StatusCode.ERROR

    def _read(self) -> str:
        return input()

    def _split_into_args(self, line: str) -> list[str]:
        line = line.strip()
        return line.split(" ")
