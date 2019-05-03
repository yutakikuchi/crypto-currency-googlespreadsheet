## crypto-currency-googlespreadsheet

### 内容
- Google Spreadsheetだけを用いた暗号通貨の値動きを抽出したもの
- Google SpreadsheetのIMPORTXML関数にて暗号通貨のhistoricalデータをスクレイピング
- Google SpreadsheetのGoogleFinance関数にてUSD to JPYに変換

### 導入手順
- 格納されているtsvをGoogle Spreadsheetに貼り付ける
- 抽出したい期間を変更する場合は、tsvの中の下記URLパラメータを修正する
  - https://coinmarketcap.com/ja/currencies/bitcoin/historical-data/?start=20140101&end=20141231
