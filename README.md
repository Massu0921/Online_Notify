# Online_Notify
Raspberry Pi等のコンピュータの起動時に、ホスト名とローカルIPアドレスをSNSに通知します。

## 対応SNS
現在、SlackとDiscordに対応しています。

## 準備・設定
Python3.7にて動作を確認しています。

### Slack
**Incoming Webhooks**を使用します。以下を参考に、任意のチャンネルのWebhook URLを発行してください。 \
https://api.slack.com/messaging/webhooks \
\
"config.json"に、WebhookのURLを設定します。
```json
{
	"discord": {
		"token": "",
		"ch_notify": ""
	},
	"slack": {
		"wh_url": "https://hooks.slack.com/... //Webhook URL for sending notification"
	}
}
```
\
起動時にスクリプトが実行されるように設定します。以下はcrontabでの設定例です。\
`crontab -e`
```
@reboot python3 リポジトリまでのフルパス/Online_Notify/slack_online_notify.py
```

### Discord
以下のライブラリをインストールしてください。\
\
**Discord.py** https://discordpy.readthedocs.io/ja/latest/index.html \
`python3 -m pip install discord.py`
\
\
**Discord Bot**を使用します。以下を参考に、Discord Developer PortalからApplicationを作成してBotを追加し、任意のサーバーに作成したBotを招待してください。\
https://discordpy.readthedocs.io/ja/latest/discord.html#inviting-your-bot \
\
"config.json"に、BotのTokenと任意のチャンネルIDを設定します。
```json
{
	"discord": {
		"token": "xxxxxxxxxxxxxx //Your Discord Bot Token",
		"ch_notify": "xxxxxxxxx  //Channel ID for sending notification"
	},
	"slack": {
		"wh_url": ""
	}
}
```
\
起動時にスクリプトが実行されるように設定します。以下はcrontabでの設定例です。\
`crontab -e`
```
@reboot python3 リポジトリまでのフルパス/Online_Notify/discord_online_notify.py
```

## 通知メッセージ例
```
Sun Dec  8 23:13:32 2019
"Your PC Name" is Connected :globe_with_meridians:
IP Address: ['xxx.xxx.xx.x']
```
