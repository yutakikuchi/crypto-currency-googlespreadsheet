## crypto-currency-googlespreadsheet

### 内容

- Google Spreadsheetだけを用いた暗号通貨の値動きを抽出したもの
- Google SpreadsheetのIMPORTXML関数にて暗号通貨のhistoricalデータをスクレイピング
- Google SpreadsheetのGoogleFinance関数にてUSD to JPYに変換
  - ※ただし現在のJP価格になっている。date当時のものではない
- Historycalのデータソースは `coinmarketcap.com`
- 対応している暗号通貨は `bitcoin`, `bitcoin-cash`, `ripple`, `ethereum`
- Google Spreadsheetに抽出したデータに対して自身でグラフを作ったり、他のツールにコピペで転載が可能
- DefaultではEnd_Dateから100日遡ってデータを取得している

### 導入手順

- Google Spreadsheetを1つ用意し、sheetタブを2つ作成する
  - 1つは値動きを表示するsheetタブ、もう一つは各種パラメータを設定するもの
- sheetタブの名前はそれぞれ下記のものとする
  - `Parameter Sheet`
  - `Crypto Currency`
- Parameter Sheetの内容は下記スクリプトを実行、Sheetに貼り付ける
  - `python parameter_sheet.py`
- Crypto Currencyの内容は下記スクリプトを実行し、Sheetに貼り付ける
  - `python currency_table_gen.py 100`
