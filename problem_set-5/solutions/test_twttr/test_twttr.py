from twttr import shorten
def test_str():
    assert shorten("twitter")=="twttr"
    assert shorten("DAVID")=="DVD"
    assert shorten ("Manab")=="Mnb"
def test_str2():
    assert shorten("123")=="123"
    assert shorten("wow!12")=="ww!12"


