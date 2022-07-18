# sjp-rest
Simple REST API capable of requesting words from SJP (Polish dictionary)

## Setup
```
pip install -r requirements.txt
```
## Access API
The API returns a single object containing two keys, word (String) and acceptable (Boolean).
## Example
```
http://127.0.0.1:5000/api/word/tren
```
```
{
"acceptable": true,
"word": "tren"
}
```
