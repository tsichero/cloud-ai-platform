# Architecture

## Runtime flow

1. Client sends a validated request.
2. FastAPI validates the HTTP contract.
3. AIService receives the prompt.
4. Demo mode returns a deterministic response without external credentials.
5. API returns a typed response.
6. Logs provide basic operational visibility.

## Cloud evolution

A production deployment can replace the demo provider with a managed model endpoint and run the container on a managed container runtime.

Before production, the architecture should add authentication, secret management, rate limiting, telemetry, cost controls and infrastructure as code.

## Important distinction

**Implemented:** local API, Docker packaging, tests and configuration.

**Not claimed as deployed:** a live cloud environment, managed LLM endpoint or production observability stack.
