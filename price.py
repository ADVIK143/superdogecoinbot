import requests

def pricesdoge():
    api = requests.get('https://api.pancakeswap.info/api/v2/tokens/0xC87A96F7af449aC18Ae59201dDE32e5A38A41C0F')
    price = str(api.json()['data']['price'])[:11]
    priceBNB = str(api.json()['data']['price_BNB'])[:12]
    welp = "<b><ins>SuperDoge (SDOGE) Token:</ins></b>\n💵 Price: <b>$"+price+"</b>\n💸 Price (in BNB): <b>"+priceBNB+"</b>\n⚖️ Total Supply: <b>6,000,000,000</b>\n⚖️ Circulating Supply: <b>1,858,958,076</b>\n📑 Contract Address: <code>0xC87A96F7af449aC18Ae59201dDE32e5A38A41C0F</code>\n\n💲 Buy Now on <a href='https://exchange.pancakeswap.finance/#/swap?outputCurrency=0xC87A96F7af449aC18Ae59201dDE32e5A38A41C0F'>Pancakeswap!!</a> \n📊 Charts:\n- <a href='https://poocoin.app/tokens/0xC87A96F7af449aC18Ae59201dDE32e5A38A41C0F'>Poocoin</a>\n- <a href='https://charts.bogged.finance/?token=0xC87A96F7af449aC18Ae59201dDE32e5A38A41C0F'>Bogged Finance</a>\n- <a href='https://www.dextools.io/app/pancakeswap/pair-explorer/0x0f718fbec201cc64471779bcf4a5dc3c0df50eee'>Dextools.io</a>\n🌐 Website: https://superdoge.com/"
    return welp
