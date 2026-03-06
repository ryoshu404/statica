from statica.extractors.hash_extractor import HashExtractor

def test_hash_extractor_returns_md5_and_sha256():
    
    extractor = HashExtractor()
    content = b'hello world'
    result = extractor.extract(content)
    
    assert result['md5'] == '5eb63bbbe01eeed093cb22bb8f5acdc3'
    assert result['sha256'] == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'