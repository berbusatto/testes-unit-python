<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>Conversor de câmbio</title>
</head>
<body>
<h1>Conversor de câmbio</h1>

@if(isset($result))
    <p>{{ $amount }} {{ $from }} = {{ $result }} {{ $to }}</p>
@endif

<form method="post" action="{{ url('/cambio') }}">
    {{ csrf_field() }}

    <label>Quantidade:</label>
    <input type="text" name="amount">

    <label>De:</label>
    <select name="from">
        <option value="USD">USD</option>
        <option value="EUR">EUR</option>
        <option value="GBP">GBP</option>
    </select>

    <label>Para:</label>
    <select name="to">
        <option value="USD">USD</option>
        <option value="EUR">EUR</option>
        <option value="GBP">GBP</option>
    </select>

    <button type="submit">Converter</button>
</form>
</body>
</html>
