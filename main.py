from web3 import Web3 
from web3.middleware import geth_poa_middleware
from configuration import CONTRACT_ADDRESS, ABI
from sol import *
from flask import Flask, render_template, request, redirect, url_for

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

app = Flask(__name__)

approved_address = "default"


@app.route('/', methods =['GET', 'POST'])
def index():
    global approved_address
    if request.method == 'POST':
        address = request.form.get('address')
        password = request.form.get('password')
        if request.form["button"] == 'sign in':
            data = login(address, password)
            if data[1]:
                approved_address = address
                return redirect(url_for('home'))
            else:
                return render_template("index.html", error=data[0], new_address=approved_address)
        else:
            data = register(password)
            if data[0] == "none":
                approved_address = data[1]
                return render_template("index.html", new_address=approved_address, error=data[0])
            else:
                return render_template("index.html", error=data[0])
    else:
        return render_template("index.html", error=None)
    
@app.route('/home', methods=['GET', 'POST'])
def home():
    choice = None
    global approved_address
    if request.method == 'POST':
        if request.form['act_button'] == "get_contract_balance":
            if get_contract_balance(approved_address)[0] == "none":
                return render_template("home.html", approved = get_contract_balance(approved_address)[1])
            else:
                return render_template("home.html", error=get_contract_balance(approved_address)[0])
        elif request.form['act_button'] == "get_account_balance":
            if get_account_balance(approved_address)[0] == "none":
                return render_template("home.html", approved = get_account_balance(approved_address)[1])
            else:
                return render_template("home.html", error=get_account_balance(approved_address)[0])        
        elif request.form['act_button'] == "get_estates":
            estates = get_estates(approved_address)
            if estates[0] == "none":
                return render_template("home.html", choice='get_estates',approved= estates[1], estates=estates[2])
            else:
                return render_template("home.html", error=estates[0])
        elif request.form['act_button'] == "get_ads":
            ads = get_ads(approved_address)
            if ads[0] == "none":
                return render_template("home.html", choice='get_ads',approved= ads[1], ads=ads[2])
            else:
                return render_template("home.html", error=ads[0])            
        elif request.form['act_button'] == "return":
            return redirect(url_for('index'))
        
        elif request.form['act_button'] == "createEstate_result":
            result = createEstate(approved_address, request.form['address'], request.form['area'], request.form['type'])
            if result[0] == "none":
                return render_template("home.html", approved = result[1]) 
            else:
                return render_template("home.html", error=result[0])
        elif request.form['act_button'] == "createAD_result":
            result = createAd(approved_address, request.form['estateId'], request.form['cost'], request.form['buyer'], request.form['date'])
            if result[0] == "none":
                print("AAAAAAAAAAAAAAAAA")
                return render_template("home.html", approved = result[1]) 
            else:
                return render_template("home.html", error=result[0])
        elif request.form['act_button'] == "sellEstate_result":
            result = sellEstate(approved_address, request.form['estateId'])
            if result[0] == "none":
                return render_template("home.html", approved = result[1]) 
            else:
                return render_template("home.html", error=result[0])
        elif request.form['act_button'] == "statusEstate_result":
            result = statusEstate(approved_address, request.form['estateId'])
            if result[0] == "none":
                return render_template("home.html", approved = result[1]) 
            else:
                return render_template("home.html", error=result[0])
        elif request.form['act_button'] == "statusAD_result":
            result = statusAD(approved_address, request.form['adId'])
            if result[0] == "none":
                return render_template("home.html", approved = result[1]) 
            else:
                return render_template("home.html", error=result[0])
        elif request.form['act_button'] == "withdraw_result":
            result = withdraw(approved_address, request.form['value'])
            if result[0] == "none":
                return render_template("home.html", approved = result[1]) 
            else:
                return render_template("home.html", error=result[0])
        elif request.form['act_button'] == "replenishment_result":
            result = replenishment(approved_address, request.form['value'])
            if result[0] == "none":
                return render_template("home.html", approved = result[1]) 
            else:
                return render_template("home.html", error=result[0])
        else:
            return render_template("home.html", choice=request.form['act_button'])
    else:
        return render_template("home.html", error=None, approved = None)

if __name__ == "__main__":
    app.run(debug=True)