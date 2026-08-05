"""
Observer Design Pattern

This program demonstrates the Observer
design pattern by notifying subscribers
when a new video is published.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """Abstract observer class."""

    @abstractmethod
    def update(self, message: str) -> None:
        """Receive updates from the subject."""


class Subscriber(Observer):
    """Represents a YouTube subscriber."""

    def __init__(self, name: str):
        self.name = name

    def update(self, message: str) -> None:
        print(f"{self.name} received notification: {message}")


class YouTubeChannel:
    """Represents the subject."""

    def __init__(self):
        self.subscribers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self.subscribers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.subscribers.remove(observer)

    def notify(self, message: str) -> None:
        for subscriber in self.subscribers:
            subscriber.update(message)

    def upload_video(self, title: str) -> None:
        print(f"New Video Uploaded: {title}")
        self.notify(f"'{title}' is now available.")


def main():

    channel = YouTubeChannel()

    subscriber1 = Subscriber("Alice")
    subscriber2 = Subscriber("Bob")
    subscriber3 = Subscriber("Charlie")

    channel.subscribe(subscriber1)
    channel.subscribe(subscriber2)
    channel.subscribe(subscriber3)

    channel.upload_video("Python Design Patterns")


if __name__ == "__main__":
    main()
