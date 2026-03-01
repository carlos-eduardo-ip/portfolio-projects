import time
from pathlib import Path

def wait_for_download(directory: Path, timeout: int = 60):
    """Espera até que não existam arquivos temporários de download (.crdownload)."""
    seconds = 0
    temporary_files = "*.crdownload"
    
    while seconds < timeout:
        time.sleep(1)
        files = list(directory.glob(temporary_files))
        if not files and any(directory.iterdir()):
            return True
            
        seconds += 1
    return False
