

def get_fx():
	from openexchangerates import OpenExchangeRatesClient
	from wallet.models import ForexRates
	ForexRates.objects.all().delete()
	client=OpenExchangeRatesClient('1c70677845b645c7b3ca0ffb90f5d0a5')
	rates=client.latest()
	currencies=client.currencies()
	
	dollars=round(float(rates['rates']['USD']),2)
	euros=round(float(rates['rates']['EUR']),2)
	pounds=round(float(rates['rates']['GBP']),2)
	cedis=round(float(rates['rates']['GHS']),2)
	shillings=round(float(rates['rates']['KES']),2)
	pesos=round(float(rates['rates']['MXN']),2)
	naira=round(float(rates['rates']['NGN']),2)
	swkrone=round(float(rates['rates']['SEK']),2)
	nwkrona=round(float(rates['rates']['NOK']),2)
	indrp=round(float(rates['rates']['INR']),2)
	chny=round(float(rates['rates']['CNY']),2)
	ausd=round(float(rates['rates']['AUD']),2)
	saud=round(float(rates['rates']['SAR']),2)
	rurub=round(float(rates['rates']['RUB']),2)

	rates=ForexRates(
		dollars=dollars,
		euros=euros,
		pounds=pounds,
		cedis=cedis,
		shillings=shillings,
		pesos=pesos,
		naira=naira,
		swkrone=swkrone,
		nwkrone=nwkrona,
		indrp=indrp,
		chny=chny,
		ausd=ausd,
		saud=saud,
		rurub=rurub
		)
	rates.save()

