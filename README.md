# vidspids
USB Vendor IDs Product IDs

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
