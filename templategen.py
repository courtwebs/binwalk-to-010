import sys

""" A binary item identified by binwalk """
class BinaryItem:
    def __init__(self, address, description):
        self.address = address
        self.description = description

    """ Creates a string of acceptable characters for a variable name for the 010 template """
    def get_name(self):
        # Limiting name length so that we don't get garbage in the name... 
        # this should be done more intelligently so that we preserve more 
        # meaning. Consider maybe escaping illegal characters?
        return"_".join(self.description.split(' '))[:10]

    """ Calculate the size of this item relative to the address of the next identified item """
    def get_size(self, next_item):
        if next_item == None:
            return 1
        else:
            return next_item.address - self.address

""" Turns binwalk output file into a list of BinaryItems """
def parse_binwalk_output(binwalk_output):
    b = []

    with open(binwalk_output) as f:
        linenum = 0
        for line in f:
            linenum += 1    
            s = line.split()

            # First three line are header
            if linenum > 3 and len(s) > 2:
                print(s)
                # 7 spaces delineate the items
                print(" ".join(s[2:]))
                b.append(BinaryItem(int(s[0]), " ".join(s[2:])))

    return b

""" Generates an 010 template from a list of binary items """
def generate_template(binary_items):
    template = ""

    print(len(binary_items))

    for i in xrange(len(binary_items)):
        item = binary_items[i]

        if len(binary_items) > i + 1:
            next_item = binary_items[i+1]
        else:
            next_item = None

        template += "struct {\n\tchar " + item.get_name() + "[" + str(item.get_size(next_item)) + "]\n};\n"

    return template

""" Turns a binwalk output file into an 010 template """
def binwalk_to_template(binwalk_output):
    binary_items = parse_binwalk_output(binwalk_output)
    print(generate_template(binary_items))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " binwalk_output_file")
        exit()

    binwalk_to_template(sys.argv[1])
