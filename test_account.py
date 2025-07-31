from account import Account

def test_create_account():
    acc = Account(10000)
    assert acc is not None

def test_account_init_10000_won():
    acc = Account(10000)
    assert acc._balance == 10000


def test_deposit_and_confirm():
    acc = Account(10000)
    acc.deposit(500)
    assert acc._balance == 10500
def test_withraw_and_confirm():
    acc = Account(10000)
    acc.withraw(600)
    assert acc._balance == 9600
