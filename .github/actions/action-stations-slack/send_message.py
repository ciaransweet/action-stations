import sys

from slack_sdk import WebClient


MESSAGE_FORMAT=(
    ":rotating_light: *ACTION STATIONS* :rotating_light: \n"
    "Someone just kicked off a build on `ciaranevans/action-stations`!\n"
    "You can take a look at the GitHub Actions Workflow by clicking"
    " <{0}|*HERE*> :sleuth_or_spy:"
)


def send_message(token: str, github_build_url: str, channel: str) -> None:
    client = WebClient(token=token)
    message = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": MESSAGE_FORMAT.format(github_build_url)
			}
		}
	]
    client.chat_postMessage(
        channel=channel,
        blocks=message,
        text="A build was kicked off!"
    )

if __name__ == "__main__":
    send_message(sys.argv[1], sys.argv[2], sys.argv[3])
