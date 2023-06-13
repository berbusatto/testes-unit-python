<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class CambioController extends Controller
{
    public function index()
    {
        return view('index');
    }

    public function convert(Request $request)
    {
        $amount = $request->input('amount');
        $from = $request->input('from');
        $to = $request->input('to');

        $response = Http::get('https://api.exchangerate-api.com/v4/latest/'.$from);
        $data = $response->json();
        $rate = $data['rates'][$to];

        $result = $amount * $rate;

        return view('index', compact('result', 'amount', 'from', 'to'));
    }
}
