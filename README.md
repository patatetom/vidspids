# vidspids
USB Vendor IDs Product IDs

```python
from vidspids import VidsPids

vp = VidsPids()

len(vp)
3407

vp.get(32902)
('Intel Corp.', {1: 'AnyPoint (TM) Home Network 1.6 Mbps Wireless Adapter', …})

vp.vendor(0x8086)
'Intel Corp.'

vp.products(0x8086)
{1: 'AnyPoint (TM) Home Network 1.6 Mbps Wireless Adapter', …}
```

```python
from vidspids import VidsPids

vp = VidsPids('/path/to/usb.ids')
```
