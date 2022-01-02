"""
this module allows to convert the vendor and product identifiers present
in the usb.ids file into a dictionary
any other file can be passed as a parameter as long as it respects the
original formatting
see http://www.linux-usb.org/usb.ids
"""

import re

# caret (^) is not used because re.match operates at the beginning of the string
regexp = re.compile("\t?[0-9a-f]{4}  .")


class VidsPids(dict):
    """
    builds a dictionary from the usb.ids file
    """

    def __init__(self, source="/usr/share/hwdata/usb.ids"):
        super().__init__()
        for line in open(source, errors="backslashreplace"):
            line = line.rstrip()
            if regexp.match(line.lower()):
                if line[0] != "\t":
                    vid, vendor = int(line[:4], 16), line[6:]
                    self[vid] = (vendor, {})
                else:
                    line = line[1:]
                    pid, product = int(line[:4], 16), line[6:]
                    self[vid][1][pid] = product

    def vendor(self, vendorid):
        """
        returns the name of the specified vendor
        the vendor ID is an integer (32902 or 0x8086)
        """
        vidpids = self.get(vendorid)
        return vidpids[0] if vidpids else ""

    def products(self, vendorid):
        """
        returns the specified vendor's products dictionary
        the vendor ID is an integer (32902 or 0x8086)
        """
        vidpids = self.get(vendorid)
        return vidpids[1] if vidpids else {}

    def product(self, vendorid, productid):
        """
        returns the specified product for the specified vendor
        the vendor ID and the product ID are integers (32902 or 0x8086)
        """
        pids = self.products(vendorid)
        return pids.get(productid) if pids else ""
