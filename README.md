# Claim-Free-Tech-eBooks

A script to claim free tech eBooks.

## Requirements:

- Python 3 is installed
- Running in a Linux environment

## Setup (Linux)

1) Download file and move it to /usr/local/bin/

2) Open terminal and run `crontab -e`

3) Add in the following line, replacing USERNAME and PASSWORD with your credentials at the bottom and save:

`30 19 * * * python3 /usr/local/bin/claim_free_ebook.py USERNAME PASSWORD`

4) Enjoy your free eBook!

Feel free to fork and make pull requests!
