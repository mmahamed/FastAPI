def test_equal_or_not_equal():
    validated = True
    assert 3 == 3
    assert 3 != 1
    assert validated is True
    assert type(validated is bool)
    assert "hello" == "hello"
    assert "hello" != "world"


def test_list():
    num_list = [1, 2, 3, 4, 5]
    any_list = [False, False]
    assert len(num_list) == 5
    assert 1 in num_list
    assert 10 not in num_list
    assert all(num_list)
    assert not any(any_list)

def test_is_instance():
    assert isinstance('this is a string', str)
    assert not isinstance('10', int)