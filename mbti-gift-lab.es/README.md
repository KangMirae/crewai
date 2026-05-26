# MBTI Gift Lab

Un proyecto para principiantes que demuestra como usar **CrewAI** con un LLM local de **Ollama**. Dado un tipo de personalidad MBTI, un equipo de agentes de IA colabora para generar, criticar y refinar recomendaciones de regalos — todo ejecutandose en tu maquina.

## Que Hace?

Introduces un tipo MBTI (ej. `INFP`, `ESTJ`), y dos agentes de IA trabajan juntos a traves de tres tareas secuenciales:

1. **Lluvia de ideas** — El agente *Listador de Regalos* crea 5 ideas de regalos adaptadas al tipo MBTI.
2. **Critica** — El agente *Selector de Regalos* revisa la lista y elige 2 regalos que son demasiado genericos, explicando por que.
3. **Refinar** — El *Listador de Regalos* toma la retroalimentacion y reemplaza los 2 regalos debiles con mejores y mas personales.

El resultado se guarda en `regalos_finales.md`.

## Como Funciona CrewAI Aqui

CrewAI orquesta multiples **Agentes** de IA, cada uno con un rol, objetivo e historia definidos. A estos agentes se les asignan **Tareas** que se ejecutan secuencialmente — la salida de una tarea alimenta la siguiente. Juntos, forman un **Crew** (equipo).

```
Entrada del Usuario (MBTI)
      │
      ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Lluvia de   │ ──▶ │   Critica     │ ──▶ │   Refinar     │
│    Ideas     │     │  (Selector)   │     │  (Listador)   │
│ (Listador)   │     │               │     │               │
└──────────────┘     └──────────────┘     └──────────────┘
                                                │
                                                ▼
                                        regalos_finales.md
```

## Estructura del Proyecto

```
mbti-gift-lab.es/
├── main.py          # Punto de entrada — recibe input del usuario y ejecuta el crew
├── crew_logic.py    # Logica principal — define el LLM, agentes, tareas y crew
├── agents.yaml      # Definiciones de agentes (roles, objetivos, historias)
├── tasks.yaml       # Definiciones de tareas (descripciones, salidas esperadas)
└── README.md
```

### `main.py`

El punto de entrada de la aplicacion. Pide al usuario un tipo MBTI, crea una instancia de `MbtiLoopCrew` y ejecuta el crew. El resultado final se imprime en la consola.

### `crew_logic.py`

Contiene la clase `MbtiLoopCrew`, que:

- Carga las configuraciones de agentes y tareas desde los archivos YAML.
- Inicializa el LLM (Ollama ejecutando Llama 3.2 localmente).
- Crea dos instancias de `Agent` y tres instancias de `Task`.
- Los ensambla en un `Crew` y lo ejecuta con el tipo MBTI del usuario como entrada.

### `agents.yaml`

Define los dos agentes usados por el crew:

- **listador_regalos** — Un "Listador de Regalos" que propone ideas de regalos segun la personalidad.
- **selector_regalos** — Un "Selector de Regalos" que revisa la lista y marca las opciones genericas.

Cada agente tiene un `role` (rol), `goal` (objetivo) y `backstory` (historia) que guian el comportamiento del LLM.

### `tasks.yaml`

Define las tres tareas que el crew ejecuta en orden:

- **lluvia_ideas_task** — Generar 5 ideas de regalos para el tipo MBTI dado.
- **critica_task** — Identificar 2 regalos genericos y explicar por que deben ser reemplazados.
- **refinamiento_task** — Reemplazar los regalos debiles con alternativas mejores y mas personales.

Cada tarea tiene una `description` (descripcion), `expected_output` (salida esperada) y un `agent` (agente) asignado.

---

## Guia de Instalacion Paso a Paso

### Paso 1 — Instalar uv

[uv](https://docs.astral.sh/uv/) es un gestor de paquetes y proyectos Python rapido.

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Para otras opciones, consulta la [documentacion de instalacion de uv](https://docs.astral.sh/uv/getting-started/installation/).

### Paso 2 — Instalar Ollama

Descarga e instala Ollama desde el sitio oficial: **https://ollama.com/download**

- **macOS** — Descarga la app y arrastrala a Aplicaciones.
- **Linux** — Ejecuta `curl -fsSL https://ollama.com/install.sh | sh`
- **Windows** — Descarga y ejecuta el instalador.

### Paso 3 — Descargar el modelo LLM

```bash
ollama pull llama3.2:1b
```

> **Consejo:** Para mejores resultados, usa el modelo 3b en su lugar:
> ```bash
> ollama pull llama3.2:3b
> ```
> Luego actualiza el nombre del modelo en `crew_logic.py` de `"ollama/llama3.2:1b"` a `"ollama/llama3.2:3b"`.

### Paso 4 — Crear el proyecto e instalar dependencias

```bash
mkdir mbti-gift-lab.es
cd mbti-gift-lab.es
uv init
uv add crewai pyyaml --prerelease allow
```

Esto inicializa un nuevo proyecto Python e instala los dos paquetes necesarios:
- **crewai** — El framework de orquestacion multi-agente.
- **pyyaml** — Para cargar los archivos de configuracion YAML.

### Paso 5 — Iniciar Ollama

```bash
ollama serve
```

> **Nota:** En macOS, si abriste la app de Ollama, ya esta sirviendo en segundo plano. Puedes omitir este paso.

### Paso 6 — Escribir el codigo

Crea los siguientes 4 archivos dentro de tu directorio `mbti-gift-lab.es/`. Puedes encontrar el codigo fuente de cada archivo en este repositorio:

| Archivo | Proposito |
|---------|-----------|
| `agents.yaml` | Define los dos agentes de IA (Listador y Selector) |
| `tasks.yaml` | Define las tres tareas (Lluvia de ideas, Critica, Refinar) |
| `crew_logic.py` | Carga configs, configura el LLM, agentes, tareas y crew |
| `main.py` | Punto de entrada que recibe input del usuario y ejecuta el crew |

### Paso 7 — Ejecutarlo

```bash
uv run main.py
```

Se te pedira que introduzcas un tipo MBTI. Escribe uno (ej. `INFP`) y observa como los agentes colaboran en tiempo real. La lista final de 5 recomendaciones de regalos se imprimira en la consola y se guardara en `regalos_finales.md`.
