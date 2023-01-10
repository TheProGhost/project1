# writing the templates
def write_template(addrss, content, name):
    basic = """
    <!DOCTYPE html>
<html>
    <head>
        <meta cherset="UTF-8">
        <title>
            BIT-INT
        </title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Mono:300">

    </head>

    <body>
        <div class="m-3 p-3 fs-3 fw-bold" style="align-items: center;">
        Address :
        """ 
    
    basic_end = """
    </div>
    </body>

    </html>
    """
    new = basic + addrss + "</div> <div>" + content + basic_end

    print(content)
    filename = "./templates/"+name

    file = open(filename, "w")
    file.writelines(new)
    file.close()

content = """ 
<table class="dataframe table table-stripped">
  <thead>
    <tr style="text-align: left;">
      <th></th>
      <th>Dates</th>
      <th>Description</th>
      <th>More</th>
      <th>Urls</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2 Jun 22</td>
      <td>Bitcoin in 2009: A Surreal Look Into The First Bitcoin Transactions Using A Blockchain Explorer : CryptoCurrency</td>
      <td>715 votes, 162 comments. Jan 3rd, 2009, Satoshi began mining the genesis block. Bitcoin was born. Block 0 - January 03, 2009 at 10:15 AM PST Mined â€¦</td>
      <td><a href="https://www.reddit.com/r/CryptoCurrency/comments/v2z4ry/bitcoin_in_2009_a_surreal_look_into_the_first/" target="_blank">https://www.reddit.com/r/CryptoCurrency/comments/v2z4ry/bitcoin_in_2009_a_surreal_look_into_the_first/</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21 Aug 21</td>
      <td>Items For Sale (digital) - The Bitcoin Forum</td>
      <td>Digital Items For Sale For Bitcoin</td>
      <td><a href="https://forum.bitcoin.com/digital-items/" target="_blank">https://forum.bitcoin.com/digital-items/</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12 May 21</td>
      <td>old-wt - Pastebin.com</td>
      <td>Pastebin.com is the number one paste tool since 2002. Pastebin is a website where you can store text online for a set period of time.</td>
      <td><a href="https://pastebin.com/Z8Ht9LAH" target="_blank">https://pastebin.com/Z8Ht9LAH</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12 May 21</td>
      <td>This is my old wallet, 3 addresses of 50 BTC are mined in 2009.1HL - Pastebin.com</td>
      <td>Pastebin.com is the number one paste tool since 2002. Pastebin is a website where you can store text online for a set period of time.</td>
      <td><a href="https://pastebin.com/qFKyxeZz" target="_blank">https://pastebin.com/qFKyxeZz</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12 May 21</td>
      <td>111111111111111111111111111111111111111This is my old wallet, 3 addr - Pastebin.com</td>
      <td>Pastebin.com is the number one paste tool since 2002. Pastebin is a website where you can store text online for a set period of time.</td>
      <td><a href="https://pastebin.com/f33ta8ev" target="_blank">https://pastebin.com/f33ta8ev</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>14 Mar 21</td>
      <td>Latest posts of: MA40</td>
      <td>Latest posts of: MA40</td>
      <td><a href="https://bitcointalk.org/index.php?action=profile;threads;u=821717;sa=showPosts" target="_blank">https://bitcointalk.org/index.php?action=profile;threads;u=821717;sa=showPosts</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>15 Feb 21</td>
      <td>wallet.dat sale on the forum</td>
      <td>wallet.dat sale on the forum</td>
      <td><a href="https://bitcointalk.org/index.php?topic=5240701.0" target="_blank">https://bitcointalk.org/index.php?topic=5240701.0</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>15 Feb 21</td>
      <td>bitcore/api-documentation.md at master Â· bitpay/bitcore Â· GitHub</td>
      <td>A full stack for bitcoin and blockchain-based applications - bitpay/bitcore</td>
      <td><a href="https://github.com/bitpay/bitcore/blob/master/packages/bitcore-node/docs/api-documentation.md" target="_blank">https://github.com/bitpay/bitcore/blob/master/packages/bitcore-node/docs/api-documentation.md</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>15 Feb 21</td>
      <td>Don't buy "wallet.dat" files with lost passwords; EXCHANGE THEM.</td>
      <td>Don't buy "wallet.dat" files with lost passwords; EXCHANGE THEM.</td>
      <td><a href="https://bitcointalk.org/index.php?topic=5242967.0" target="_blank">https://bitcointalk.org/index.php?topic=5242967.0</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>27 May 19</td>
      <td>'Craig Is a Liar' â€“ Early Adopter Proves Ownership of Bitcoin Address Claimed by Craig Wright : btc</td>
      <td>r/btc: /r/btc was created to foster and support free and open Bitcoin discussion, Bitcoin news, and exclusive AMA (Ask Me Anything) interviews from top Bitcoin industry leaders! Bitcoin is the currency of the Internet. A distributed, worldwide, decentralized digital money. Unlike traditional currencies such as dollars, bitcoins are issued and managed without the need for any central authority whatsoever.</td>
      <td><a href="https://www.reddit.com/r/btc/comments/bpsj1z/craig_is_a_liar_early_adopter_proves_ownership_of/" target="_blank">https://www.reddit.com/r/btc/comments/bpsj1z/craig_is_a_liar_early_adopter_proves_ownership_of/</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>30 Sep 18</td>
      <td>Ð‘Ð»Ð¾ÐºÑ‡ÐµÐ¹Ð½ Ð¸ Ð²Ð¾ÑÑÑ‚Ð°Ð½Ð¸Ðµ Ð·Ð¾Ð¼Ð±Ð¸-Ð±Ð¸Ñ‚ÐºÐ¾Ð¹Ð½Ð¾Ð² -</td>
      <td></td>
      <td><a href="https://bitnovosti.com/2014/08/16/zombie-bitcoins/" target="_blank">https://bitnovosti.com/2014/08/16/zombie-bitcoins/</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2 Jun 18</td>
      <td>Ordereddress (#OD-xxxxxxxxxx...) a new way of saying a bitcoin address</td>
      <td>Ordereddress (#OD-xxxxxxxxxx...) a new way of saying a bitcoin address</td>
      <td><a href="https://bitcointalk.org/index.php?topic=455303.15" target="_blank">https://bitcointalk.org/index.php?topic=455303.15</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2 Jun 18</td>
      <td>hw5/tenthousandblocks.txt at master Â· solinger10/hw5 Â· GitHub</td>
      <td>Contribute to hw5 development by creating an account on GitHub.</td>
      <td><a href="https://github.com/solinger10/hw5/blob/master/data/tenthousandblocks.txt" target="_blank">https://github.com/solinger10/hw5/blob/master/data/tenthousandblocks.txt</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>9 Feb 18</td>
      <td>Dormant/Zombie//Satoshi Nakamoto Address</td>
      <td>BlockChain Statistics Report generated by John W. Ratcliff. This Spreadsheet lists all dormant bitcoin addresses with a balance of 25 bitcoins or more.</td>
      <td><a href="https://docs.google.com/spreadsheets/d/1xTROekDerP1TPOB3SOD_1bbQr580BPqbhF3YHdO96pw/edit#gid=189299283" target="_blank">https://docs.google.com/spreadsheets/d/1xTROekDerP1TPOB3SOD_1bbQr580BPqbhF3YHdO96pw/edit#gid=189299283</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>17 May 16</td>
      <td>How To Prove You Are Satoshi: Demonstrate Control Of The Block 9 Bitcoin Address | Bitcoin Who's Who</td>
      <td></td>
      <td><a href="http://bitcoinwhoswho.com/blog/2016/05/08/how-to-prove-you-are-satoshi-demonstrate-control-of-the-block-9-address/" target="_blank">http://bitcoinwhoswho.com/blog/2016/05/08/how-to-prove-you-are-satoshi-demonstrate-control-of-the-block-9-address/</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>29 Mar 16</td>
      <td>Bitcoin Addresses | BitcoinChain.com</td>
      <td>Get the detailed statistics on Bitcoin Addresses: transactions, hash, balance, received bitcoins.</td>
      <td><a href="http://bitcoinchain.com/block_explorer/catalog" target="_blank">http://bitcoinchain.com/block_explorer/catalog</a></td>
      <td>Loading...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>21 Oct 15</td>
      <td>Rise of the Zombie Bitcoins | Lets Talk Bitcoin</td>
      <td>With approximataly 30% of all bitcoins in existence currently in a state of limbo it remains a nagging question, just what is happening with them and will they ever rise from the dead?This article discusses in detail the character and quantity of these zombie bitcoins, presenting detailed graphical analysis extracted directly from the bitcoin blockchain, and highlights theories as to what their fate might be.</td>
      <td><a href="https://letstalkbitcoin.com/blog/post/rise-of-the-zombie-bitcoins" target="_blank">https://letstalkbitcoin.com/blog/post/rise-of-the-zombie-bitcoins</a></td>
      <td>Loading...</td>
    </tr>
  </tbody>
</table>
"""


# write_template("1FvzCLoTPGANNjWoUo6jUGuAG3wg1w4YjR", content, "websites.html")
