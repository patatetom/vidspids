# vidspids
USB Vendor IDs Product IDs (http://www.linux-usb.org/usb-ids.html)

```python
from vidpid import VidsPids

vp = VidsPids()
# or vp = VidsPids('/path/to/usb.ids')

len(vp)
3407

vp.get(32902)
('Intel Corp.', {1: 'AnyPoint (TM) Home Network 1.6 Mbps Wireless Adapter', …})

vp.vendor(0x8086)
'Intel Corp.'

vp.products(0x8086)
{1: 'AnyPoint (TM) Home Network 1.6 Mbps Wireless Adapter', …}

vp.product(0x8086, 0x0001)
'AnyPoint (TM) Home Network 1.6 Mbps Wireless Adapter'
```

```console
$ vidpid.sh 
hexadecimal (ex. 02ad) vendor ID is required (vid [pid|-] [usb.ids])

$ vidpid.sh 8086
Intel Corp. (8086)

$ vidpid.sh 8086 -
Intel Corp. (8086)

$ vidpid.sh 8086 0001
Intel Corp. (8086)	AnyPoint (TM) Home Network 1.6 Mbps Wireless Adapter (0001)

$ vidpid.sh 8086 - /tmp/usb.ids 
Intel Corp. (8086)

$ vidpid.sh 8086 0001 /tmp/usb.ids 
Intel Corp. (8086)	AnyPoint (TM) Home Network 1.6 Mbps Wireless Adapter (0001)
```
