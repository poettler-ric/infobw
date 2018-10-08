+++
title = "Unit 01"
+++

# Misc

## Tutor

Richard Poettler (richard.poettler (at) student.tugraz.at)

## Dates

Days and times are changing - check
[online.tugraz.at](https://online.tugraz.at/tug_online/wbTermin_list.wbLehrveranstaltung?pStpSpNr=216507)
beforehand.

# Communication

## Coding

1. [Search engine](https://www.google.com/)
2. Newsgroup
3. Tutor

## Administrative

- Tiago Santos, Helmut Leitner

## Internet access

- ZID

# Assignments

| Assignment   | Due Date         | Points |
| ------------ | ---------------- | ------ |
| Assignment 0 | 14.10.2018 23:59 | 0      |
| Assignment 1 | 21.10.2018 23:59 | 10     |
| Assignment 2 | 09.11.2018 23:59 | 15     |
| Assignment 3 | 06.01.2018 23:59 | 25     |

{{% alert theme="danger" %}}Do NOT copy code!{{% /alert %}}

{{% alert theme="warning" %}}Assignment interviews are mandatory.{{% /alert %}}

# Software

## Thunderbird

[Download link](https://www.thunderbird.net/)

- Create newsgroup account:
    - Accounts - Newsgroups
    - Konten einrichten - Newsgruppen
- Server: news.tugraz.at
- Groups:
    - tu-graz.test
    - tu-graz.inf1

### How to use

- Use meaningful subject
- Do NOT post solutions to assignments

## Notepad++

[Download link](https://notepad-plus-plus.org/)

### Replace tabs with spaces

- Settings - Preferences

![npp](npp.png)

## Python / Anaconda

[Donwload link](https://www.anaconda.com/)

{{% alert theme="warning" %}}Set PATH during installation.{{% /alert %}}

![anaconda](anaconda.png)

# Assignment 0

## Code

assignment0.py:

```python
print("Hello world!")
```

README.txt:
```
Some meaningful text.
```

### Show file extensions

- Organize - Folder and search options - View - Hide extensions for known file
  types

![extensions1](extensions1.png)
![extensions2](extensions2.png)

## Testing

![cmd](cmd.png)

1. Open command prompt (Start - cmd - [enter])
2. Navigate to your python script
    - `cd` to open a folder (change directory)
        - `cd ..` moves to the parent folder.
    - `dir`/`ls` lists directory content.
3. Execute script: `python assignment0.py`

## Create archive

- Mark files - right click - Send to - Compressed (zipped) folder

![compress](compress.png)

- Alternative: [7zip](https://www.7-zip.org/)

## Upload

[Palme](https://palme.iicm.tugraz.at/)

![palme](palme.png)

## Verify

- Count `[  OK  ]` in `[PALME] AutoTest Notification` mail (should occur four
  times):

```
*** Automatisch vom Palme Learnmanagementsystem generierte E-Mail ***

Diese Mail ergeht an: palme@iicm.tugraz.at, Richard Pöttler

=====================================================================================
TESTSCRIPT

Name:              Assignment Test - Informatik BW
Version:           1
Description:       Test fuer Assignments aus InfBW
Configuration:     infbw_ass1_ws15.xml
=====================================================================================
SUBMISSION

Assignment Group:  11991
Submission ID:     40698
Inspectation ID:   40698
Test Time:         2015 Oct 20 08:36:01
=====================================================================================
UNPACK

archive has correct name: [  OK  ]
archive has correct type: [  OK  ]

OUTPUT
    Archive:  Term_10/Course_21/Assignment_115/Group_11991/Submission_2_assignment1.zip
      inflating: /Course_21/Assignment_115/Group_11991/40698/1445322961/assignment1.py
      inflating: /Course_21/Assignment_115/Group_11991/40698/1445322961/readme.txt
    Returnvalue was: 0 - should be 0
=====================================================================================
CHECK

check #1
  Result:
    [  OK  ] File assignment1.py present
check #2
  Result:
    [  OK  ] File readme.txt present
=====================================================================================

Eine Hilfestellung zum Output von evtl. nicht bestandenen Testcases finden Sie unter: https://de.wikipedia.org/wiki/Diff#Ausgabe



-- 
Ihr Palme Team
Palme LMS

Sie erreichen uns unter: https://palme.iicm.tugraz.at
```

