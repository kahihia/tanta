from openexchangerates import OpenExchangeRatesClient
from wallet.models import ForexRates

def get_fx():
	client=OpenExchangeRatesClient('1c70677845b645c7b3ca0ffb90f5d0a5')
	rates=client.latest()
	currencies=client.currencies()
	
	dollars=round(rates['rates']['USD'],2)
	euros=round(['rates']['EUR'],2)
	pounds=round(['rates']['GBP'],2)
	cedis=round(['rates']['GHS'],2)
	shillings=round(['rates']['KES'],2)
	pesos=round(['rates']['MXN'],2)
	naira=round(['rates']['NGN'],2)
	swkrone=round(['rates']['SEK'],2)
	nwkrone=round(['rates']['NOK'],2)
	indrp=round(['rates']['INR'],2)
	chny=round(['rates']['CNY'],2)
	ausd=round(['rates']['AUD'],2)
	saud=round(['rates']['SAR'],2)
	rurub=round(['rates']['RUB'],2)

	rates=ForexRates(
		dollars=dollars,
		euros=euros,
		pounds=pounds,
		cedis=cedis,
		shillings=shillings,
		pesos=pesos,
		naira=naira,
		swkrone=swkrone,
		nwkrone=nwkron,
		indrp=indrp,
		chny=chny,
		ausd=ausd,
		saud=saud,
		rurub=rurub
		)
	rates.save()

