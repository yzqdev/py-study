function useNuit()
{

    $start = Get-Date
    python -m nuitka --show-memory --onefile --show-progress --include-qt-plugins=sensible, styles --windows-disable-console --enable-plugin = pyside6    .\mihoyo_main.py


    $end = Get-Date

    Write-Host -ForegroundColor red  ('total runtime: ' + ($end - $start).totalseconds)
}

#pipenv shell
$env:PYTHONPATH = "E:\PycharmProjects\pygui";
pyinstaller --noconfirm --hidden-import httpx --onefile --windowed  "E:/PycharmProjects/pygui/mihoyo_main.py"