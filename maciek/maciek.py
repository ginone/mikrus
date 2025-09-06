from datetime import datetime, timedelta, timezone

import feedparser
import requests

CHANNEL_ID = "UCmEO_9hLHnZE1lvMNtPgDow"  # channelId feed kanału MaciekiKlocki
NOW = datetime.now(timezone.utc)


def ntfy(message: str, topic: str) -> None:
    print(f"[{NOW}] {message}")
    requests.post(f"https://ntfy.sh/{topic}", data=message.encode(encoding="utf-8"))


def get_new_videos(channel_id: str, since: datetime) -> list[dict[str, str]]:
    feed = feedparser.parse(
        f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    )

    new_videos = []
    for entry in feed.entries:
        published = datetime.fromisoformat(
            entry.published  # type: ignore[reportArgumentType]
        )
        if published > since:
            new_videos.append(
                {
                    "title": entry.title,
                    "link": entry.link,
                    "type": "short" if "shorts" in entry.link else "film",
                    "published": published,
                }
            )

    return new_videos


if __name__ == "__main__":
    try:
        since = NOW - timedelta(hours=1)
        videos = get_new_videos(CHANNEL_ID, since=since)
    except Exception as e:
        ntfy(type(e).__name__, topic="MaciekiKlocki-errors")
        exit(1)
    if videos:
        for v in videos:
            ntfy(f"Nowy {v['type']}: {v['title']}", topic="MaciekiKlocki")
    else:
        print(f"[{NOW}] Brak nowych filmów od {since}.")
