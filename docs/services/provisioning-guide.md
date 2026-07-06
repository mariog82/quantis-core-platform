# Provisioning Service Guide

## Purpose

The Provisioning Service manages tenant product activation, resource snapshots and deprovisioning.

## Public API

- `ProvisioningRequest`
- `ProvisioningResult`
- `ProvisioningStatus`
- `ProvisionedEnvironment`
- `ProvisioningService`

## Provider-neutrality

Cloud providers, DNS, storage, database and IAM systems must be implemented as adapters.
