from cx_Freeze import setup, Executable

executables = [Executable("appli1.py")]

setup(
    name="lucifer",
    version="1.0",
    description="stanisme et violence",
    executables=executables
)
