from account import Account

def test_create_account():
    sut = Account()
    assert sut is not None