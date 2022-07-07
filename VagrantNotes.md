# Vagrant Notes:
### Start
```
vagrant up
```

### Stop
```
vagrant halt
```

### Pause
```
vagrant suspend
```

### Resume
```
vagrant resume
```

### Status
```
vagrant status
```

### Upgrade
```
vagrant box update
```

### Remove
```
vagrant destroy --force
```
#### Example:
```
vagrant box remove cybersecurity/UbuntuVM --all
```

### Remove old versions
```
vagrant box prune
```

### Purge
```
sudo rm -rf .vagrant*
```

### List all known installation directories
```
vagrant global-status --prune
```

## To Update 
```
vagrant box update
vagrant destroy
vagrant up
vagrant box prune 
```
