from account import Account

def test_create_account():
    acc = Account()
    assert acc is not None

def test_account_init_10000_won():
    acc = Account()
    ret = acc._balance
    assert ret == 10000