#### Archivo: `docs/utility-tree.md`
```markdown
# Árbol de Utilidad - Evaluación Arquitectónica (ATAM)

## 1. Atributo: Rendimiento (Performance)
* **Escenario 1.1:** Ante un pico de tráfico de 100 registros concurrentes, el sistema debe responder con el token o confirmación de registro en menos de 500 milisegundos.
  * **Estímulo:** 100 peticiones simultáneas de registro hacia `/auth/register`.
  * **Entorno:** Servidor NestJS en producción/desarrollo conectado a Supabase.
  * **Respuesta:** Procesamiento de la solicitud y persistencia/creación en Supabase.
  * **Medida de Respuesta:** Latencia menor a 500ms por cada petición completada con éxito.

## 2. Atributo: Modificabilidad (Modifiability)
* **Escenario 2.1:** Si la organización decide migrar la persistencia o autenticación de Supabase a otro proveedor (ej. Firebase o AWS RDS), el cambio debe aislarse completamente en el módulo de infraestructura de NestJS, sin alterar los componentes de la interfaz de usuario en React.
