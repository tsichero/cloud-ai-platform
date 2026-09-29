# Cloud AI Platform — Cloud-Native AI Service

> **Portfolio project · Cloud · AI Engineering · Backend · DevOps**

Projeto de referência para demonstrar como estruturar uma aplicação de IA com princípios **cloud-native**, separando API, serviço de IA, configuração, observabilidade, testes e empacotamento.

## Objetivo

Demonstrar decisões de engenharia para levar uma aplicação de IA de um ambiente local para uma arquitetura preparada para cloud, sem confundir **arquitetura planejada** com **deploy efetivamente realizado**.

## Arquitetura

```text
Client
  │
  ▼
FastAPI
  │
  ├── Health / Readiness
  ├── Validation
  └── AI Service
          │
          ├── Model Provider
          └── Response Validation
  │
  ▼
Observability
  ├── Logs
  └── Error Handling

Container → Cloud Runtime
```

## Implementado

- API HTTP com FastAPI
- endpoint de health check
- validação de entrada com Pydantic
- serviço de IA desacoplado do transporte HTTP
- modo demo determinístico para execução sem credenciais
- configuração por variáveis de ambiente
- Dockerfile
- testes automatizados
- logging estruturado básico
- documentação da arquitetura

## Execução

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Health:

```text
GET http://127.0.0.1:8000/health
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## Docker

```bash
docker build -t cloud-ai-platform .
docker run --rm -p 8000:8000 cloud-ai-platform
```

## Testes

```bash
pytest -q
```

Os testes validam health check, contrato da API e comportamento do serviço demo.

## Configuração

Variáveis previstas:

```text
AI_MODE=demo
AI_MODEL=
AI_API_KEY=
```

Nenhum segredo deve ser commitado no repositório.

## Cloud

A aplicação foi estruturada para poder ser adaptada a runtimes como **Azure Container Apps, Azure App Service ou outros ambientes containerizados**.

O repositório não declara um deploy cloud como realizado enquanto ele não tiver sido efetivamente executado e registrado.

## Decisões técnicas

- **FastAPI:** API leve e tipada para serviços Python.
- **Containerização:** reduz diferença entre ambiente local e runtime.
- **AI service separado:** permite trocar o provedor/modelo sem acoplar a API.
- **Demo mode:** permite testes determinísticos sem depender de credenciais externas.
- **Configuração por ambiente:** evita hardcode de segredos.

## Competências demonstradas

**Python · FastAPI · REST · Docker · Cloud Architecture · Azure Concepts · Configuration · Observability · Testing · AI Engineering**

## Roadmap

- [ ] integração com provedor de LLM
- [ ] telemetria distribuída
- [ ] CI/CD completo
- [ ] infraestrutura como código
- [ ] autenticação
- [ ] rate limiting
- [ ] métricas de custo e latência
- [ ] deploy cloud documentado

## Portfólio

[AI & Data Portfolio](https://tsichero.github.io/tsichero.github.io-portfolio-ai/)
