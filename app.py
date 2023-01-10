from flask import Flask, request, render_template, url_for
from py_src import transactions as txn
from py_src import check_addr as check
from py_src import address_info
from py_src import reports
from py_src import template_write

# constructor
app = Flask(__name__, template_folder='./templates')

# to pass address across pages
var_lst = []
external_links = {
                    "intelx.io":"https://intelx.io/?s=", 
                    "oxt.me":"https://oxt.me/address/", 
                    "walletexplorer.com":"https://www.walletexplorer.com/?q=", 
                    "google.com":"https://www.google.com/search?q="
                }

# favicon.ico
@app.route('/favicon.ico')
def fevicon():
    return url_for('static', filename='image/icons8-reser.ico')


# home page
@app.route('/')
@app.route('/home')
@app.route('/index')
def form():
    return render_template('index.html')


# url with function
@app.route('/data', methods=["GET", "POST"])
def addr():
    if request.method == "POST":
        addrs = request.form.get("addrs")
        if addrs == "":
            empty = True
            return render_template("output.html", empty=empty)
        
        # validate the bitcoin address
        if check.validation(addrs) != True:
            improperAddress = True
            return render_template("output.html", improperAddress=improperAddress, addrs=addrs)
        
        
        app.logger.info(type(addrs))
        var_lst.append(addrs)
        app.logger.info(var_lst[0])
        # var_lst.append(request_addr.get_data(addrs))

        # getting general info
        gen_info = address_info.get_info(var_lst[0])
        app.logger.info("general info done")

        scams_report, scams, website_report, websites = reports.Scams_Reports(var_lst[0])
        var_lst.append(scams)
        var_lst.append(websites)

        return render_template("output.html", address=addrs, external_links=external_links, gen_info = gen_info, 
                                scams_report = scams_report, website_report = website_report )

    return render_template("output.html")


# transactions
@app.route('/transactions', methods=["GET", "POST"])
def trxns():
    result = txn.transactions(var_lst[0])
    return render_template("transactions.html", data=result, address=var_lst[0])


# scam reports
@app.route('/scams', methods=["GET", "POST"])
def scams():
    template_write.write_template(var_lst[0], var_lst[1], "scams.html")
    return render_template("scams.html")


# website appearences
@app.route('/websites', methods=["GET", "POST"])
def websites():
    app.logger.info(var_lst[1])
    app.logger.info(var_lst[2])
    app.logger.info("scams report done.")
    template_write.write_template(var_lst[0], var_lst[2], "websites.html")
    # app.logger.info(type(output))
    return render_template("websites.html")


if __name__ == "__main__":
    app.run(debug=True)
