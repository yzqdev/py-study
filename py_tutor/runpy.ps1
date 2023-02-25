$env:PYTHONPATH = pwd
#linux 使用export PYTHONPATH="$PWD"

param(
[string]$path
)
& "$pwd\.venv\Scripts\python.exe"  "$pwd\fast_api\fast_app.py"