function useNuitka() {
    $start = get-date


python -m nuitka --show-memory --onefile --show-progress   --windows-disable-console --enable-plugin=tk-inter   ./gui.py

$end = get-date
write-host -foregroundcolor red ('total runtime: ' + ($end - $start).totalseconds)
}