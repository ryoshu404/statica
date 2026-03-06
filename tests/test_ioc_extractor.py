from statica.extractors.ioc_extractor import IOCExtractor

def test_ioc_detection():
    
    extractor = IOCExtractor()
    content = ['121.121.121.121', 'google.com', 'https://ryoshu404.com', 'cmd.exe']
    result = extractor.extract(content)

    assert '121.121.121.121' in result.get('ipv4')
    assert 'google.com' in result.get('domains')
    assert 'https://ryoshu404.com' in result.get('urls')
    assert 'cmd.exe' in result.get('files')

def test_no_ioc_detection():
    
    extractor = IOCExtractor()
    content = ['this should not match']
    result = extractor.extract(content)

    assert not result.get('ipv4')
    assert not result.get('domains')
    assert not result.get('urls')
    assert not result.get('files')


