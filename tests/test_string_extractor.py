from statica.extractors.string_extractor import StringExtractor

def test_basic_extraction():
    
    extractor = StringExtractor()
    content = b"hello world\x00\x01\x02malware"
    result = extractor.extract(content)

    assert 'hello world' in result
    assert 'malware' in result

def test_min_length():

    extractor = StringExtractor(min_len=6)
    content = b'nah'
    result = extractor.extract(content)

    assert result == []

def test_empty_input():

    extractor = StringExtractor(min_len=6)
    content = b''
    result = extractor.extract(content)

    assert result == []
