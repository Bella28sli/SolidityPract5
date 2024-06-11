from web3 import Web3
from web3.middleware import geth_poa_middleware 
from configuration import CONTRACT_ADDRESS, ABI

# импортим всякое
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545')) 
# наш блокчейн
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
# хз че это
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
# экземпляр контракта

def register(password ):
    mesg = ["none", ""]
    if len(password) >= 8 and not password.__contains__("123") and not password.__contains__("qwerty") and not password.isalpha() and not password.isdigit():
        account = w3.geth.personal.new_account(password)
        mesg[1] = account
    else:
        mesg[0] = "Пароль слишком лёгкий"
    return mesg

def login(public_key, password):
    mesg = ["none", ""]
    try:
        w3.geth.personal.unlock_account(public_key, password)
        mesg[1] = True
    except Exception as e:
        mesg[0] = f"Ошибка авторизации {e}"
    return mesg

def get_contract_balance(account):
    mesg = ["none", ""]
    try:
        balance = contract.functions.getBalance().call({
            'from': account
        })
        mesg[1] = f"Ваш баланс на смарт-контракте: {balance}"
    except Exception as e:
        mesg[0] = f"Ошибка получения баланса: {e}"
    return mesg

def withdraw(account, value):
    mesg = ["none", ""]
    try:
        tx_hash = contract.functions.withdrawall().transact({ 
            'from' : account,
            'value': value
        })
        mesg[1] = f"ваша транзакция успешно отправлена. Хэш транзакции: {tx_hash.hex()}"
    except Exception as e:
        mesg[0] = f"Ошибка отправки WEI: {e}"
    return mesg

def replenishment(account, value):
    mesg = ["none", ""]
    try:
        tx_hash = contract.functions.replenishment().transact({ 
            'from' : account,
            'value': value
        })
        mesg[1] = f"ваша транзакция успешно отправлена. Хэш транзакции: {tx_hash.hex()}"
    except Exception as e:
        mesg[0] = f"Ошибка отправки WEI: {e}"
    return mesg

def createEstate(account, address, area, type):
    mesg = ["none", ""]
    try:
        tx_hash = contract.functions.addEstate(int(area), address, int(type), True, len(get_estates(account)[2])).transact({ 
            'from' : account,
        })
        mesg[1] = f"Вы создали недвижимость. Хэш транзакции: {tx_hash.hex()}"
    except Exception as e:
        mesg[0] = f"Ошибка создания недвижимости: {e}"
    return mesg


def statusEstate(account, id):
    mesg = ["none", ""]
    try:
        tx_hash = contract.functions.eastateStatus(int(id)).transact({ 
            'from' : account,
        })
        mesg[1] = f"Вы изменили статус недвижимости. Хэш транзакции: {tx_hash.hex()}"
    except Exception as e:
        mesg[0] = f"Ошибка изменения статуса недвижимости: {e}"
    return mesg

def sellEstate(account,id):
    mesg = ["none", ""]
    try:
        if str(contract.functions.getEstate().call({'from': account})[int(id)]).__contains__(account):
            mesg[0] = "Вы владелец, нельзя купить"
        else:
            tx_hash = contract.functions.SellEstate(id).transact({ 
                'from' : account,
            })
            mesg[1] = f"Вы купили недвижимость. Хэш транзакции: {tx_hash.hex()}"
    except Exception as e:
        mesg[0] = f"Ошибка покупки недвижимости: {e}"
    return mesg

def createAd(account, estateId, cost, buyer, date):
    mesg = ["none", ""]
    try:
        tx_hash = contract.functions.addAD(buyer, int(cost), int(estateId), date, True, len(get_ads(account)[2])).transact({ 
            'from' : account,
        })
        mesg[1] = f"Вы создали объявление. Хэш транзакции: {tx_hash.hex()}"
    except Exception as e:
        mesg[0] = f"Ошибка создания объявления: {e}"
    return mesg

def statusAD(account, id):
    mesg = ["none", ""]
    try:
        tx_hash = contract.functions.adStatus(int(id)).transact({ 
            'from' : account,
        })
        mesg[1] = f"Вы изменили статус объявления. Хэш транзакции: {tx_hash.hex()}"
    except Exception as e:
        mesg[0] = f"Ошибка изменения статуса объявления: {e}"
    return mesg

def get_estates(account):
    mesg = ["none", "", ""]
    try:
        mesg[2] = contract.functions.getEstate().call({'from':account})
        mesg[1] = f"Недвижимости получены успешно"
    except Exception as e:
        mesg[0] = f"Ошибка получения недвижимости: {e}"
    return mesg

def get_ads(account):
    mesg = ["none", "", ""]
    try: 
        mesg[2] = contract.functions.getAd().call({'from':account})
        mesg[1] = f"Объявления получены успешно"
    except Exception as e:
        mesg[0] = f"Ошибка получения объявлений: {e}"
    return mesg

def get_account_balance(account):
    mesg = ["none", ""]
    try:
        mesg[1] = f"Баланс аккаунта: {w3.eth.get_balance(account)}"
    except Exception as e:
        mesg[0] = f"Ошибка получения баланса: {e}"
    return mesg

    