# M1 PR4 — EventBus + Configuration

## Purpose

Introduce reusable domain event and configuration contracts.

## Scope

- DomainEvent
- EventPublisher
- EventSubscriber
- InMemoryEventBus
- EventBusService
- ConfigValue
- ConfigurationProvider
- InMemoryConfigurationProvider
- ConfigurationService

## Rules

EventBus and Configuration remain core platform capabilities and must not contain vertical-specific logic.
