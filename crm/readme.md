# Rutas API

- ```crm/api/login/``` iniciar sesion y obtener token** 

- ```crm/api/prospectos/``` devuelve todos los prospectos si eres **supervisor**, y los asignados si eres agente de ventas**

- GET ```crm/api/prospectos/<int:idagente>/``` lista de prospectos asignados a un agente. **vista exclusiva de supervisor**

- ```crm/api/prospecto/<int:idprospecto>/``` CRUD de prospectos
  - GET  ```crm/api/prospecto/<int:idprospecto>/``` obtener info de un prospecto
  - POST ```crm/api/prospecto/<int:idprospecto>/``` crear un prospecto, en idprospecto pon cualquier numero 😀
  - PUT  ```crm/api/prospecto/<int:idprospecto>/``` actualizar un prospecto

- ```crm/api/sesiones/<int:idprospecto>/``` lista de sesiones de un prospecto

- GET ```api/sesiones/<int:idprospecto>/<str:tipo>/``` obtener todas las sesiones por tipo [todos|llamadas|reuniones]

- ```crm/api/sesion/<int:idprospecto>/<int:idsesion>/```  CRUD de Sesiones 
  - GET  ```crm/api/sesion/<int:idprospecto>/<int:idsesion>/``` obtener info de un sesion
  - POST ```crm/api/sesion/<int:idprospecto>/<int:idsesion>/``` crear un sesion, en idsesion pon cualquier numero 😀
  - PUT  ```crm/api/sesion/<int:idprospecto>/<int:idsesion>/``` actualizar un sesion

# Categorias usuarios

- **1** Activo
- **2** Inactivo
- **3** Potencial

# tipo de sesiones
- **1** LLamada
- **2** Reunión