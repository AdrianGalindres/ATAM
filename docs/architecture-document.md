# Documento de Arquitectura - Sistema de Autenticación (Modelo C4)

## 1. Nivel 1: Diagrama de Contexto del Sistema
* **Usuario (Actor):** Persona que interactúa con la aplicación web para registrarse e iniciar sesión.
* **Frontend SPA (React):** Aplicación de interfaz de usuario alojada en el cliente que gestiona el estado y los formularios de autenticación.
* **Backend Orchestrator (NestJS):** API central que maneja la lógica de negocio, validaciones de seguridad y orquestación de llamadas.
* **Identity Provider & DB (Supabase):** Servicio backend-as-a-service externo que provee Supabase Auth y PostgreSQL.

## 2. Nivel 2: Diagrama de Contenedores
```text
[React SPA] --(HTTP / REST / JSON)--> [NestJS API Gateway] --(Supabase JS Client / Service Role)--> [Supabase (Auth & PostgreSQL)]
