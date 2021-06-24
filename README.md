# Corporate_Masks
8-14 character Hashcat masks based on analysis of 1.5 million NTLM hashes cracked while pentesting

## corp_8-14.sorted 

sorted mask by efficiency (keyspace/cracked)

## Active Directory NTLM Cracking Cheatsheet

### wordlist

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\uniqpass-v16-passwords.txt -r C:\hashcat\rules\best64.rule --debug-mode=1 --debug-file=matched.rule

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\rockyou.txt -r C:\hashcat\rules\hob064.rule --debug-mode=1 --debug-file=matched.rule

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\uniqpass-v16-passwords.txt -r C:\hashcat\rules\rockyou-30000.rule --debug-mode=1 --debug-file=matched.rule

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\rockyou.txt -r C:\hashcat\rules\rockyou-30000.rule --debug-mode=1 --debug-file=matched.rule

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\xato-net-10-million-passwords.txt -r C:\hashcat\rules\dive.rule --debug-mode=1 --debug-file=matched.rule

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\english.txt -r C:\hashcat\rules\clem9669_large.rule --debug-mode=1 --debug-file=matched.rule

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\realuniq.lst -r C:\hashcat\rules\hob064.rule --debug-mode=1 --debug-file=matched.rule

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\realuniq.lst -r C:\hashcat\rules\best64.rule --debug-mode=1 --debug-file=matched.rule

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\realuniq.lst -r C:\hashcat\rules\best64.rule --debug-mode=1 --debug-file=matched.rule

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\realhuman_phill.txt -r C:\hashcat\rules\clem9669_large.rule --debug-mode=1 --debug-file=matched.rule

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\realuniq.lst -r C:\hashcat\rules\d3adhob0.rule --debug-mode=1 --debug-file=matched.rule

### mask

hashcat -a 3 -m 1000 secretsdump.txt C:\hashcat\masks\mymask.txt

### password reuse

hashcat -m 1000 secretsdump.txt C:\hashcat\wordlists\mywordlist.txt -r C:\hashcat\rules\all.rule --debug-mode=1 --debug-file=matched.rule
