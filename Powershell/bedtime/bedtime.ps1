# variable for while loop
$x = 1 

# so that we can use a popup message box
add-type -assemblyname presentationcore,presentationframework

# start a never ending while loop
while ($x -eq 1) {
    # check to make sure things were working
    # write-host('x = 1')
    # start small sleep timer (incase I need to stop it) 
    Start-Sleep -s 150
    # grab the current hours in military time and set as a variable
    $time = get-date -Format "HH"
    # another check to make sure it works
    # write-host($time)
    # if loop to check if it is bed time
    # if variable time is greater than or equal to 9 
    # OR if variable time is less than or equal to 4 
    if ($time -ge 17 -Or $time -le 4) {
        # popuo message box warning it is bedtime
        [System.Windows.MessageBox]::Show('It is Bedtime!\nSay good night to your friends.\nWe love you.\nNow go to sleep.\nThis Computer will Shutdown in 5 minutes!!')
        # 5 minute timer
        Start-Sleep -s 300
        # Force shutdown the computer
        Stop-Computer -Force
    }
}
