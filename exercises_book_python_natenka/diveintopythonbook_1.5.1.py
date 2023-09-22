try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree
    print(etree.__path__)