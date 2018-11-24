# Binwalk to 010
Pretty simple script that takes output from the binwalk command line utility and turns it into an 010 template.
This is useful for inspecting binary blobs in 010, particularly if binwalk isn't able to extract all of the items it lists on the command line.
I used this to take a manual look at some memory dumped from flash on a Roku 3.

## Usage
```
binwalk my_bin_file > binwalk_output.txt
python tempaltegen.py binwalk_output.txt > template.bt
```
