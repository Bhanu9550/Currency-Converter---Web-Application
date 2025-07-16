document.getElementById('convert-btn').addEventListener('click', async () => {
  const amount = document.getElementById('amount').value;
  const fromCurrency = document.getElementById('from-currency').value;
  const toCurrency = document.getElementById('to-currency').value;
  const resultElement = document.getElementById('result');

  if (!amount || isNaN(amount)) {
    resultElement.textContent = 'Please enter a valid amount';
    return;
  }

  try {
    const response = await fetch(`/convert?from=${fromCurrency}&to=${toCurrency}&amount=${amount}`);
    const data = await response.json();

    if (data.error) {
      resultElement.textContent = `Error: ${data.error}`;
    } else {
      resultElement.textContent = `${amount} ${fromCurrency} = ${data.converted_amount} ${toCurrency}`;
    }
  } catch (error) {
    resultElement.textContent = 'Failed to fetch exchange rates';
  }
});