This repo serves as a POC to show an error communicating with Vesktop over RPC. The connection is made as shown in the logs, but commands sent to Vesktop do send any response.

## How to test
1. Edit `main.py` to include a `CLIENT_ID` and `CLIENT_SECRET` for your Discord Application.
1. Run `python main.py` and it should trigger an authorization popup. You can run against the normal Discord client to see what is expected.
