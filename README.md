<<<<<<< HEAD
\# Quantis Core Platform™



> \*\*Enterprise Modular Framework for Building Secure, Scalable and Reusable SaaS Platforms\*\*



!\[Version](https://img.shields.io/badge/version-0.2.0--alpha.2-blue)

!\[Python](https://img.shields.io/badge/python-3.12+-green)

!\[Architecture](https://img.shields.io/badge/architecture-Hexagonal-success)

!\[Status](https://img.shields.io/badge/status-Active%20Development-brightgreen)

!\[License](https://img.shields.io/badge/license-Proprietary-orange)



\---



\# Vision



\*\*Quantis Core Platform™\*\* è un framework enterprise modulare progettato per realizzare prodotti SaaS verticali condividendo un'unica infrastruttura applicativa.



L'obiettivo del progetto è eliminare la duplicazione del codice tra applicazioni diverse, separando completamente:



\- infrastruttura tecnica;

\- modello di programmazione;

\- moduli funzionali riutilizzabili;

\- prodotti verticali.



Ogni nuovo prodotto sviluppato con Quantis utilizza la stessa piattaforma di base, cambiando esclusivamente i moduli installati.



\---



\# Filosofia Architetturale



La piattaforma è organizzata in quattro livelli indipendenti.



```

&#x20;               +----------------------+

&#x20;               |     Vertical Apps    |

&#x20;               +----------▲-----------+

&#x20;                          |

&#x20;               +----------+-----------+

&#x20;               |       Modules        |

&#x20;               +----------▲-----------+

&#x20;                          |

&#x20;               +----------+-----------+

&#x20;               |      Framework       |

&#x20;               +----------▲-----------+

&#x20;                          |

&#x20;               +----------+-----------+

&#x20;               |         Core         |

&#x20;               +----------------------+

```



Ogni livello può dipendere esclusivamente dal livello sottostante.



\---



\# Architettura della piattaforma



\## Core



Il Core contiene esclusivamente capacità fondamentali riutilizzabili.



```

core/



identity/

tenant/

rbac/

audit/

configuration/

eventbus/

observability/

```



Responsabilità:



\- Identity

\- Tenant Management

\- RBAC

\- Audit

\- Configuration

\- Event Bus

\- Logging

\- Metrics

\- Tracing

\- Security



Il Core \*\*non contiene business logic\*\*.



\---



\## Framework



Il Framework definisce il modello di sviluppo delle applicazioni.



```

framework/



contracts/

runtime/

plugins/

workflow/

testing/

services/

```



Responsabilità:



\- Runtime Kernel

\- Module Lifecycle

\- Dependency Injection

\- Plugin Runtime

\- Workflow Engine

\- Base Services

\- Contracts

\- Validation

\- Runtime Context



Il Framework è indipendente dai moduli applicativi.



\---



\## Modules



I moduli implementano funzionalità riutilizzabili.



```

modules/



analytics/

dashboard/

reporting/

notification/

storage/

search/

scheduler/

ai/

```



Ogni modulo può essere installato o rimosso senza modificare il Framework.



\---



\## Verticals



I prodotti verticali utilizzano esclusivamente Core, Framework e Modules.



Esempi:



```

verticals/



DeliberaScuola AI



ATTENTIS AI



Political Intelligence Platform



Festival Intelligence Platform



Health Intelligence Platform



...

```



Nei verticali \*\*non è consentito duplicare codice infrastrutturale\*\*.



\---



\# Principi Architetturali



Quantis Core Platform™ adotta i seguenti principi.



\- Clean Architecture

\- Hexagonal Architecture

\- Domain Driven Design (DDD)

\- SOLID

\- Event Driven Architecture

\- API First

\- Cloud Native

\- Modular Monolith Ready

\- Microservices Ready

\- Test First

\- Secure by Design

\- Multi Tenant

\- Provider Agnostic



\---



\# Tecnologie



\- Python 3.12+

\- FastAPI

\- SQLAlchemy

\- Alembic

\- Pydantic

\- Pytest

\- Ruff

\- MyPy

\- GitHub Actions



\---



\# Stato della Roadmap



\## M0 — Repository Baseline



Status



✅ Completed



Contenuti



\- Repository

\- Git Strategy

\- CI/CD

\- Repository Standards

\- Coding Standards



\---



\## M1 — Core Foundation



Status



✅ Completed



Implementato



\- Identity

\- Tenant

\- RBAC

\- Audit

\- EventBus

\- Configuration

\- Observability



\---



\## M2 — Framework Contracts



Status



✅ Beta Freeze



Completato



\- Framework Skeleton

\- Runtime Kernel

\- Runtime Lifecycle



Completato



\✅ Dependency Injection

\✅ Unit of Work

\✅ API Contracts

\✅ Plugin Runtime

\✅ Workflow Runtime

\✅ Dashboard Runtime

\✅ Reporting Runtime



\---



\## Milestone future



\### M3



Enterprise Services



\### M4



AI Platform



\### M5



Cloud Platform



\### M6



Enterprise Security



\### M7



SDK



\### M8



Developer Experience



\### M9



Marketplace



\### M10



Quantis Core Platform™ 1.0 LTS



\---



\# Repository



```

quantis-core-platform/



core/

framework/

modules/

verticals/



deployment/

docs/

examples/

sdk/

tests/

tools/



.github/

```



\---



\# Branching Strategy



```

main

```



Versioni stabili.



```

develop

```



Integrazione continua.



```

feature/\*

```



Nuove funzionalità.



```

release/\*

```



Preparazione release.



```

hotfix/\*

```



Correzioni urgenti.



\---



\# Quality Gates



Ogni Pull Request deve superare:



\- Ruff

\- MyPy

\- Pytest

\- GitHub Actions

\- Documentazione aggiornata

\- ADR aggiornata

\- Changelog aggiornato



Nessuna Pull Request viene integrata se anche un solo Quality Gate fallisce.



\---



\# Versioning



Il progetto utilizza Semantic Versioning.



Formato



```

MAJOR.MINOR.PATCH

```



Versione corrente

0.2.0-beta.1



\---



\# Design Principles



Ogni componente della piattaforma deve rispettare le seguenti regole.



\- nessuna dipendenza circolare;

\- nessun accesso diretto tra moduli;

\- comunicazione mediante Contracts;

\- configurazione esterna;

\- logging centralizzato;

\- audit centralizzato;

\- osservabilità nativa;

\- testabilità completa;

\- estendibilità tramite plugin.



\---



\# Obiettivo Finale



Quantis Core Platform™ mira a diventare una piattaforma enterprise completa per la realizzazione di ecosistemi SaaS modulari.



Su di essa verranno sviluppati tutti i prodotti della famiglia Quantis, condividendo:



\- infrastruttura;

\- runtime;

\- sicurezza;

\- autenticazione;

\- configurazione;

\- osservabilità;

\- plugin;

\- workflow;

\- servizi comuni.



Questo approccio riduce drasticamente tempi di sviluppo, costi di manutenzione e duplicazione del codice, garantendo al tempo stesso elevata qualità, modularità e scalabilità.



\---



\# Licenza



\*\*Copyright © Quantis\*\*



Tutti i diritti riservati.



Quantis Core Platform™ è software proprietario. La riproduzione, distribuzione o utilizzo non autorizzati sono vietati salvo esplicita autorizzazione del titolare.

=======
# Quantis Core Platform™

> Enterprise Modular Framework for Building Secure, Scalable and Reusable SaaS Platforms.

## Current Version

`0.2.0-beta.1`

## Current Status

M2 Framework Contracts is now in beta freeze.

## Architecture Layers

```text
Core
Framework
Modules
Verticals
```

## Completed

- M1 Core Foundation
- M2 Framework Contracts Beta

## Next

M3 — Reusable Modules Foundation
>>>>>>> 06185b7c61e78ae42b568b1c7e634a1031c8930c
