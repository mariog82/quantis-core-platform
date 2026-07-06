# M4 PR4 — Provisioning Service

## Purpose

The Provisioning Service manages tenant product activation and deprovisioning.

## Components

- ProvisioningRequest
- ProvisioningResult
- ProvisioningStatus
- ProvisionedEnvironment
- ProvisioningService

## Rule

Provisioning remains provider-neutral. Cloud infrastructure, DNS, database, storage and identity providers must be implemented as adapters.
