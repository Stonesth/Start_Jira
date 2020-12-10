from cx_Freeze import setup, Executable


setup(
    name = "start_jira",
    version = "0.1",
    description = "",
    executables = [Executable("start_jira.py")]
)
