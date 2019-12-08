# Online_Notify
Raspberry Pi等のコンピュータの起動時に、ホスト名とローカルIPアドレスをSNSに通知します。

## 対応SNS
現在、Discordのみ対応です。よく鯖落ちするので、Slackとかも検討しようと思います

## 準備・設定
Python3.7にて動作を確認しています。

### Discord
以下のライブラリをインストールしてください。\
\
**Discord.py** https://discordpy.readthedocs.io/ja/latest/index.html \
`python3 -m pip install discord.py`
\
\
Discord Botを使用します。Discord Developer PortalからApplicationを作成してBotを追加し、任意のサーバーに作成したBotを招待してください。\
https://discordpy.readthedocs.io/ja/latest/discord.html#inviting-your-bot \
\
"config.json"に、BotのTokenと任意のチャンネルIDを設定します。
```json
{
	"discord": {
		"token": "xxxxxxxxxxxxxx //Your Discord Bot Token",
		"ch_notify": "xxxxxxxxx  //Channel ID for sending notification"
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
