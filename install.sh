#!/bin/bash
#tidak saya copy ke bin agar berguna di semua terminal kayak ny :v
go install -v github.com/hahwul/dalfox/v2@latest
sudo cp ~/go/bin/* /usr/bin/
sudo cp ~/go/bin/* /usr/local/bin/
figlet Done
