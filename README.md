# Claim Free Tech eBooks

## About

This is a script to claim free tech eBooks from [PacktPub](https://www.packtpub.com/). PacktPub offers its users a free tech eBook each day. For some of us who may forget occasionally that a free eBook awaits them, you can run this script as a cron job. If you have a Raspberry Pi or server running at all times, you may want to place the script there and execute it daily. The script works for a Linux environment. I make no promises about running it elsewhere. I have no problems running it in Ubuntu 15.10. If it doesn't work on your end, feel free to open up an issue! You can also fork the script and make a pull request.

## Requirements:

- Python 3 is installed
- Running in a Linux environment

## Setup (Linux)

1) Download file and move it to /usr/local/bin/

2) Open terminal and run `crontab -e`

3) Add in the following line, replacing USERNAME and PASSWORD with your credentials at the bottom and save:

`30 19 * * * python3 /usr/local/bin/claim_free_ebook.py USERNAME PASSWORD`

4) Enjoy your free eBook!

## Contributing

Feel free to fork and make pull requests! =)
