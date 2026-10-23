"""
Factory Method Design Pattern

This program demonstrates the Factory Method
design pattern by creating different types
of notifications.
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    """Abstract base class for notifications."""

    @abstractmethod
    def send(self) -> None:
        """Send the notification."""


class EmailNotification(Notification):
    """Represents an email notification."""

    def send(self) -> None:
        print("Sending Email Notification")


class SMSNotification(Notification):
    """Represents an SMS notification."""

    def send(self) -> None:
        print("Sending SMS Notification")


class PushNotification(Notification):
    """Represents a push notification."""

    def send(self) -> None:
        print("Sending Push Notification")


class NotificationFactory:
    """Creates notification objects."""

    @staticmethod
    def create(notification_type: str) -> Notification:

        notification_type = notification_type.lower()

        if notification_type == "email":
            return EmailNotification()

        if notification_type == "sms":
            return SMSNotification()

        if notification_type == "push":
            return PushNotification()

        raise ValueError("Invalid notification type.")


def main():

    notifications = [
        NotificationFactory.create("email"),
        NotificationFactory.create("sms"),
        NotificationFactory.create("push")
    ]

    for notification in notifications:
        notification.send()


if __name__ == "__main__":
    main()
