# vidspids
USB Vendor IDs Product IDs

```python
from vidspids import VidsPids

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

vp.product(0x8086, 61861)
'Z-U130 [Value Solid State Drive]'
```
