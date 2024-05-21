# Bragging to VX-Underground 

This alert is looking for any emails outbound to "staff@vx-underground.org" indicating a potential breach of the sending email account. vx-underground is not malicious itself. This alert exists because of a hacker who was bragging to vx-underground about a compromised government email address. To prove they had control of the account they sent an email to "staff@vx-underground.org", who then posted it on social media. To jump on the bandwagon, several other hackers started emailing proof that they had also compromised government email accounts. We created this alert to find that activity since this is becoming a trend for hackers that want to brag. 

### References: 
https://twitter.com/vxunderground/status/1690330814427365376

# KQL:
```kql
EmailEvents
| where RecipientEmailAddress contains "vx-underground.org"
```