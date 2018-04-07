#!/usr/bin/python

import sys, commands

passwd_f=commands.getoutput("cat /etc/passwd | grep -v '#'")

if sys.argv[1].isdigit():
   valueName=int(sys.argv[1])
else:
   valueName=sys.argv[1]

for line in passwd_f.split("\n"):
   uid=line.split(":")[2]
   userName=line.split(":")[0].strip("_")
   dictName=[""]
   if userName == valueName or int(uid) >= valueName:
      for lengthrange in range(1,len(line.split(":"))):
         dictName.append(line.split(":")[lengthrange])
      dict={userName : dictName}
      print dict
