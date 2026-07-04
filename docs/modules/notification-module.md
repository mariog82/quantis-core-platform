# M3 PR5 — Notification Module Foundation

## Purpose

Introduce a reusable notification module for alerts, messages and future channel adapters.

## Components

- NotificationMessage
- NotificationPriority
- NotificationChannel
- InMemoryNotificationChannel
- NotificationChannelRegistry
- NotificationService
- NotificationModule

## Rule

The module remains provider-neutral. Email, SMS, PEC, Slack, Teams and push notifications must be implemented as adapters.
